# COMP2090 course project（GRP_23）
## project Overview
This is a Python-based desktop application for managing board orders across different communities and rooms. It provides a graphical interface for maintaining a board library, creating orders, associating boards with quantities, and exporting structured data for further analysis in Task 2.
## Demonstration
[Task1](https://youtu.be/RAFmSs5guhA?si=ZhdDAGnCdyyCo-lg)
[Task2](https://youtu.be/uAZMfByUcjQ?si=HhsLqFDOxm-hQMPo)
## Operating environment requirements：
This project is a Python desktop application. The GUI is based on tkinter (Python's standard GUI interface) and can run without any additional third-party libraries. It comes pre-installed on most Windows/macOS systems or with Python; some Linux distributions may require separate installation. Data storage uses JSON files, and reading and writing depend on the Python standard library json.

## Recommended environment:
* Python 3.9
* Place GUI.py, material_lib.py, and order.py in the same directory 

## Startup method：
### In the directory containing the aforementioned .py files, execute GUI.pyAfter startup, it will automatically load：
* board.json →which is the Board Library data file, read and written by material_lib.py and：
* orders.json →the order data file, read and written by order.py. It contains basic order information, status, creation time, and a list of boards in the order.

## Function Operation Instructions:
### Board Library Management:
#### 1) Enter the following in the input boxes:
   * Brand
   * Board color
   * Board factory
#### 2) Click Add:
   Add the board to the library; the system will check if Brand + Color is duplicated (if duplicated, a Warning will be displayed, and duplicate insertion will not be allowed).
#### 3) Delete:
   Select the item in “Board List” and click Delete to delete the board record.

### Order Management (Corresponding interface: "Order Management")
#### 1)Create an order: 
Enter:
* Community (or project name)
* Roomnumber (or unit number)
Click Creating to create an order (default status is pending).
#### 2) Delete an order: Select the order in the order list and click Delete.
#### 3) Switch order status: Select the order and click Changing Status to switch between pending and completed.
#### 4) View board materials in an order: Select the order and click Show Board. The "Board in This Order" section below will display the board material details (Brand/Color/Factory/Quantity) included in the order.

### Add Board to Order
#### 1) Select an order in the order list; select a board in the board list.
#### 2) Click Add, a quantity input box will pop up, enter Quantity (range limited to 1-1000).
#### 3) Deleting Board from an Order:
   * Select the order → Click Show Board to display the board in the order;
   * Select the board entry to be removed in “Board in This Order”;
   * Click Delete in the “Add Board to Order” area (delete the order detail row).

### Export                 
#### In the “Order Management” area, click Export:
* The system will write the board details from all orders into task1_orders.json; each record contains the fields community, room, brand, color, and quantity, which task 2.html will read and perform Brand+Color 
aggregation.
