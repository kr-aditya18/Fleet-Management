# Copyright (c) 2026, Aditya Verma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address


class Driver(Document):

    def validate(self):
        if not self.phone_number.isdigit() or len(self.phone_number) != 10:
            frappe.throw("Phone number must contain exactly 10 digits.")

        validate_email_address(self.email, throw=True)

    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        driver_name: DF.Data | None
        email: DF.Data | None
        phone_number: DF.Data | None
        status: DF.Literal["Available", "Busy"]
    # end: auto-generated types

    _DOCTYPE_NAME = "Driver"