from langchain.text_splitter import PythonCodeTextSplitter

# Your Python source code as a string
text = """import datetime

# --- Function Example ---
# A simple standalone function that performs a specific task.
def greet_user(name):
    \"\"\"
    Greets a user by name.

    Args:
        name (str): The name of the user to greet.
    \"\"\"
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        time_of_day = "Good morning"
    elif 12 <= current_hour < 18:
        time_of_day = "Good afternoon"
    else:
        time_of_day = "Good evening"

    print(f"{time_of_day}, {name}!")

# --- Class Example ---
# A class is a blueprint for creating objects (instances).
# It bundles data (attributes) and methods (functions) that operate on that data.
class Product:
    \"\"\"
    Represents a product with a name, price, and quantity.
    \"\"\"
    # Class attribute (shared by all instances of the class)
    currency = "BDT"  # Assuming local currency is Bangladeshi Taka

    # Constructor method: called automatically when a new object is created.
    def __init__(self, name, price, quantity):
        \"\"\"
        Initializes a new Product object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
        \"\"\"
        self.name = name
        self.price = price
        self.quantity = quantity

    # Instance method: operates on the data of a specific object.
    def get_total_value(self):
        \"\"\"
        Calculates the total value of the product based on price and quantity.

        Returns:
            float: The total value of the product.
        \"\"\"
        return self.price * self.quantity

    # Instance method to update quantity
    def update_quantity(self, change):
        \"\"\"
        Updates the quantity of the product.

        Args:
            change (int): The amount to change the quantity by (can be positive or negative).
        \"\"\"
        if self.quantity + change >= 0:
            self.quantity += change
            print(f"Quantity of {self.name} updated to {self.quantity}.")
        else:
            print(f"Error: Not enough {self.name} in stock to reduce by {abs(change)}.")

    # Another instance method to display product info
    def display_info(self):
        \"\"\"
        Prints the product's name, price, and current quantity.
        \"\"\"
        print(f"Product: {self.name}")
        print(f"Price: {self.price:.2f} {Product.currency}")
        print(f"Quantity in stock: {self.quantity}")
        print(f"Total current value: {self.get_total_value():.2f} {Product.currency}")
        print("-" * 30)


# --- Using the Code ---

# 1. Calling the standalone function
print("--- Function Call ---")
greet_user("Alice")
greet_user("Bob")
print("\\n")

# 2. Creating objects (instances) of the Product class
print("--- Class Instances ---")
laptop = Product("Laptop", 1200.50, 5)
keyboard = Product("Mechanical Keyboard", 85.00, 10)
mouse = Product("Wireless Mouse", 25.99, 20)

# 3. Accessing attributes and calling methods on objects
print(f"Initial quantity of {laptop.name}: {laptop.quantity}")
laptop.display_info()
keyboard.display_info()
mouse.display_info()

# Update product quantity using a method
print("--- Updating Quantity ---")
laptop.update_quantity(-2)
laptop.display_info()

laptop.update_quantity(1)
laptop.display_info()

laptop.update_quantity(-10)
laptop.display_info()

print("\\n")

# Demonstrate another product's total value
print("--- Total Value ---")
print(f"Total value of all keyboards: {keyboard.get_total_value():.2f} {Product.currency}")
print("\\n")

# Accessing a class attribute directly from the class
print(f"All products use the currency: {Product.currency}")
print(f"Mouse currency (via instance): {mouse.currency}")
"""

# Use PythonCodeTextSplitter to split the code while preserving structure
splitter = PythonCodeTextSplitter(chunk_size=800, chunk_overlap=100)

chunks = splitter.split_text(text)

# Output the chunks
print(f"Total chunks: {len(chunks)}\n")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n{'=' * 50}\n")
