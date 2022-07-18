# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import frappe
import json
import datetime
from frappe.model.document import Document

class AGerstellen(Document):
	pass

@frappe.whitelist()
def insert(args):
	args = json.loads(args)
	begin = args["erster_termin"]
	end = args["letzter_termin"]
	dauer = args["dauer"]
	repeat = args["wiederholung"]
	ag = frappe.new_doc("AG")
	date = begin
	while frappe.utils.getdate(end) > frappe.utils.getdate(date):
		ag.append("termine",{
			"termin" : date,
			"ende" : frappe.utils.add_to_date(date, minutes=dauer)
		})
		if repeat=="Wöchentlich":
			date = frappe.utils.add_to_date(date, weeks=1)
		elif repeat=="Täglich":
			date = frappe.utils.add_to_date(date, days=1)
			if frappe.utils.getdate(date).weekday() > 4 and not args["wochenende"]:
				date = frappe.utils.add_to_date(date, days=2)
			else:
				pass
	try: ag.tutor = args["tutorin"]
	except: ag.tutor = ""
	ag.insert()
