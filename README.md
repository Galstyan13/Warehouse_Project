
# 🧾 Warehouse Management System

A simple desktop-based stock management application built using **Python (Tkinter)** and **MySQL**. This system allows you to add, update, delete, search, and export stock inventory data in a user-friendly graphical interface. It is suitable for managing inventory in small shops, repair centers, or personal use.

## 📦 Features

- Add new inventory items with auto-generated IDs
- Edit existing records (except the item ID)
- Delete selected stock items
- Search items by various fields
- Export data to a CSV file
- Interactive table using `ttk.Treeview`
- Input validation with real-time feedback
- Clean and intuitive UI with categorized dropdowns

## 🛠 Technologies Used

- **Python 3.x**
- **Tkinter** – for GUI
- **PyMySQL** – for database connection
- **MySQL** – to store and manage stock records
- **NumPy** – used in random ID generation
- **CSV Module** – to export data
- **datetime** – for timestamping exports

## 📁 Folder Structure

```
├── stock_management.py        # Main Python file
├── README.md                  # This file
├── requirements.txt           # List of dependencies
└── stocks_YYYY-MM-DD_HH-MM.csv  # Auto-generated exports
```

## 🧰 Requirements

Before running the project, ensure you have the following installed:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```
tk
PyMySQL==1.1.0
numpy==1.26.4
```

## ⚙️ Database Setup

1. Install MySQL and start your local server.
2. Create a database named `warehousemanagmentsystem`.
3. Use the following SQL schema to create the `warehouse` table:

```sql
CREATE TABLE warehouse (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_id VARCHAR(10) NOT NULL UNIQUE,
    name VARCHAR(100),
    price FLOAT,
    quantity INT,
    category VARCHAR(100),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

> ⚠️ Note: In your Python code, use the actual column names (`item_id`, `name`, `price`, etc.) without single quotes in SQL queries.

## ▶️ How to Run

1. Make sure your MySQL server is running.
2. Open a terminal and run:
   ```bash
   python main.py
   ```
3. The app window will launch. From here you can start managing your stock items.

## 📤 Exporting to Excel

Use the **"Export Excel"** button in the UI to save current stock data to a `.csv` file. The file is named with a timestamp like:

```
warehouse_2025-04-15_13-45.csv
```

## 🔧 Future Improvements

- Add login system with user roles (Admin/User)
- Support for bulk CSV import
- Pagination for large stock lists
- Cloud-based database support
- More advanced filters and reporting


This project is open-source and free to use and further development
---
