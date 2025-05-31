# **Car Rental System**

## **Introduction**
The Car Rental System is a command-line interface (CLI) application that allows users to register, log in, and manage car rentals. It includes features for both administrators and customers, such as adding cars, booking rentals, and managing rental approvals.

---

## **Table of Contents**
1. [Features](#features)
2. [Installation and Configuration](#installation-and-configuration)
3. [How to Operate](#how-to-operate)
4. [File Descriptions](#file-descriptions)
5. [Licensing](#licensing)
6. [Known Issues](#known-issues)
7. [Credits](#credits)

---

## **Features**
- **User Management**: Register and log in as an admin or customer.
- **Car Management**: Add, update, delete, and view cars (admin only).
- **Rental Management**: Book cars, view rentals, and approve/decline rental requests.

---

## **Installation and Configuration**

### **Prerequisites**
- Python 3.8 or higher
- SQLite3 (pre-installed with Python)


### **Step 1: Clone the Repository**

Clone the project repository to your local machine:
```bash
git clone https://github.com/your-username/car-rental-system.git
cd car-rental-system
```

### **Step 2: Install Dependencies

Install the required Python libraries:
```bash
pip install bcrypt
```

### **Step 3: Set Up the Database
Run the following script to initialize the SQLite database:
```bash
python utils/database_setup.py
```
This will create the necessary tables (users, cars, rentals) in the database.

### **Step 4: Run the Application
Start the application by running:
```bash
python main.py
```

---

## **How to Operate**
1. Main Menu
- Register: Create a new user account (admin or customer).
- Login: Log in to the system using your credentials.
- Exit: Exit the application.
2. Admin Menu
- View Cars: Display all available cars.
- Add Car: Add a new car to the system.
- Update Car: Update details of an existing car.
- Delete Car: Remove a car from the system.
- View Rentals: View all rental requests.
- Approve/Decline Rentals: Manage rental requests.
- Logout: Return to the main menu.
3. Customer Menu
- View Cars: Display all available cars for rent.
- Book Car: Book a car for a specific duration.
- My Booked Cars: View your rental history.
- Logout: Return to the main menu.

---

## File Descriptions

- **main.py**  
  Entry point of the application. Initializes the system and displays the main menu.

- **models/user.py**  
  Handles user registration and login, including password hashing for security.

- **models/car.py**  
  Manages car-related operations such as adding, updating, deleting, and displaying cars.

- **models/rental.py**  
  Handles rental operations: booking, approving, declining, and viewing rentals. Includes validation for rental dates and durations.

- **utils/admin_menu.py**  
  Provides the admin menu interface and handles admin-specific actions.

- **utils/customer_menu.py**  
  Provides the customer menu interface and handles customer-specific actions.

- **utils/menu.py**  
  Displays the main menu and routes users to the appropriate interface (admin or customer).

- **utils/database.py**  
  Utility for connecting to the SQLite database.

- **utils/database_setup.py**  
  Script to initialize the SQLite database and create necessary tables.

---

## Licensing

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software, provided that proper credit is given to the original developer.

---

## Known Issues

- **Limited Error Handling:**  
  Some edge cases (e.g., invalid database states) may not be handled gracefully.

- **No GUI:**  
  The system is CLI-based and does not include a graphical user interface.

- **Concurrency:**  
  The system does not handle concurrent database access, which may cause issues in multi-user environments.

---

## Credits

**Developer:** Shiela Marie L. Umali  
**GitHub:** (https://github.com/shielaumalii)

---
