# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Kurstermin(Document):
	def autoname(self):
		self.name = f'{self.ag} - {frappe.utils.getdate(self.termin).isoformat()}'
	def before_save(self):
		self.ag = self.parent
	pass

@frappe.whitelist()
def get_termine():
	termine = []
	sTermine = frappe.get_list('Kurstermin',
	fields=['parent','termin','ende','kursprogramm'])
	for d in sTermine:
		terminData = {
			'termin': d.termin,
			'ende': d.ende,
			'kursprogramm': f'{d.parent} - {d.kursprogramm}',
			'id': d.parent,
			'name': d.name
		}
		termine.append(terminData)
	return termine