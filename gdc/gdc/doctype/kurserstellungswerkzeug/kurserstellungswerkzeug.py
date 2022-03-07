# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class Kurserstellungswerkzeug(Document):
	def after_insert(self):
		kuerzel = frappe.get_doc("Kursprogramm", self.kursprogramm).kuerzel
		if kuerzel == "DC":
			grp = frappe.new_doc("Gruppe")
			grp.typ = "K"
			grp.insert()
		kurs = frappe.new_doc("Kurs")
		kurs.kursprogramm = self.kursprogramm
		kurs.kuerzel = kuerzel
		try:
			grp
		except:
			# TODO: Only every second number get's used for naming
			grp = frappe.new_doc("Gruppe")
			grp.typ = "V"
			grp.insert()
			kurs.gruppe = grp.name
		else:
			kurs.gruppe = grp.name
			kurs.name = f"{kuerzel}-{grp.name}"
		print(self.termine)
		for kurstermin in self.termine:
			termin = frappe.get_doc("Kurserstellungstermin",kurstermin.name)
			kurs.append("kurstermine",{
				"kurstitel": kurs.name,
				"termin": termin.termin
			})
		kurs.insert()

@frappe.whitelist()
def printvalues(doc: str):
	doc_dict = json.loads(doc)
	print(doc_dict)
	kp = frappe.get_doc("Kursprogramm", doc_dict['kursprogramm'])
	frappe.msgprint(
        title = "Print Data",
        msg = kp.kuerzel
		)