// Copyright (c) 2022, didaktik-aktuell e.V. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Abschlusstool', {
	ag: function(frm) {
		frm.refresh
		console.log("Refreshed");
		console.log(frm.doc.beginn)
		frm.set_query('termin', ()=>{
			return {
				filters: [
					["Kurstermin", "ag", "=", frm.doc.ag],
					["Kurstermin", "abgeschlossen", "=", "False"]
				]
			}
		});
		console.log(frm.doc.ag)
	}
});
