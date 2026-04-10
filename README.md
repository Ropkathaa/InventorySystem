# 🛒 Inventory Management System (Polyglot Persistence)

## 📌 Overview
This project is a backend-based Inventory Management System built using Flask.  
It demonstrates **Polyglot Persistence** by integrating multiple databases, each used for a specific purpose.

---

## 🚀 Technologies Used

- 🐍 Python (Flask)
- 🍃 MongoDB → Product storage
- ⚡ Redis → Rate Limiting
- 🔗 Neo4j → Product–Manufacturer relationships

---

## 🧠 Core Concept

### 🔥 Polyglot Persistence
Using multiple databases in one system based on their strengths:

| Feature | Database | Reason |
|--------|--------|--------|
| Inventory Storage | MongoDB | Flexible NoSQL storage |
| Rate Limiting | Redis | Fast in-memory operations |
| Relationships | Neo4j | Graph-based queries |

---

## ⚡ Features

### 🟢 Inventory Management (MongoDB)
- Add Product (POST)
- View All Products (GET)
- View Product by ID (GET)
- Update Product (PUT)
- Delete Product (DELETE)

---

### 🔵 Rate Limiting (Redis)
- Endpoint: `/ratelimit`
- Limit: **5 requests per minute**
- Prevents API abuse

---

### 🟣 Graph Relationships (Neo4j)
- Product → Manufacturer mapping
- Efficient relationship queries

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|------|--------|-------------|
| POST | `/add_product` | Add new product |
| GET | `/get_products` | View all products |
| GET | `/get_product/<id>` | View product by ID |
| PUT | `/update_product/<id>` | Update product |
| DELETE | `/delete_product/<id>` | Delete product |
| GET | `/ratelimit` | Rate limit check |

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Ropkathaa/InventorySystem.git
cd InventorySystem
