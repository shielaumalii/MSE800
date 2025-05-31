# Car Rental System (CLI Edition)

## Introduction

Welcome to the **Car Rental System**, a user-friendly command-line application created to streamline vehicle rental operations for a car rental business. It simplifies both the customer rental experience and administrative management tasks. Whether you need to book a car or oversee a vehicle inventory, this tool is built to assist both clients and staff.

Developed in Python and supported by an SQLite database, the system manages user sign-up, login, car reservations, and administrative approvals. For added security, it incorporates encrypted password storage using bcrypt, ensuring user credentials are safely handled.

---

## Main Features

### User Types

- **Admins:**  
  Have access to tools for managing the car listings and approving/ declining rental requests.

- **Customers:**  
  Can browse cars, make bookings, and manage their own rentals.

### Login & Security

- New users can create an account and log in through a secure authentication process. All the data will be stored in SQLite database.
- Administrative access is restricted and requires a unique registration code.
- User passwords are safely stored using bcrypt hashing to enhance security.

### Car Inventory Management

- Efficiently add new vehicles to the system, update the existing listings, or remove them as needed.
- Each car entry includes key information such as car ID number, car maker, model, manufacture year, total mileage, daily rental rate, and current availability for booking. All the data will be stored in SQLite database.

### Rental Handling

- Customers can schedule rentals starting from the day after the current date, with the option to book up to one month ahead.
- This advance booking window helps reduce last-minute requests, enabling the company to better coordinate vehicle readiness and availability.
- An optional driver service is offered at an extra charge.
- All rental requests are stored in the SQLite database and require admin approval before confirmation. While pending approval, the car is flagged as pending but remains visible as available to other customers.
- If a booking is denied, the vehicle is automatically returned to the pool of available cars.

### Smart Recommendations

- To enhance the user experience, the system offers personalized vehicle suggestions by reviewing a customer’s rental history, analyzing the most frequent model/maker. Additionally, it highlights the most economical cars available, helping users find budget-friendly options quickly and easily.

### Input Checks

- The system validates all forms and user inputs to make sure every required field is completed accurately and without errors.

---

## Getting Started

### 1. **What You’ll Need**

- Python 3.8 or newer
- Install bcrypt:  
  ```sh
  pip install bcrypt
