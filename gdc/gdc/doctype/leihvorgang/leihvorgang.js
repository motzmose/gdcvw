// Copyright (c) 2022, didaktik-aktuell e.V. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Leihvorgang', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Leihvorgang', "scan", function(frm){
	new frappe.ui.Scanner({
			dialog: true, // open camera scanner in a dialog
			multiple: false, // stop after scanning one value
			on_scan(data) {
			  frm.doc.items.append(data.decodedText);
			  console.log(data.decodedText);
			  frm.refresh_field('items');
			}
	  });
})