# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
from frappe import whitelist
from frappe.model.document import Document

class Abschlusstool(Document):
	pass

@frappe.whitelist()
def query(ag):
	response = frappe.get_list('AG Termin',
		filters={
			'ag': ag,
			'abgeschlossen': False
		},
		pluck='name',
		order_by='termin desc')
	return response
