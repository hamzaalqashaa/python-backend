def analyze_cart(inventory: dict, cart: list):
    total = 0
    categories = set()
    most_expensive_item = ""
    highest_price = 0

    print("🧾 Receipt".center(40, "-"))
    for item in cart:
        if (info := inventory.get(item)):
            price = info["price"]
            category = info["category"]
            categories.add(category)
            total += price

            # Check if this is the most expensive item
            if price > highest_price:
                most_expensive_item = item
                highest_price = price

            # Print formatted line
            print(f"{item.title():<15} ${price:.2f}  ({category})")
        else:
            print(f"{item.title():<15} Not found in inventory")

    print("-" * 40)
    print(f"Total:            ${total:.2f}")
    print(f"Unique categories: {categories}")
    print(f"Most expensive:   {most_expensive_item.title()} (${highest_price:.2f})")


if __name__ == "__main__":
    inventory = {
        "apple": {"price": 1.5, "category": "fruit"},
        "banana": {"price": 0.75, "category": "fruit"},
        "milk": {"price": 2.99, "category": "dairy"},
        "bread": {"price": 3.25, "category": "bakery"},
        "cheese": {"price": 4.5, "category": "dairy"},
        "chocolate": {"price": 2.25, "category": "snacks"}
    }

    cart = ["apple", "banana", "milk", "cheese", "chocolate"]
    analyze_cart(inventory, cart)
