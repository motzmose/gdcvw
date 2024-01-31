# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import requests
import json
from frappe.model.document import Document
import random
import string
#from moodle import Moodle

class Teilnehmerin(Document):

    # Read Wirtschaftsregion from Document indexed by zipcode
    def before_save(self):
        plz = self.plz
        doc = frappe.get_doc('PLZWR', plz)
        self.wirtschaftsregion = doc.wirtschaftsregion
        self.wr = doc.kuerzel
        self.email = f'{self.username}@gdc-bw.de'
        pos = random.randint(0, 7)
        characters = "23456789ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        characters = list(characters)
        password = ''
        for i in range(8):
            if i == pos:
                password += random.choice('!?+*#-=')
            else:
                password += random.choice(characters)
        self.password = password

    # Create Username based on Firstname and Lastname before the Document gets its name
    def before_naming(self):
        print(self.username)
        num_retries = 100
        nickname = f'{self.vorname.lower().replace(" ", "")}_{self.nachname.lower().replace(" ", "")}'
        if not self.username:
            for attempt_no in range(num_retries):
                if frappe.db.exists('Teilnehmerin', nickname):
                    nickname = f'{self.vorname.lower().replace(" ", "")}_{self.nachname.lower().replace(" ", "")}'+str(attempt_no)
                else:
                    self.username = nickname
                    break
        else:
            pass

    # Controller Method to start API requests after the Document has been created
    def after_insert(self):
        # print("~~~API REQUESTS IN PROGRESS~~~")
    # Fetch Settings from Single DocType 'GDC Settings'
        settings = frappe.get_doc('GDC Settings')
        # API Request to Mailcow creating a new Mailbox
        mc_values = {"local_part": self.username,
                    "domain": "gdc-bw.de",
                    "name": f"{self.vorname} {self.nachname}",
                    "quota": "100",
                    "password": self.password,
                    "password2": self.password,
                    "active": "1",
                    "force_pw_update": "0",
                    "tls_enforce_in": "0",
                    "tls_enforce_out": "0"}
        mc_headers = {'Content-Type': 'application/json',
                    'X-API-Key': settings.mcapi}
        mc_request = requests.post(
                    f'https://{settings.mcdomain}/api/v1/add/mailbox',
                    json=mc_values,
                    headers=mc_headers)

        # API Request to Moodle creating a new Account
        mdl_params = {"wstoken": settings.mdl_api_key,
                    "moodlewsrestformat": 'json',
                    "wsfunction": 'core_user_create_users',
                    "users[0][password]": self.password,
                    "users[0][username]": self.username,
                    "users[0][firstname]": self.vorname,
                    "users[0][lastname]": self.nachname,
                    "users[0][email]": self.email,
                    "users[0][city]": self.stadt,
                        "users[0][customfields][0][type]":"name_eltern",
                        "users[0][customfields][0][value]":f'{self.eltern_vorname} {self.eltern_nachname}',

                        "users[0][customfields][1][type]":"mail_eltern",
                        "users[0][customfields][1][value]":self.eltern_email,

                        "users[0][customfields][2][type]":"plz",
                        "users[0][customfields][2][value]":self.plz,

                        "users[0][customfields][3][type]":"schulform",
                        "users[0][customfields][3][value]":self.schulform,

                        "users[0][customfields][4][type]":"schule",
                        "users[0][customfields][4][value]":self.schule,

                        "users[0][customfields][5][type]":"region",
                        "users[0][customfields][5][value]":self.wirtschaftsregion,

                        "users[0][customfields][6][type]":"schulform",
                        "users[0][customfields][6][value]":self.schulform,

                        "users[0][customfields][7][type]":"klassenstufe",
                        "users[0][customfields][7][value]":self.klasse,
                    }
        mdl_request = requests.post(f'https://{settings.mdl_domain}/webservice/rest/server.php', mdl_params)
        print(mdl_request)

@frappe.whitelist()
def resetmail(doc: str):
    doc_dict = json.loads(doc)
    print(doc_dict)
    settings = frappe.get_doc('GDC Settings')
    values = {
        "items": [
            f"{doc_dict['username']}@gdc-bw.de"
            ],
        "attr": {
            "password": doc_dict['password'],
            "password2": doc_dict['password'],
            }
        }
    headers = {'Content-Type': 'application/json','X-API-Key': settings.mcapi}
    request = requests.post(
        f'https://{settings.mcdomain}/api/v1/edit/mailbox', 
        json=values, 
        headers=headers)
    frappe.msgprint(
        title = 'Bestätigung',
        msg = 'Mailpasswort wurde zurückgesetzt')