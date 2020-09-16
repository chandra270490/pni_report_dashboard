import frappe
from frappe.utils import date_diff, add_months, today, getdate, add_days

@frappe.whitelist()
def get_carton():
	_date = add_days(today(), -1)
	sql  = frappe.db.sql("""
		select sum(sed.qty)  
			from `tabStock Entry Detail` as sed, `tabStock Entry` as se
		where sed.docstatus=1 and sed.item_group="paper reel" and se.posting_date="{0}" and sed.parent = se.name
	""".format(_date))
	data = 0
	if sql[0] and sql[0][0]:
		data = sql[0][0]
	return data

@frappe.whitelist()
def get_ldpe():
	_date = add_days(today(), -1)
	sql  = frappe.db.sql("""
		select sum(sed.qty)  
			from `tabStock Entry Detail` as sed, `tabStock Entry` as se
		where sed.docstatus=1 and sed.item_code="LDP LA 17"
		and se.posting_date="{0}" and sed.parent = se.name
	""".format(_date))
	data = 0
	if sql[0] and sql[0][0]:
		data = sql[0][0]
	return data