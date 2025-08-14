# ---------------------------
# Base Class: Payment
# ---------------------------
class Payment:
    def __init__(self, amount):
        self._amount = amount  # Protected attribute
        self.__status = "Pending"  # Private attribute

    def process(self):
        """
        Default payment process (to be overridden by subclasses).
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def get_status(self):
        """
        Getter for private status.
        """
        return self.__status

    def _set_status(self, status):
        """
        Protected method to set private status.
        """
        self.__status = status

    def __str__(self):
        return f"Payment of ${self._amount:.2f} - Status: {self.__status}"

    def __repr__(self):
        return f"Payment(amount={self._amount}, status='{self.__status}')"

    def __add__(self, other):
        """
        Magic method to sum payments.
        """
        if isinstance(other, Payment):
            return Payment(self._amount + other._amount)
        return NotImplemented


# ---------------------------
# Subclass: CreditCardPayment
# ---------------------------
class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):
        # Overriding process method
        print(f"Processing credit card payment of ${self._amount:.2f}...")
        self._set_status("Completed")  # Using protected method to update private attribute


# ---------------------------
# Subclass: PayPalPayment
# ---------------------------
class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):
        # Overriding process method
        print(f"Processing PayPal payment of ${self._amount:.2f} from {self.email}...")
        self._set_status("Completed")


# ---------------------------
# Demonstrating Polymorphism
# ---------------------------
def process_all_payments(payments):
    for p in payments:
        p.process()  # Calls overridden method depending on object type
        print(p)  # Uses __str__ magic method


# ---------------------------
# Example Usage
# ---------------------------
if __name__ == "__main__":
    payment1 = CreditCardPayment(100.50, "1234-5678-9876-5432")
    payment2 = PayPalPayment(59.99, "customer@example.com")

    # Polymorphism in action
    process_all_payments([payment1, payment2])

    # Demonstrate __add__ magic method
    combined_payment = payment1 + payment2
    print("Combined payment:", combined_payment)

    # Encapsulation example
    print("Payment1 status (via getter):", payment1.get_status())
