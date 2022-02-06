# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import requests
import json
from frappe.model.document import Document



class Teilnehmerin(Document):
    def before_save(self):
        plz = self.plz
        doc = frappe.get_doc('PLZWR', plz)
        self.wirtschaftsregion = doc.wirtschaftsregion

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

    def after_insert(self):
        settings = frappe.get_doc('GDC Settings')
        values = {"local_part": self.username, "domain": "gdc-bw.de", "name": f"{self.vorname} {self.nachname}", "quota": "100",
                  "password": settings.mcstdpw, "password2": settings.mcstdpw, "active": "1", "force_pw_update": "1", "tls_enforce_in": "0", "tls_enforce_out": "0"}
        headers = {'Content-Type': 'application/json',
                   'X-API-Key': settings.mcapi}
        request = requests.post(
            'https://mail.gdc-bw.de/api/v1/add/mailbox', json=values, headers=headers)

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
    request = requests.post('https://mail.gdc-bw.de/api/v1/edit/mailbox', json=values, headers=headers)