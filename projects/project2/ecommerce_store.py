import sqlite3
import os

# ------------------ Database Setup ------------------
DB_NAME = os.path.join(os.path.dirname(__file__), "store.db")

def init_db():
    """Initialize database with tables for products and users."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    # Create Products Table
    cur.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL)''')

    # Create Users Table
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL)''')

    conn.commit()
    conn.close()


# ------------------ OOP Models ------------------
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self._stock = stock   # encapsulated stock

    @property
    def stock(self):
        return self._stock

    def reduce_stock(self, quantity):
        if quantity <= self._stock:
            self._stock -= quantity
        else:
            raise ValueError("Not enough stock available.")

    def __str__(self):
        return f"{self.name} | ${self.price:.2f} | Stock: {self._stock}"


class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"User: {self.username}"


class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.items = {}  # {product_id: quantity}

    def add_product(self, product_id, quantity=1):
        self.items[product_id] = self.items.get(product_id, 0) + quantity

    def view_cart(self):
        return self.items

    def clear_cart(self):
        self.items.clear()

    def calculate_total(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        total = 0
        for pid, qty in self.items.items():
            cur.execute("SELECT price FROM products WHERE id=?", (pid,))
            result = cur.fetchone()
            if result:
                price = result[0]
                total += price * qty
        conn.close()
        return total


# ------------------ Database CRUD Operations ------------------
def add_product_to_db(name, price, stock):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    conn.close()
    return products

def update_product_stock(product_id, new_stock):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE products SET stock=? WHERE id=?", (new_stock, product_id))
    conn.commit()
    conn.close()


# ------------------ Checkout Process ------------------
def checkout(cart: ShoppingCart):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    try:
        for pid, qty in cart.items.items():
            cur.execute("SELECT stock FROM products WHERE id=?", (pid,))
            result = cur.fetchone()
            if result:
                stock = result[0]
                if stock >= qty:
                    new_stock = stock - qty
                    cur.execute("UPDATE products SET stock=? WHERE id=?", (new_stock, pid))
                else:
                    raise ValueError(f"Not enough stock for product ID {pid}.")
        conn.commit()
        total = cart.calculate_total()
        cart.clear_cart()
        print(f"✅ Checkout successful! Total: ${total:.2f}")
    except Exception as e:
        print("❌ Checkout failed:", e)
    finally:
        conn.close()


# ------------------ Demo ------------------
if __name__ == "__main__":
    init_db()

    # Add some demo products
    if not get_all_products():
        add_product_to_db("Laptop", 1200.00, 5)
        add_product_to_db("Phone", 800.00, 10)
        add_product_to_db("Headphones", 150.00, 20)

    # Show all products
    print("\n📦 Available Products:")
    for p in get_all_products():
        print(f"ID: {p[0]} | {p[1]} | ${p[2]} | Stock: {p[3]}")

    # Create a user and cart
    user = User("Hamza")
    cart = ShoppingCart(user)

    # Add items to cart
    cart.add_product(1, 1)  # 1 Laptop
    cart.add_product(3, 2)  # 2 Headphones

    print("\n🛒 Cart contents:", cart.view_cart())
    print("Total before checkout:", cart.calculate_total())

    # Perform checkout
    checkout(cart)

    # Show updated products
    print("\n📦 Updated Products:")
    for p in get_all_products():
        print(f"ID: {p[0]} | {p[1]} | ${p[2]} | Stock: {p[3]}")
