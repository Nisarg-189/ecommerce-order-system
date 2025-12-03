from dataclasses import dataclass
from .product import Product

@dataclass
class CartItem:
    product : Product
    quantity : int


    def total_price(self):
        return self.product.price * self.quantity
    

class Cart:

    def __init__(self):
        self.items = []

    def add_item(self, product: Product, qty: int = 1):
        cart_item = CartItem(product, qty)
        self.items.append(cart_item)
        
    def calculate_total(self):
        return sum(item.total_price() for item in self.items)
    
    def list_items(self):
        return self.items