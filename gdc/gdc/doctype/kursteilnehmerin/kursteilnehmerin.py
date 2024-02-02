# Copyright (c) 2024, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document


class Kursteilnehmerin(Document):
	pass

@frappe.whitelist()
def kurs_erstellen(doc: str):
	doc_dict = json.loads(doc)
	kurs = frappe.new_doc('Kurs')
	kurs.kurstitel = doc_dict['k_id']
	tn = doc_dict['tn_list']
	tn_list = tn.split('\n')
	print(doc_dict['k_id'])
	for k_tn in tn_list:
		try:
			doc = frappe.get_doc('Teilnehmerin', k_tn)
			kurs.append("k_tn", {
				"tn": k_tn,
			})
		except:
			pass
	kurs.insert()
	frappe.msgprint(
        title = 'Bestätigung',
        msg = 'Kurs wurde erstellt')

