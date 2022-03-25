from __future__ import unicode_literals

import frappe

def get_context(context):
	name = frappe.call('gdc.gdc.doctype.teilnehmerin.teilnehmerin.getname',frappe.request.args['teilnehmerin'])
	context.title = f"Hallo {name[0]} {name[1]}"

def get_list_context(context):
	context.row_template = "gdc/templates/includes/teilnahmeantwort/teilnahmeantwort_row_template.html"
	context.get_list = get_date_list

def get_date_list(doctype, txt, filters, limit_start, limit_page_length = 20, order_by='modified desc'):
	teilnehmerin = frappe.request.arg['teilnehmerin']
	dates = frappe.db.sql("""select * from `tabPatient Appointment`
		where patient = %s and (status = 'Open' or status = 'Scheduled') order by appointment_date""", patient, as_dict = True)
	return dates