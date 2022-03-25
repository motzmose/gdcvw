// Copyright (c) 2022, didaktik-aktuell e.V. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Kurseinladung', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on("Kurseinladung", "loadtn", function(frm) {
	if(frm.doc.kurse){
		const future_tn = frappe.call({
			method: "gdc.gdc.doctype.kurseinladung.kurseinladung.loadtn",
			freeze: true,
			args: {
				args: {
					"kurs": frm.doc.kurse
				}
			}
		}).then(r => {
			for (let tn in r.message){
				console.log(r.message[tn])
				console.log(tn)
				let row = frm.add_child('teilnehmerinnen',{teilnehmerin: r.message[tn]});
			}
			frm.refresh_field('teilnehmerinnen');
		});
		
		//console.log(future_tn)
		//frm.refresh_field('teilnehmerinnen');
		//console.log(frm.doc.teilnehmerinnen)
	};
});
