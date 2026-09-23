import frappe


@frappe.whitelist()
def complete_trip(trip_name:str):
    trip = frappe.get_doc("Trip", trip_name)

    if trip.status == "Completed":
        frappe.throw("Trip is already completed.")

    if trip.status == "Cancelled":
        frappe.throw("Cancelled trip cannot be completed.")

    trip.status = "Completed"
    trip.save()

    vehicle = frappe.get_doc("Vehicle", trip.vehicle)
    vehicle.status = "Available"
    vehicle.save()

    driver = frappe.get_doc("Driver", trip.driver)
    driver.status = "Available"
    driver.save()

    return trip.name