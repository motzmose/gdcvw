frappe.views.calendar['AG'] = {
    field_map: {
        start: 'termin',
        end: 'ende',
        id: 'id',
        title: 'kursprogramm',
        subject: 'kursprogramm',
        allDay: 'allDay',
        name: 'name'
    },
    gantt: false,
    get_events_method: "gdc.gdc.doctype.ag_termin.ag_termin.get_termine"
}