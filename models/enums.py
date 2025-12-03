from enum import Enum, auto

class OrderStatus(Enum):
    CONFIRMED = auto()
    CREATED = auto()
    PACKED = auto()
    SHIPPED = auto()
    DELIVERED = auto()

class PaymentMethod(Enum):
    COD = "Cash on Delivery"
    CARD = "CARD"
    UPI = "UPI"