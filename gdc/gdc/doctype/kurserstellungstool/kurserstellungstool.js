// Copyright (c) 2022, didaktik-aktuell e.V. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Kurserstellungstool', {
	// refresh: function(frm) {

	// }
	refresh: function(frm) {
		frm.disable_save();
	},
});

frappe.ui.form.on("Kurserstellungstool", "erstellen", function(frm) {
	if(frm.doc.kursprogramm && frm.doc.termine){
		frappe.call({
			method: "gdc.gdc.doctype.kurserstellungstool.kurserstellungstool.insert",
			freeze: true,
			args: {
				args: {
					"kursprogramm": frm.doc.kursprogramm,
					"termine": frm.doc.termine
				}
			}
		})
	}
	frappe.msgprint(__('Kurs wurde erstellt.'));
});
