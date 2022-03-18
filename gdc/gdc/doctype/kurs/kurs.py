# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Kurs(Document):
	def after_insert(self):
		for kurstermin in self.kurstermine:
			kurstermin.ende = frappe.utils.add_to_date(kurstermin.termin, hours=2)
			kurstermin.save()
	pass