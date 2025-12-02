# 🛒 E-Commerce Order Processing System

A clean and modular Python project that simulates a small e-commerce workflow using **Dataclasses**, **Enums**, and production-style project structure.  
This project is perfect for showcasing your understanding of Python OOP, code organization, and real-world logic.

---

## 🚀 Features

- 📦 Product catalog using `dataclass`
- 🛒 Cart system (add/remove items)
- 💵 Automatic total price calculation
- 🔄 Order processing pipeline:
  - CREATED → CONFIRMED → PACKED → SHIPPED → DELIVERED
- 💳 Payment modes using `Enum`
- 🔐 Safe order state transitions (validations included)
- 🧱 Clean folder structure for scalability

---

## 📁 Project Structure

ecommerce_order_system/
│── main.py
│── README.md
│
├── models/
│   ├── __init__.py
│   ├── enums.py
│   ├── product.py
│   ├── cart.py
│   └── order.py

---

## ▶️ Run the Project
```bash
python3 main.py



