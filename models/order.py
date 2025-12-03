from dataclasses import dataclass, field
from typing  import List
from models.enums import PaymentMethod, OrderStatus
from models.cart import CartItem

@dataclass
class Order:
    id : int
    items: list[CartItem]
    payment_method : PaymentMethod
    status : OrderStatus = field(default = OrderStatus.CONFIRMED)

    def total_amount(self):
        return sum(item.total_price() for item in self.items)

    def update_status(self):
        flow = {
            OrderStatus.CONFIRMED: OrderStatus.CREATED,
            OrderStatus.CREATED: OrderStatus.PACKED,
            OrderStatus.PACKED: OrderStatus.SHIPPED,
            OrderStatus.SHIPPED: OrderStatus.DELIVERED
        }
        self.status = flow.get(self.status, self.status)


