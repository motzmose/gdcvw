# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Gruppenteilnehmerin(Document):
	# Funktioniert noch nicht
	def before_naming(self):
		parent_doc = self.get_parent()
		for termin in termine.parent_doc:
			print(termin)
	pass
