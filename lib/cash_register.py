#!/usr/bin/env python3

class CashRegister:
    """A class representing a cash register with functionality for tracking items, 
    calculating the total, applying discounts, and voiding the last transaction.
    """
    
    def __init__(self, discount=0):
        """Initialize the cash register with a discount, total of 0, and empty items list."""
        self.discount = discount
        self.total = 0.0
        self.items = []
        self._last_transaction = 0.0

    def add_item(self, title, price, quantity=1):
        """
        Adds items to the cash register's total and tracks them in the items list.
        
        Args:
            title: The name of the item
            price: The price of a single item
            quantity: The number of items to add (default: 1)
        """
        item_cost = price * quantity
        
        # Update total
        self.total += item_cost
        
        # Track individual items in the list
        for _ in range(quantity):
            self.items.append(title)
        
        # Track the last transaction amount
        self._last_transaction = item_cost

    def apply_discount(self):
        """
        Applies the discount to the current total.
        Prints a success message if discount exists, or error message if no discount.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            # Calculate the discount amount
            discount_amount = (self.discount / 100) * self.total
            
            # Apply the discount
            self.total -= discount_amount
            
            # Round to avoid floating point issues
            self.total = round(self.total, 2)
            
            # Print success message (note: total should be an integer if it's a whole number)
            print(f"After the discount, the total comes to ${int(self.total) if self.total == int(self.total) else self.total}.")

    def void_last_transaction(self):
        """
        Removes the last transaction's amount from the total.
        """
        # Subtract the last transaction amount
        self.total -= self._last_transaction
        
        # Reset to 0.0 if very close to zero (floating point precision)
        if abs(self.total) < 0.0001:
            self.total = 0.0
        
        # Reset last transaction
        self._last_transaction = 0.0