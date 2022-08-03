# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import requests
import json
from frappe.model.document import Document
from unidecode import unidecode
#from moodle import Moodle

class Teilnehmerin(Document):
    def before_save(self):
        pass
        


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
    request = requests.post(
        f'https://{settings.mcdomain}/api/v1/edit/mailbox', 
        json=values, 
        headers=headers)
    frappe.msgprint(
        title = 'Bestätigung',
        msg = 'Mailpasswort wurde zurückgesetzt')

@frappe.whitelist()
def printvalues(doc: str):
    frappe.msgprint(
        title = "Print Data",
        msg = doc
    )

@frappe.whitelist(allow_guest=True)
def getname(teilnehmerin: str):
    doc = frappe.get_doc('Teilnehmerin',teilnehmerin)
    vorname = doc.vorname
    nachname = doc.nachname
    r = [vorname, nachname]
    return r
    # frappe.get_doc('Teilnehmerin',)