# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import json
from frappe import whitelist
from frappe.model.document import Document

class Dokumentation(Document):
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

@frappe.whitelist()
def get_tn(ag):
    dataset = frappe.get_doc("Veranstaltung", ag).ag_teilnehmerin
    response = []
    for i in dataset:
        tn = frappe.get_doc(i).teilnehmerin
        response.append(tn)
    return response

# Under heavy development
# TODO: Implementierung von Datenhaltung - Kurstermin <-> Veranstaltung <-> Teilnehmerin
@frappe.whitelist()
def set_anwesenheit(termin, anwesenheit):
	janwesenheit = json.loads(anwesenheit)
	print(anwesenheit)
	i = 0
	for entry in janwesenheit:
		tn = frappe.get_doc("Teilnehmerin", entry["tn"])
		tn.append("termin",{
			"termin": termin,
			"anwesend": entry["anwesend"],
			"bemerkung": entry["bemerkung"]
		})
		tn.save()
		i+=1