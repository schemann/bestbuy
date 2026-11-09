class Product:
    """A product type available in the store, with its stock quantity."""

    def __init__(self, name: str, price: float, quantity: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must be a non-empty string.")
        if isinstance(price, bool) or not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the quantity currently in stock."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Set the stock quantity; a quantity of 0 deactivates the product."""
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print a one-line description of the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """Buy the given quantity, update the stock and return the total price."""
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if not self.active:
            raise Exception(f"{self.name} is not active and cannot be bought.")
        if quantity > self.quantity:
            raise Exception(
                f"Only {self.quantity} of {self.name} in stock, "
                f"cannot buy {quantity}."
            )

        self.set_quantity(self.quantity - quantity)
        return float(self.price * quantity)


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
