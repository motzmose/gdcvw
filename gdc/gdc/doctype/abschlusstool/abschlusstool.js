// Copyright (c) 2022, didaktik-aktuell e.V. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Abschlusstool', {
	setup: function(frm) {
		console.log("Refreshed");
		frm.set_query('termin', ()=>{
			return {
				filters: [
					["Kurstermin", "ag", "=", frm.ag],
					["Kurstermin", "abgeschlossen", "=", "False"]
				]
			}
		});
	},
	ag: function(frm){
		console.log(frm.ag);
		frm.refresh();
	}
});
