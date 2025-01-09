class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class StockManagementSystem:
    def __init__(self):
        self.inventory = {}
        self.total_sales = 0.0

    def add_product(self, name, quantity, price):
        self.inventory[name] = Product(name, quantity, price)

    def take_order(self, name, order_quantity):
        product = self.inventory.get(name)
        if product:
            if product.quantity >= order_quantity:
                product.quantity -= order_quantity
                sale_value = order_quantity * product.price
                self.total_sales += sale_value
                print(f"Order placed for {order_quantity} units of {name}. Sale Value: ksh.{sale_value:.2f}")
            else:
                print(f"Insufficient stock for {name}. Available quantity: {product.quantity}")
        else:
            print(f"Product {name} not found.")

    def evaluate_sales(self):
        print(f"Total Sales: ksh.{self.total_sales:.2f}")

    def display_inventory(self):
        print("Current Inventory:")
        for product in self.inventory.values():
            print(f"Product: {product.name}, Quantity: {product.quantity}, Price: ${product.price:.2f}")

def main():
    system = StockManagementSystem()

    # Adding some products to the inventory
    system.add_product("Delmonte", 100, 500)
    system.add_product("Gilbeys", 150, 1800)
    system.add_product("County", 80, 950)

    while True:
        print("\n1. Display Inventory")
        print("2. Take Order")
        print("3. Evaluate Sales")
        print("4. Add Products")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            system.display_inventory()
        elif choice == '2':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity to order: "))
            print("Thank you for shopping with us, Your order will be available shortly!")
            system.take_order(product_name, quantity)
        elif choice == '3':
            system.evaluate_sales()
        elif choice == '4':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity of product added in ml. : "))
            price = int(input("Enter price of product in Ksh  "))
            system.add_product(product_name, quantity, price)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()