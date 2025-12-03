from models import Order, OrderStatus, PaymentMethod, Product, Cart
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel

console = Console()

def select_product(catalog):
    table = Table(title="Product Catalog",show_lines= True)
    table.add_column("ID", justify="centre")
    table.add_column("Name", justify="left")
    table.add_column("Price (₹) ", justify="right")

    for p in catalog:
        table.add_row(str(p.id), p.name, str(p.price))
        

    console.print(table)

    while True:
        product_id = IntPrompt.ask("Enter product ID")
        product = next((p for p in catalog if p.id == product_id), None)

        if product:
            qty = IntPrompt.ask(f"Enter quantity for [bold green]{product.name}[/]")
            if qty > 0:
                return product, qty
            else:
                console.print("[red]Quantity must be greater than 0")

        else:
            console.print("[red]Invalid product ID[/]")


def choose_payment():
    console.print("[bold cyan ]Choose your Payment mode: [/]")
    for i,pm in enumerate(PaymentMethod, start = 1):
        console.print(f"{i}. {pm.value}")
    
    while True:
        choice = IntPrompt.ask("Enter option")
        if 1 <= choice <= len(PaymentMethod):
            return list(PaymentMethod)[choice-1]
        else:
            console.print("[red]Invalid option[/]")

def main():
    catalog = [
    Product(1, "Wireless Mouse", 899.0),
    Product(2, "Mechanical Keyboard", 2499.0),
    Product(3, "Laptop Stand", 1299.0),
    Product(4, "Gaming Headset", 1999.0),
    Product(5, "USB-C Hub", 1599.0),
    Product(6, "Webcam HD", 2199.0),
    Product(7, "External SSD 1TB", 7499.0),
    Product(8, "Laptop Backpack", 1799.0)
    ]

    cart = Cart()
    console.print(Panel("[bold yellow]🛒 Welcome to Python E-Commerce CLI![/]"))

    while True:
        product, qty = select_product(catalog)
        cart.add_item(product, qty)
        more = Prompt.ask("Add more Products? (y,n)", choices = ["y", "n"], default = "n")
        if more.lower()!= "y":
            break


    table = Table(title="🛒 Cart Items: ", show_lines=True)
    table.add_column("Product", justify="left")
    table.add_column("Quantity", justify="centre")
    table.add_column("Total Proce (₹)", justify="right")

    for item in cart.list_items():
        table.add_row(item.product.name, str(item.quantity), str(item.total_price()))

    console.print(table)
    console.print(f"[bold green]💰Cart Total: {cart.calculate_total()}[/]")


    payment_mode = choose_payment()
    order = Order(id=101, items = cart.list_items(), payment_method = payment_mode)
    console.print(f"\n📦 Order #{order.id} created with payment mode: [bold cyan]{order.payment_method.value} and status: [bold yellow]{order.status.name}[/]")

    for s in [OrderStatus.CREATED, OrderStatus.PACKED, OrderStatus.SHIPPED, OrderStatus.DELIVERED]:
        order.update_status()
        console.print(f" Updated Order Status: [bold green]{order.status.name}[/]")


    console.print(f"\n [bold magenta] FINAL ORDER TOTAL:  ₹{order.total_amount()}[/]")
    console.print(f"[bold green] 🎉Order Delivered Successfully!![/]")


if __name__ == "__main__":
    main()




                     


