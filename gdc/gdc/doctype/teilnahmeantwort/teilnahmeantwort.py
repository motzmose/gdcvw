# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

no_cache = True
class Teilnahmeantwort(Document):
	pass

@frappe.whitelist(allow_guest=True)
def caughtme():
	print("You caught me!")