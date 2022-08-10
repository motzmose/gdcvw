# Copyright (c) 2022, didaktik-aktuell e.V. and contributors
# For license information, please see license.txt

import requests
import frappe
from unidecode import unidecode
from frappe.model.document import Document

class TNStammdaten(Document):
	def before_save(self):
		self.email = f'{self.username}@gdc-bw.de'
		plz = self.plz
		try: 
			doc = frappe.get_doc('PLZWR', plz)
			self.wirtschaftsregion = doc.wirtschaftsregion
			self.wr = doc.kuerzel
			self.email = f'{self.username}@gdc-bw.de'
		except:
			self.wirtschaftregion = "ERROR"
			self.wr = "ERR"
			self.email = f'{self.username}@gdc-bw.de'
	
	def before_naming(self):
		num_retries = 100
		nickname = f'{self.vorname.lower().replace(" ", "")}_{self.nachname.lower().replace(" ", "")}'
		nickname = unidecode(nickname)
		if not self.username:
			for attempt_no in range(num_retries):
				nickname_temp = nickname
				if frappe.db.exists('Teilnehmerin', nickname_temp):
					nickname_temp = f'{self.vorname.lower().replace(" ", "")}_{self.nachname.lower().replace(" ", "")}'+str(attempt_no)
				else:
					self.username = nickname_temp
					break
		else:
			pass

	def after_insert(self):
		tn = frappe.new_doc('Teilnehmerin')
		if self.angelegt == True:
			pass
		else:
			tn.username = self.username
			tn.vorname = self.vorname
			tn.nachname = self.nachname
			tn.email= self.email
			tn.schulform = self.schulform
			tn.insert()
			settings = frappe.get_doc('GDC Settings')
			# API Request to Mailcow creating a new Mailbox
			mc_values = {"local_part": self.username,
						"domain": "gdc-bw.de",
						"name": f"{self.vorname} {self.nachname}",
						"quota": "100",
						"password": settings.mcstdpw,
						"password2": settings.mcstdpw,
						"active": "1",
						"force_pw_update": "0",
						"tls_enforce_in": "0",
						"tls_enforce_out": "0"}
			mc_headers = {'Content-Type': 'application/json',
						'X-API-Key': settings.mcapi}
			mc_request = requests.post(
						f'https://{settings.mcdomain}/api/v1/add/mailbox',
						json=mc_values,
						headers=mc_headers)
			# API Request to Moodle creating a new Account
			mdl_params = {"wstoken": settings.mdl_api_key,
						"moodlewsrestformat": 'json',
						"wsfunction": 'core_user_create_users',
						"users[0][password]": settings.mdl_std_pwd,
						"users[0][username]": self.username,
						"users[0][firstname]": self.vorname,
						"users[0][lastname]": self.nachname,
						"users[0][email]": self.email,
						"users[0][city]": self.stadt,
							"users[0][customfields][0][type]":"name_eltern",
							"users[0][customfields][0][value]":f'{self.eltern_vorname} {self.eltern_nachname}',

							"users[0][customfields][1][type]":"mail_eltern",
							"users[0][customfields][1][value]":self.eltern_email,

							"users[0][customfields][2][type]":"plz",
							"users[0][customfields][2][value]":self.plz,

							"users[0][customfields][3][type]":"schulform",
							"users[0][customfields][3][value]":self.schulform,

							"users[0][customfields][4][type]":"schule",
							"users[0][customfields][4][value]":self.schule,

							"users[0][customfields][5][type]":"region",
							"users[0][customfields][5][value]":self.wirtschaftsregion,

							"users[0][customfields][6][type]":"schulform",
							"users[0][customfields][6][value]":self.schulform,

							"users[0][customfields][7][type]":"klassenstufe",
							"users[0][customfields][7][value]":self.klasse,
						}
			mdl_request = requests.post(f'https://{settings.mdl_domain}/webservice/rest/server.php', mdl_params)
