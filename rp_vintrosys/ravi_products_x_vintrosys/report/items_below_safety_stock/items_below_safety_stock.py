# Copyright (c) 2025, Vintrosys and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
	data = []
	columns = [
			{
				"label": _("Item Code"),
				"fieldname": "item_code",
				"fieldtype": "Link",
				"options": "Item",
				"width": 150,
			},
			{
				"label": _("Item Name"),
				"fieldname": "item_name",
				"fieldtype": "Data",
				"width": 150,
			},
			{
				"label": _("Stock UOM"),
				"fieldname": "stock_uom",
				"fieldtype": "Data",
				"width": 150,
			},
			{
				"label": _("Warehouse"),
				"fieldname": "warehouse",
				"fieldtype": "Link",
				"options": "Warehouse",
				"width": 200,
			},{
				"label": _("Safety Stock"),
				"fieldname": "safety_stock",
				"fieldtype": "Float",
				"width": 150
			},
			{
				"label": _("Actual Qty"),
				"fieldname": "actual_qty",
				"fieldtype": "Float",
				"width": 150
			}]
	items = frappe.db.sql("""
		SELECT
			bin.item_code,
			bin.warehouse,
			bin.actual_qty,
			bin.stock_uom,
			item.item_name,
			item.safety_stock
		FROM
			`tabBin` bin
		INNER JOIN
			`tabItem` item ON bin.item_code = item.item_code
		WHERE
			item.safety_stock IS NOT NULL and bin.actual_qty Is NOT NULL and bin.warehouse = "Finished Goods - RP"
	""", as_dict=True)

	for row in items:
		if flt(row.safety_stock):
			if flt(row.actual_qty) <= flt(row.safety_stock):
				data.append({
					"item_code": row.item_code,
					"item_name": row.item_name,
					"stock_uom": row.stock_uom,
					"warehouse": row.warehouse,
					"actual_qty": row.actual_qty,
					"safety_stock": row.safety_stock
				})

	return columns, data
