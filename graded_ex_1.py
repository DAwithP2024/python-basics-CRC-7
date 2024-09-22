# Implementing the required functions step by step in graded_ex_1.py

products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    """Sort the products list based on the user's chosen order."""
    if sort_order == 1:
        return sorted(products_list, key=lambda x: x[1])  # ascending
    elif sort_order == 2:
        return sorted(products_list, key=lambda x: x[1], reverse=True)  # descending
    return products_list


def display_products(products_list):
    """Display the products in a numbered list with their prices."""
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")


def display_categories():
    """Display the categories of products in a numbered format."""
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")


def add_to_cart(cart, product, quantity):
    """Add the selected product and quantity to the cart."""
    cart.append((product[0], product[1], quantity))  # append product name, price, and quantity


def display_cart(cart):
    """Display the contents of the cart and the total cost."""
    total_cost = 0
    for product, price, quantity in cart:
        cost = price * quantity
        total_cost += cost
        print(f"{product} - ${price} x {quantity} = ${cost}")
    print(f"Total cost: ${total_cost}")


def generate_receipt(name, email, cart, total_cost, address):
    """Generate and display a receipt for the user."""
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted after successful delivery.")


def validate_name(name):
    """Validate the user's name: must have first and last name, alphabetic only."""
    if len(name.split()) == 2 and all(part.isalpha() for part in name.split()):
        return True
    return False


def validate_email(email):
    """Validate the user's email: must contain '@'."""
    return "@" in email


def main():
    cart = []
    total_cost = 0

    # Get user's name and validate
    while True:
        name = input("Enter your full name: ")
        if validate_name(name):
            break
        print("Invalid name. Please enter a valid full name (first and last name).")

    # Get user's email and validate
    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            break
        print("Invalid email. Please enter a valid email address.")

    # Show product categories
    while True:
        print("Product Categories:")
        display_categories()
        category_choice = input("Enter the number of the category you want to explore: ")

        try:
            category_index = int(category_choice) - 1
            if category_index not in range(len(products)):
                raise ValueError
            category_name = list(products.keys())[category_index]
        except ValueError:
            print("Invalid selection. Please enter a valid number.")
            continue

        # Show products in the chosen category
        product_list = products[category_name]
        while True:
            print(f"Products in {category_name}:")
            display_products(product_list)
            print("-" * 40)
            print("The choices you can make are as follows:" )
            action_choice = input("1. Select a product to buy\n2. Sort products by price\n3. Go back to categories\n4. Finish shopping\nEnter your choice: ")

            if action_choice == "1":
                product_num = int(input("Enter the number of the product to buy: "))
                if 1 <= product_num <= len(product_list):
                    quantity = int(input("Enter the quantity: "))
                    selected_product = product_list[product_num - 1]
                    add_to_cart(cart, selected_product, quantity)
                    total_cost += selected_product[1] * quantity
                else:
                    print("Invalid product number.")

            elif action_choice == "2":
                sort_order = int(input("Enter 1 for ascending or 2 for descending order: "))
                product_list = display_sorted_products(product_list, sort_order)

            elif action_choice == "3":
                break  # Go back to category selection

            elif action_choice == "4":
                if cart:
                    display_cart(cart)
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something next time!")
                return  # Exit the program

            else:
                print("Invalid choice. Please select a valid option.")


# The following block ensures that main() runs when this script is executed.
if __name__ == "__main__":
    main()
