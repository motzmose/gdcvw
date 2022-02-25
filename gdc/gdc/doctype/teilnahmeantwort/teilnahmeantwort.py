# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Teilnahmeantwort(Document):
	def get_context(context):
		query_params = frappe.request.environ.get('QUERY_STRING')
		print(query_params)
	pass
