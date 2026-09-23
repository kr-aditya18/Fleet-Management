# Copyright (c) 2026, Aditya Verma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address


class Owner(Document):

    def validate(self):
        if not self.phone_number.isdigit() or len(self.phone_number) != 10:
            frappe.throw("Phone number must contain exactly 10 digits.")

        validate_email_address(self.email, throw=True)

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        email: DF.Data
        owner_name: DF.Data
        phone_number: DF.Data

    # end: auto-generated types

    _DOCTYPE_NAME = "Owner"