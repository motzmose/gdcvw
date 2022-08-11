# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import locale
from frappe.model.document import Document

class Kurstermin(Document):
	def autoname(self):
		if self.parent:
			self.name = f'{self.parent} - {frappe.utils.getdate(self.termin).isoformat()}'
		else:
			self.name = self.name
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
			'name': d.parent
		}
		termine.append(terminData)
	return termine