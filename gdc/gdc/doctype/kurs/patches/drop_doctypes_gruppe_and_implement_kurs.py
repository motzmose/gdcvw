
import frappe

def execute():
	"""drop doctypes gruppe and implement kurs"""
	frappe.reload_doc("gdc", "doctype", "kurs")
	frappe.reload_doc("gdc", "doctype", "kurs_erstellen")
	frappe.reload_doc("gdc", "doctype", "kursteilnehmerin")