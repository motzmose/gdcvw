# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Gruppe(Document):

	pass

@frappe.whitelist()
def printvalues(doc: str):
    frappe.msgprint(
        title = "Print Data",
        msg = doc
    )
    pass