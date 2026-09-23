# Copyright (c) 2026, Aditya Verma and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Trip(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		destination: DF.Data
		driver: DF.Link
		start_location: DF.Data
		status: DF.Literal["Assigned", "In Progress", "Completed", "Cancelled"]
		trip_date: DF.Data
		vehicle: DF.Link
	# end: auto-generated types

	_DOCTYPE_NAME = "Trip"
