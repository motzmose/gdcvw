# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document


class Kurserstellungstool(Document):
	pass

@frappe.whitelist()
def insert(args):
	print(args)
	args = json.loads(args)
	print(args)
	kuerzel = frappe.get_doc("Kursprogramm", args["kursprogramm"]).kuerzel
	if kuerzel == "DC":
		grp = frappe.new_doc("Gruppe")
		grp.typ = "K"
		grp.insert()
	kurs = frappe.new_doc("Kurs")
	kurs.kursprogramm = args["kursprogramm"]
	kurs.kuerzel = kuerzel
	try:
		grp
	except:
		# TODO: Only every second number get's used for naming
		grp = frappe.new_doc("Gruppe")
		grp.typ = "V"
		grp.insert()
		kurs.gruppe = grp.name
	else:
		kurs.gruppe = grp.name
		kurs.name = f"{kuerzel}-{grp.name}"
	print(args["termine"])
	for kurstermin in args["termine"]:
		kurs.append("kurstermine",{
			"kurstitel": kurs.name,
			"termin": kurstermin["termin"]
		})
	kurs.insert()

