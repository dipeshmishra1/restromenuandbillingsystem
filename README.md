
# Restro Menu System

A simple desktop-based **Restaurant Menu and Billing System** developed using **Python and Tkinter**.

The application provides a graphical user interface where users can select food and beverage items, add them to their current order, view the total bill, and clear the order.

## Features

* Simple and user-friendly graphical interface
* Displays available restaurant menu items with prices
* Add multiple items to the current order
* Automatically calculates the total bill
* Displays selected items in the order list
* Clear the complete order with one button
* Fixed-size desktop application window
* No external database required

## Menu

The application currently contains the following items:

| Item       |   Price |
| ---------- | ------: |
| Pizza      | Rs. 500 |
| Boiled Egg |  Rs. 25 |
| Momo       | Rs. 150 |
| Pasta      | Rs. 100 |
| Coffee     | Rs. 150 |
| Coke       | Rs. 200 |

The menu and prices are defined directly inside the Python program.

## Technologies Used

* **Programming Language:** Python
* **GUI Library:** Tkinter
* **Interface:** Desktop GUI
* **Database:** Not required

Tkinter is used to create the application window, buttons, labels, frames, and order list.

## Requirements

Before running the application, make sure Python is installed on your computer.

Check Python installation:

```bash
python --version
```

Tkinter is normally included with standard Python installations.

## Project Structure

```text
Restro-Menu-System/
│
├── restromenu.py
└── README.md
```

## How to Run

### 1. Download or clone the project

Place `restromenu.py` in a folder.

### 2. Open the terminal

Navigate to the project folder:

```bash
cd path/to/Restro-Menu-System
```

### 3. Run the program

```bash
python restromenu.py
```

The restaurant menu window will open.

## How to Use

### Step 1: Select an Item

Click any item from the **Select Items** section.

For example:

```text
Pizza — Rs. 500
Momo — Rs. 150
Coffee — Rs. 150
```

### Step 2: Add Items to Order

Every time an item is clicked, it is added to the current order and its price is added to the total bill.

Example:

```text
Pizza (Rs. 500)
Momo (Rs. 150)
Coffee (Rs. 150)

Total Bill: Rs. 800
```

### Step 3: Clear the Order

Click **Clear Order** to remove all selected items and reset the total bill to:

```text
Total Bill: Rs. 0
```

The reset operation clears both the order list and the stored total.

## Application Structure

The application uses a class called `HotelMenu`.

```python
class HotelMenu:
```

The main components are:

### `__init__()`

Initializes the application window, menu, total bill, and user interface.

### `setup_ui()`

Creates the graphical interface, including:

* Application title
* Menu section
* Menu buttons
* Current order section
* Order list
* Total bill
* Clear Order button

### `add_item_to_order()`

Adds the selected menu item to the order and updates the total bill.

### `reset_order()`

Removes all items from the current order and resets the bill to zero.

## User Interface

The application contains two main sections:

```text
+---------------------------------------------------+
|             Welcome to Dipesh Restro              |
+-------------------------+-------------------------+
|      Select Items       |    Your Current Order   |
|                         |                         |
| Pizza — Rs. 500         | Pizza (Rs. 500)        |
| Boiled Egg — Rs. 25     | Momo (Rs. 150)         |
| Momo — Rs. 150          |                         |
| Pasta — Rs. 100         | Total Bill: Rs. 650   |
| Coffee — Rs. 150        |                         |
| Coke — Rs. 200          | [   Clear Order   ]   |
+-------------------------+-------------------------+
```

## Calculation

The total bill is calculated by adding the price of every selected item.

For example:

```text
Pizza = Rs. 500
Momo  = Rs. 150
Coke  = Rs. 200
----------------
Total = Rs. 850
```

The program maintains the total using:

```python
self.order_total
```

## Limitations

The current version is a basic restaurant ordering system and does not include:

* Customer information
* Quantity controls
* Receipt printing
* Database storage
* Login system
* Online payment
* Tax/service charge calculation
* Order history
* Stock/inventory management

## Future Improvements

Possible improvements include:

1. Add quantity selection.
2. Add customer name and contact information.
3. Add automatic receipt generation.
4. Add tax and service charges.
5. Add database support using SQLite or MySQL.
6. Add an admin panel for managing menu items.
7. Add order history.
8. Add payment options.
9. Add food images.
10. Improve the GUI design.
11. Add search/filter functionality.
12. Add table number/order number management.

## Author

**Dipesh Mishra**

## License

This project is created for educational and learning purposes.
