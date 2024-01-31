// Copyright (c) 2024, didaktik-aktuell e.V. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Kurs erstellen", {
    refresh(frm) {
        frm.disable_save();
    },
});
