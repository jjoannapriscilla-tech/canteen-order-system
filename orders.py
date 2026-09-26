order = []


def add_item(name, price, quantity=1):
    """Add a food item to the order."""
    for item in order:
        if item["name"] == name:
            item["quantity"] += quantity
            return

    order.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })


def remove_item(name):
    """Remove a food item from the order."""
    for item in order:
        if item["name"] == name:
            order.remove(item)
            return True

    return False


def view_order():
    """Display the current order."""
    if not order:
        print("Your order is empty.")
        return

    print("\nCurrent Order:")
    for item in order:
        subtotal = item["price"] * item["quantity"]
        print(
            f"{item['name']} x {item['quantity']} "
            f"- ₹{subtotal:.2f}"
        )


def calculate_total():
    """Calculate the total bill."""
    total = 0

    for item in order:
        total += item["price"] * item["quantity"]

    return total