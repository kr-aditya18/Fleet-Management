# Copyright (c) 2026, Aditya Verma and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Vehicle(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		status: DF.Literal["Busy", "Available"]
		vehicle_number: DF.Data
		vehicle_owner: DF.Link
		vehicle_type: DF.Literal["Car", "Truck", "Bike", "Other"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Vehicle"
