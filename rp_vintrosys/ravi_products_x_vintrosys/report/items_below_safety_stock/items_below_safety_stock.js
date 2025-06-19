// Copyright (c) 2025, Vintrosys and contributors
// For license information, please see license.txt

frappe.query_reports["Items Below Safety Stock"] = {
	"filters": [

	],
	formatter: function(value, row, column, data, default_formatter) {
    value = default_formatter(value, row, column, data);
    console.log(value);

    if (data.actual_qty === 0) {
        value = "⁠<span style='color: red;'>" + value + "</span> ";
    }
    return value;
}
};
