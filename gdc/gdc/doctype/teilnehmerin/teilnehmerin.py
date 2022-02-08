# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import requests
import json
from frappe.model.document import Document
#from moodle import Moodle

class Teilnehmerin(Document):

    # Read Wirtschaftsregion from Document indexed by zipcode
    def before_save(self):
        plz = self.plz
        doc = frappe.get_doc('PLZWR', plz)
        self.wirtschaftsregion = doc.wirtschaftsregion
        self.email = f'{self.username}@gdc-bw.de'

    # Create Username based on Firstname and Lastname before the Document gets its name
    def before_naming(self):
        num_retries = 100
        nickname = f'{self.vorname.lower()}_{self.nachname.lower()}'
        for attempt_no in range(num_retries):
            if frappe.db.exists('Teilnehmerin', nickname):
                nickname = f'{self.vorname.lower()}_{self.nachname.lower()}' + \
                    str(attempt_no)
            else:
                self.username = nickname
                break

    # Controller Method to start API requests after the Document has been created
    def after_insert(self):
        # Fetch Settings from Single DocType 'GDC Settings'
        settings = frappe.get_doc('GDC Settings')
        # API Request to Mailcow creating a new Mailbox
        mc_values = {"local_part": self.username, "domain": "gdc-bw.de", "name": f"{self.vorname} {self.nachname}", "quota": "100",
                     "password": settings.mcstdpw, "password2": settings.mcstdpw, "active": "1", "force_pw_update": "1", "tls_enforce_in": "0", "tls_enforce_out": "0"}
        mc_headers = {'Content-Type': 'application/json',
                      'X-API-Key': settings.mcapi}
        mc_request = requests.post(
            f'https://{settings.mcdomain}/api/v1/add/mailbox', json=mc_values, headers=mc_headers)
        # API Request to Moodle creating a new Account
        mdl_params = {"wstoken": settings.mdl_api_key, "moodlewsrestformat": 'json', "wsfunction": 'core_user_create_users', "password":settings.mdl_std_pwd, "username": self.username, "firstname": self.vorname, "lastname": self.nachname, "email": self.email, "city": self.stadt}
        mdl_request = requests.post(f'https://{settings.mdl_domain}/webservice/rest/server.php', mdl_params)
        print(mdl_request)
@frappe.whitelist()
def resetmail(doc: str):
    doc_dict = json.loads(doc)
    settings = frappe.get_doc('GDC Settings')
    values = {
        "items": [
            f"{doc_dict['username']}@gdc-bw.de"
            ],
        "attr": {
            "password": settings.mcstdpw,
            "password2": settings.mcstdpw,
            }
        }
    headers = {'Content-Type': 'application/json','X-API-Key': settings.mcapi}
    request = requests.post(f'https://{settings.mdl_domain}/api/v1/edit/mailbox', json=values, headers=headers)