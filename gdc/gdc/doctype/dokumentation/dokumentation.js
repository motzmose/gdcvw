// Copyright (c) 2022, didaktik-aktuell e.V. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Dokumentation', {
	refresh: function(frm) {
		frm.disable_save();
		frm.add_custom_button('Absenden', () => {
			frappe.call({
				method: 'gdc.gdc.doctype.dokumentation.dokumentation.set_anwesenheit',
				freeze: true,
				args: {
					termin: frm.doc.termin,
					anwesenheit: frm.doc.anwesenheit
				}
			});
			frm.reload_doc();
		})
	},
	ag: function(frm) {
		//frm.refresh
		//console.log("Refreshed");
		//console.log(frm.doc.beginn)
		frm.set_query('termin', ()=>{
			return {
				filters: [
					["Kurstermin", "ag", "=", frm.doc.ag],
					["Kurstermin", "abgeschlossen", "=", "False"]
				]
			}
		});
		frappe.call({
			method: "gdc.gdc.doctype.dokumentation.dokumentation.get_tn",
			freeze: true,
			args: {
				"ag" : frm.doc.ag
			},
			callback: function(r){
				for (let i = 0; i < r.message.length; i++){
					frm.add_child('anwesenheit', {
						tn: r.message[i],
						anwesend: true,
						bemerkung: "",
					})
					console.log(r.message[i])
				}
				frm.refresh_field('anwesenheit');
				console.log("Refreshed Anwesenheit");
			}
		});
	}
});
