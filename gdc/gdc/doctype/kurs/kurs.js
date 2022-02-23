// Copyright (c) 2022, didaktik-aktuell e.V. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Kurs', {
    gruppe: function (frm) {
        if (frm.doc.gruppe) {
            frm.clear_table('teilnehmerinnen');
            frappe.model.with_doc('Gruppe', frm.doc.gruppe, function () {
                let source_doc = frappe.model.get_doc('Gruppe', frm.doc.gruppe);
                $.each(source_doc.teilnehmerinnen, function (index, source_row) {
                    frm.add_child('teilnehmerinnen').teilnehmerin = source_row.teilnehmerin;
					frm.add_child('teilnehmerinnen').tn_name = source_row.tn_name; // this table has only one column. You might want to fill more columns.
                    frm.refresh_field('teilnehmerinnen');
                });
            });
        }
    },
});