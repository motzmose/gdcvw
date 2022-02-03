# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Teilnehmerin(Document):
	def before_save(self):
		self.username = f'{self.vorname.lower()}_{self.nachname.lower()}'
