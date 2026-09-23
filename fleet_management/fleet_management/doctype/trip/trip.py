# Copyright (c) 2026, Aditya Verma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Trip(Document):

    def validate(self):
        if not self.is_new():
        	return
        vehicle = frappe.get_doc("Vehicle", self.vehicle)
        driver = frappe.get_doc("Driver", self.driver)

        if vehicle.status != "Available":
            frappe.throw("Selected vehicle is not available.")

        if driver.status != "Available":
            frappe.throw("Selected driver is not available.")

        # Prevent the vehicle from being assigned to another active trip
        existing_vehicle_trip = frappe.db.get_list(
            "Trip",
            filters={
                "vehicle": self.vehicle,
                "status": ["in", ["Assigned", "In Progress"]],
                "name": ["!=", self.name]
            },
            fields=["name"],
            limit=1
        )

        if existing_vehicle_trip:
            frappe.throw("Selected vehicle is already assigned to an active trip.")

        # Prevent the driver from being assigned to another active trip
        existing_driver_trip = frappe.db.get_list(
            "Trip",
            filters={
                "driver": self.driver,
                "status": ["in", ["Assigned", "In Progress"]],
                "name": ["!=", self.name]
            },
            fields=["name"],
            limit=1
        )

        if existing_driver_trip:
            frappe.throw("Selected driver is already assigned to an active trip.")

    def after_insert(self):
        vehicle = frappe.get_doc("Vehicle", self.vehicle)
        vehicle.status = "Busy"
        vehicle.save()

        driver = frappe.get_doc("Driver", self.driver)
        driver.status = "Busy"
        driver.save()

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