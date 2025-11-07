import sqlite3
from tkinter import *
from tkinter import messagebox

def connect_db():
    return sqlite3.connect('food_order.db')

def get_menu():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM menu")
    data = cur.fetchall()
    conn.close()
    return data

def save_order(name, items, total):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO orders (customer_name, items, total) VALUES (?, ?, ?)", (name, items, total))
    conn.commit()
    conn.close()

def place_order():
    name = entry_name.get()
    if not name:
        messagebox.showerror("Error", "Please enter your name!")
        return

    total = 0
    ordered_items = []

    for i, qty_var in enumerate(qty_vars):
        qty = qty_var.get()
        if qty > 0:
            item_name = menu[i][1]
            item_price = menu[i][2]
            total += item_price * qty
            ordered_items.append(f"{item_name} x {qty}")

    if not ordered_items:
        messagebox.showerror("Error", "Please select at least one item!")
        return

    order_summary = "\n".join(ordered_items)
    save_order(name, order_summary, total)
    messagebox.showinfo("Order Placed",
                        f"Order placed successfully!\n\nName: {name}\n\nItems:\n{order_summary}\n\nTotal: ₹{total}")

    for var in qty_vars:
        var.set(0)
    entry_name.delete(0, END)

def view_history():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT customer_name, items, total, order_date FROM orders ORDER BY order_id DESC")
    records = cur.fetchall()
    conn.close()

    history_window = Toplevel(root)
    history_window.title("Order History")
    history_window.geometry("450x400")
    history_window.config(bg="#fefefe")

    Label(history_window, text="Order History", font=("Arial", 14, "bold"), bg="#fefefe").pack(pady=10)

    if not records:
        Label(history_window, text="No orders found.", bg="#fefefe").pack()
        return

    text_area = Text(history_window, width=60, height=18, wrap=WORD)
    text_area.pack(padx=10, pady=10)

    for record in records:
        text_area.insert(END, f"Name: {record[0]}\nItems: {record[1]}\nTotal: ₹{record[2]}\nDate: {record[3]}\n\n")

    text_area.config(state=DISABLED)

root = Tk()
root.title("🍔 Online Food Ordering System")
root.geometry("550x600")
root.config(bg="#fff8e7")

Label(root, text="🍽️ Online Food Ordering System", font=("Arial", 18, "bold"), bg="#fff8e7", fg="#d35400").pack(pady=15)
Label(root, text="Enter Your Name:", font=("Arial", 12), bg="#fff8e7").pack()
entry_name = Entry(root, font=("Arial", 12), width=30)
entry_name.pack(pady=5)
Label(root, text="Select Your Items:", font=("Arial", 14, "bold"), bg="#fff8e7").pack(pady=10)

menu = get_menu()
qty_vars = []

frame_menu = Frame(root, bg="#fff8e7")
frame_menu.pack(pady=5)

for item_id, name, price in menu:
    var = IntVar()
    qty_vars.append(var)
    frame_item = Frame(frame_menu, bg="#fff8e7")
    frame_item.pack(anchor="w", pady=3)
    Label(frame_item, text=f"{name} - ₹{price}", font=("Arial", 12), bg="#fff8e7").pack(side=LEFT, padx=10)
    Spinbox(frame_item, from_=0, to=10, textvariable=var, width=5, font=("Arial", 12)).pack(side=LEFT, padx=10)

Button(root, text="Place Order", font=("Arial", 13, "bold"), bg="#27ae60", fg="white", command=place_order, width=15).pack(pady=15)
Button(root, text="View Order History", font=("Arial", 12, "bold"), bg="#2980b9", fg="white", command=view_history, width=18).pack(pady=5)
Button(root, text="Exit", font=("Arial", 12, "bold"), bg="#c0392b", fg="white", command=root.destroy, width=10).pack(pady=10)

root.mainloop()
