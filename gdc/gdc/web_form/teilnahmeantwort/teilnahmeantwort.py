from __future__ import unicode_literals

import frappe

def get_context(context):
	name = frappe.call('gdc.gdc.doctype.teilnehmerin.teilnehmerin.getname',frappe.request.args['teilnehmerin'])
	context.title = f"Hallo {name[0]} {name[1]}"
