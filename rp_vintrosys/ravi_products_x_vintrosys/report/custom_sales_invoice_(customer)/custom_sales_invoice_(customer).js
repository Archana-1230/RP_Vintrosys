// Copyright (c) 2025, Vintrosys and contributors
// For license information, please see license.txt

frappe.query_reports["Custom Sales invoice (Customer)"] = {
	"filters": [
		{
			"fieldname":"period",
			"label": __("Period"),
			"fieldtype": "Select",
			"options": [
				{ "value": "Monthly", "label": __("Monthly") },
				{ "value": "Quarterly", "label": __("Quarterly") },
				{ "value": "Half-Yearly", "label": __("Half-Yearly") },
				{ "value": "Yearly", "label": __("Yearly") }
			],
			"default": "Monthly"
		},
		{
			"fieldname": "company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"reqd": 1,
			"default": frappe.defaults.get_user_default("Company")
		},
		{
			"fieldname": "fiscal_year",
			"label": __("Fiscal Year"),
			"fieldtype": "Link",
			"options": "Fiscal Year",
			"reqd": 1,
			"default": frappe.defaults.get_user_default("Fiscal Year")
		},
		{
			"fieldname": "value_quantity",
			"label": __("Value Or Qty"),
			"fieldtype": "Select",
			"options": [
				{ "value": "Quantity", "label": __("Quantity (Kg Sold) - with schm") },
				{ "value": "QuantityWschm", "label": __("Quantity (Kg Sold) - without schm") },
			],
			"default": "Quantity",
			"reqd": 1
		},

	]
};
