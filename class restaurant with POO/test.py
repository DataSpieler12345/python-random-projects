# Write a python class called restaurant

# perform the following tasks now:

    #. Add items to the menu
    #. reserve tables
    #. Take customer orders.
    #. Print menu .
    #. Prints table reservations .
    #. Print customer orders .


# assumptions:

    #1. items have name price: {"hamburger":3.5}
    #2. tables will be numbered, they will have a name of the person who has booked the table status (if it is booked or not)
    #3. the orders will have the name of the customer and the desired items

# Write a python class called restaurant

class Restaurant:
    def __init__(self):
        self.menu = {}
        self.tables = {}
        self.reservations = {}
        self.orders = {}

    # Add items to the menu
    def add_item(self, item, price):
        self.menu[item] = price

    # Reserve tables
    def reserve_table(self, table_number, customer_name):
        if table_number not in self.reservations:
            self.reservations[table_number] = customer_name
        else:
            print(f"Sorry, table {table_number} is already reserved.")

    # Take customer orders
    def take_order(self, table_number, items):
        self.orders[table_number] = items

    # Print menu
    def print_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    # Print table reservations
    def print_reservations(self):
        print("Table Reservations:")
        for table, customer in self.reservations.items():
            print(f"Table {table}: Reserved for {customer}")

    # Print customer orders
    def print_orders(self):
        print("Customer Orders:")
        for table, items in self.orders.items():
            print(f"Table {table}: {', '.join(items)}")

# Create an instance of the Restaurant class
restaurant = Restaurant()

# Add items to the menu
restaurant.add_item("Hamburger", 3.5)
restaurant.add_item("Completo", 4)

# Reserve tables
restaurant.reserve_table(1, "Ivan")
restaurant.reserve_table(2, "Benjamin")
restaurant.reserve_table(3, "John")
restaurant.reserve_table(4, "Lemon")
restaurant.reserve_table(5, "Dirk")

# Take customer orders
restaurant.take_order(1, ["Hamburger", "Completo"])

# Print orders
restaurant.print_orders()