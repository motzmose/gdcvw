# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AGTermin(Document):
	pass

@frappe.whitelist()
def get_termine():
	termine = []
	sTermine = frappe.get_list('AG Termin',
	fields=['parent','termin','ende','kursprogramm'])
	for d in sTermine:
		terminData = {
			'termin': d.termin,
			'ende': d.ende,
			'kursprogramm': f'{d.parent} - {d.kursprogramm}',
			'id': d.parent,
			'name': d.parent
		}
		termine.append(terminData)
	return termine