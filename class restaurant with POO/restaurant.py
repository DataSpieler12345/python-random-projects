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
class restaurant:
    def __init__(self):
        self.menu = {}
        self.mesas = []
        self.mesas_reservadas = {}
        self.ordenes = {}
    #. Add items to the menu
    def add_item(self, item, precio):
        self.menu[item] = precio
    #. reserve tables
    def reserva_mesas(self, numero, nombre_cliente):
        if numero not in self.mesas_reservadas:
            self.mesas_reservadas[numero] = nombre_cliente
        else:
            print(f"sorry table {numero} is reserved")
    #. take customer orders
    def pedidos(self, numero, item):
        self.ordenes[numero] = item



#. Add items to the menu
restaurante = restaurant()
restaurante.add_item("Hamburger", "3.5")
restaurante.add_item("Completo", 4)
restaurante.reserva_mesas(1, "Ivan")
restaurante.reserva_mesas(2, "Benjamin")
restaurante.reserva_mesas(3, "John")
restaurante.reserva_mesas(4, "Lemon")
restaurante.reserva_mesas(5, "Dirk")
#restaurante.reserva_mesas(5, "Frank")
restaurant.pedidos(1, ["Hamburger", "Completo"])
print(restaurante.ordenes)


