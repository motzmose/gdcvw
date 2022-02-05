# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Teilnehmerin(Document):
	def before_save(self):
		plz = self.plz
		doc = frappe.get_doc('PLZWR', plz)
		self.wirtschaftsregion = doc.wirtschaftsregion
	def before_naming(self):
		num_retries = 100
		nickname = f'{self.vorname.lower()}_{self.nachname.lower()}'
		for attempt_no in range(num_retries):
			if frappe.db.exists('Teilnehmerin', nickname):
				nickname=f'{self.vorname.lower()}_{self.nachname.lower()}'+str(attempt_no)
			else:
				self.username = nickname
				break

