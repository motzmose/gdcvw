// Copyright (c) 2022, didaktik-aktuell e.V. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Blockveranstaltung erstellen', {
	refresh: function(frm) {
		frm.disable_save();
		frm.set_value('dauer', 90);
		frm.set_value('wiederholung', "Täglich")
	}
});

frappe.ui.form.on("Blockveranstaltung erstellen", "create", function(frm) {
	if(frm.doc.erster_termin && frm.doc.letzter_termin){
		frappe.call({
			method: "gdc.gdc.doctype.blockveranstaltung_erstellen.blockveranstaltung_erstellen.insert",
			freeze: true,
			args: {
				args: {
					"erster_termin": frm.doc.erster_termin,
					"letzter_termin": frm.doc.letzter_termin,
					"dauer": frm.doc.dauer,
					"wochenende": frm.doc.wochenende,
					"wiederholung": frm.doc.wiederholung,
					"tutorin": frm.doc.tutorin
				}
			}
		})
		frm.set_value({
			"erster_termin": null,
			"letzter_termin": null,
			"dauer": "90",
			"wochenende": null,
			"wiederholung": null,
			"tutorin": null
		})
		frappe.msgprint(__('Blockveranstaltung wurde erstellt.'));
	}
	else {
		frappe.msgprint(__('Blockveranstaltung konnte nicht erstellt werden. Es ist zumindest ein Beginn und Ende erforderlich.'));
	}
});