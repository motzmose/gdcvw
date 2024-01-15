
import frappe

def execute():
	"""deploy_password_changes"""
	frappe.reload_doc("gdc", "doctype", "teilnehmerin")
	frappe.db.sql("update tabTeilnehmerin set password='pitirikoge' where password is null")
	frappe.db.commit()
