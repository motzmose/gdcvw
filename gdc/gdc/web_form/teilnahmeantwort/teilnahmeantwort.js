frappe.ready(function() {
	frappe.web_form.after_load = () => {
		
		// frappe.call({
		// 	method: "gdc.gdc.doctype.teilnehmerin.teilnehmerin.getname",
		// 	args: {
		// 		'teilnehmerin':frappe.web_form.get_value('teilnehmerin')
		// 	},
		// 	callback: function(r) {
		// 		frappe.web_form.set_value('tn_vorname',r.message[0])
		// 		frappe.web_form.set_value('tn_nachname',r.message[1])
		// 	}
		// })
	}
	// bind events here
})