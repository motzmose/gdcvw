
import frappe

def execute():
	"""drop doctypes gruppe and implement kurs"""
	frappe.reload_doc("gdc", "doctype", "kurs")
	frappe.reload_doc("gdc", "doctype", "kurs erstellen")
	frappe.reload_doc("gdc", "doctype", "kursteilnehmerin")
	frappe.reload_doc("gdc", "doctype", "gruppe")