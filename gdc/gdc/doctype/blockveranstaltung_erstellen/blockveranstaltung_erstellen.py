# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class Blockveranstaltungerstellen(Document):
	pass

@frappe.whitelist()
def insert(args):
	args = json.loads(args)
	ag = frappe.new_doc("Blockveranstaltung")
	date = args["erster_termin"]
	while frappe.utils.getdate(args["letzter_termin"]) > frappe.utils.getdate(date):
		ag.append("termine",{
			"termin" : date,
			"ende" : frappe.utils.add_to_date(date, minutes=int(args["dauer"]))
		})
		if args["wiederholung"]=="Wöchentlich":
			date = frappe.utils.add_to_date(date, weeks=1)
		elif args["wiederholung"]=="Täglich":
			date = frappe.utils.add_to_date(date, days=1)
			if frappe.utils.getdate(date).weekday() > 4 and not args["wochenende"]:
				date = frappe.utils.add_to_date(date, days=2)
			else:
				pass
	try: ag.tutor = args["tutorin"]
	except: ag.tutor = ""
	ag.insert()
