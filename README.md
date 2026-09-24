# Fleet Management App (Frappe)

A Fleet Management POC built with the Frappe Framework as part of a Frappe developer onboarding program.

## What's in this repo

- Owner, Vehicle, Driver, and Trip DocTypes
- Relationships between Owner, Vehicle, Driver, and Trip
- Public registration Web Forms
- Trip validation to prevent duplicate active assignments
- Backend lifecycle logic using `validate()` and `after_insert()`
- Vehicle and Driver availability tracking
- Client Script with a custom **Complete Trip** button
- Custom whitelisted API using `frappe.call()`
- Frappe REST API usage

## Tech Stack

- Frappe Framework
- Python
- JavaScript
- MariaDB
- Redis
- WSL2 / Ubuntu

## DocTypes

### Owner

- Owner Name
- Phone Number
- Email

### Vehicle

- Vehicle Number
- Owner
- Vehicle Type
- Status (`Available` / `Busy`)

### Driver

- Driver Name
- Phone Number
- Email
- Status (`Available` / `Busy`)

### Trip

- Vehicle
- Driver
- Start Location
- Destination
- Trip Date
- Status (`Assigned` / `In Progress` / `Completed` / `Cancelled`)

## Project Flow

    Owner Registration
           |
           v
    Vehicle Registration <----- Driver Registration
           |
           v
       Assign Trip
           |
           v
    Trip = Assigned
    Vehicle = Busy
    Driver = Busy
           |
           v
      Complete Trip
           |
           v
    Trip = Completed
    Vehicle = Available
    Driver = Available

## Backend Logic

### Trip Validation

The `validate()` method checks:

- Selected vehicle is available.
- Selected driver is available.
- Vehicle is not already assigned to another active trip.
- Driver is not already assigned to another active trip.

`frappe.db.get_list()` is used to check for existing active trips.

### Trip Creation

`after_insert()` updates the related records after a Trip is created:

    Vehicle -> Busy
    Driver  -> Busy

## Client Script

A Client Script adds a **Complete Trip** button to an existing active Trip.

The button uses `frappe.call()` to call the server-side Python method.

    Complete Trip button
            |
            v
       frappe.call()
            |
            v
    fleet_management.api.complete_trip
            |
            v
    Trip      -> Completed
    Vehicle   -> Available
    Driver    -> Available

## API

### Fetch Vehicles

Frappe provides REST APIs for DocTypes.

**Endpoint**

    GET /api/resource/Vehicle

**cURL**

    curl http://localhost:8000/api/resource/Vehicle \
      -H "Authorization: token API_KEY:API_SECRET"

**Example Response**

    {
      "data": [
        {
          "name": "UP32AB1234"
        }
      ]
    }

### Complete Trip

Custom whitelisted server-side method:

    POST /api/method/fleet_management.api.complete_trip

**Parameter**

    trip_name=TRIP-00001

The method changes:

    Trip      -> Completed
    Vehicle   -> Available
    Driver    -> Available

## Local Setup

Start the Frappe development server:

    cd ~/frappe-bench
    bench start

Open:

    http://frappe.local:8000

## Repository

https://github.com/kr-aditya18/Fleet-Management

## Demo

The demo covers:

1. Owner registration
2. Driver registration
3. Vehicle registration
4. Trip assignment
5. Vehicle and Driver status changing to `Busy`
6. Active-trip validation
7. Complete Trip button
8. Trip changing to `Completed`
9. Vehicle and Driver changing back to `Available`

## Demo Video

https://youtu.be/uXQrI2vrRcQ