# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class Kurseinladung(Document):
	pass

@frappe.whitelist()
def loadtn(args):
	future_tn = []
	args_dict = json.loads(args)
	kuerzel = frappe.get_doc("Kurs",args_dict["kurs"][0]["kurs"]).kuerzel
	teilnehmerinnen = frappe.db.get_list("Teilnehmerin", pluck="name")
	for teilnehmerin in teilnehmerinnen:
		tn_doc = frappe.get_doc("Teilnehmerin", teilnehmerin)
		future_tn.append(tn_doc.name)
		for tag in tn_doc.get_tags():
			if tag == kuerzel:
				future_tn.pop(-1)
				print(f"Popped {tn_doc.name}")
	print(future_tn)
	return future_tn<