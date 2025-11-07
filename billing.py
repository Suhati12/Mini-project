import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

class SimpleBilling:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🛒 Simple Grocery Billing")
        self.root.geometry("800x600")
        self.root.config(bg="#1e3a8a")
        
        # Variables
        self.name = tk.StringVar()
        self.phone = tk.StringVar()
        self.bill_id = tk.StringVar(value=f"B{random.randint(1000, 9999)}")
        
        # Products
        self.products = {
            "Rice": {"price": 50, "var": tk.IntVar()},
            "Wheat": {"price": 40, "var": tk.IntVar()},
            "Sugar": {"price": 45, "var": tk.IntVar()},
            "Oil": {"price": 100, "var": tk.IntVar()},
            "Tea": {"price": 120, "var": tk.IntVar()},
            "Coffee": {"price": 150, "var": tk.IntVar()},
            "Salt": {"price": 20, "var": tk.IntVar()},
            "Milk": {"price": 60, "var": tk.IntVar()}
        }
        
        self.total_var = tk.StringVar(value="₹0")
        self.create_ui()
    
    def create_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#3b82f6", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(header, text="🛒 GROCERY BILLING SYSTEM", 
                font=("Arial", 18, "bold"), bg="#3b82f6", fg="white").pack(expand=True)
        
        # Main container
        main = tk.Frame(self.root, bg="#1e3a8a")
        main.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Left side - Customer & Products
        left = tk.Frame(main, bg="#1e3a8a")
        left.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # Customer info
        cust_frame = tk.LabelFrame(left, text="Customer Info", bg="#1e3a8a", fg="white", font=("Arial", 12, "bold"))
        cust_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(cust_frame, text="Name:", bg="#1e3a8a", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(cust_frame, textvariable=self.name, width=20, font=("Arial", 10)).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(cust_frame, text="Phone:", bg="#1e3a8a", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(cust_frame, textvariable=self.phone, width=20, font=("Arial", 10)).grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(cust_frame, text="Bill ID:", bg="#1e3a8a", fg="white").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        tk.Label(cust_frame, textvariable=self.bill_id, bg="#1e3a8a", fg="yellow", font=("Arial", 10, "bold")).grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        # Products
        prod_frame = tk.LabelFrame(left, text="Products", bg="#1e3a8a", fg="white", font=("Arial", 12, "bold"))
        prod_frame.pack(fill="both", expand=True)
        
        tk.Label(prod_frame, text="Item", bg="#1e3a8a", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(prod_frame, text="Price", bg="#1e3a8a", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10, pady=5)
        tk.Label(prod_frame, text="Qty", bg="#1e3a8a", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10, pady=5)
        
        row = 1
        for item, data in self.products.items():
            tk.Label(prod_frame, text=item, bg="#1e3a8a", fg="white").grid(row=row, column=0, padx=10, pady=2, sticky="w")
            tk.Label(prod_frame, text=f"₹{data['price']}", bg="#1e3a8a", fg="lightgreen").grid(row=row, column=1, padx=10, pady=2)
            
            qty_entry = tk.Entry(prod_frame, textvariable=data['var'], width=8, font=("Arial", 10))
            qty_entry.grid(row=row, column=2, padx=10, pady=2)
            qty_entry.bind('<KeyRelease>', self.calculate_total)
            row += 1
        
        # Total
        total_frame = tk.Frame(left, bg="#1e3a8a")
        total_frame.pack(fill="x", pady=10)
        
        tk.Label(total_frame, text="TOTAL:", bg="#1e3a8a", fg="white", font=("Arial", 14, "bold")).pack(side="left")
        tk.Label(total_frame, textvariable=self.total_var, bg="#1e3a8a", fg="yellow", font=("Arial", 14, "bold")).pack(side="right")
        
        # Buttons
        btn_frame = tk.Frame(left, bg="#1e3a8a")
        btn_frame.pack(fill="x", pady=10)
        
        tk.Button(btn_frame, text="Generate Bill", command=self.generate_bill, 
                 bg="#10b981", fg="white", font=("Arial", 11, "bold"), width=15).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Clear All", command=self.clear_all, 
                 bg="#ef4444", fg="white", font=("Arial", 11, "bold"), width=15).pack(side="right", padx=5)
        
        # Right side - Bill display
        right = tk.Frame(main, bg="#1e3a8a")
        right.pack(side="right", fill="both", expand=True)
        
        tk.Label(right, text="📄 BILL RECEIPT", bg="#1e3a8a", fg="white", font=("Arial", 12, "bold")).pack(pady=(0, 10))
        
        self.bill_text = tk.Text(right, font=("Courier", 9), bg="white", fg="black", wrap="word")
        self.bill_text.pack(fill="both", expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(right, command=self.bill_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.bill_text.config(yscrollcommand=scrollbar.set)
    
    def calculate_total(self, event=None):
        try:
            total = 0
            for item, data in self.products.items():
                qty = data['var'].get() or 0
                total += qty * data['price']
            self.total_var.set(f"₹{total}")
        except:
            self.total_var.set("₹0")
    
    def generate_bill(self):
        if not self.name.get().strip():
            messagebox.showerror("Error", "Please enter customer name!")
            return
        
        # Check if any items selected
        total_items = sum(data['var'].get() or 0 for data in self.products.values())
        if total_items == 0:
            messagebox.showerror("Error", "Please select items!")
            return
        
        self.bill_text.delete("1.0", tk.END)
        
        # Calculate totals
        subtotal = 0
        bill_content = f"""
{'='*40}
    🛒 GROCERY STORE RECEIPT
{'='*40}

Bill ID: {self.bill_id.get()}
Date: {datetime.now().strftime('%d/%m/%Y %I:%M %p')}

Customer: {self.name.get()}
Phone: {self.phone.get()}

{'='*40}
ITEMS PURCHASED:
{'='*40}
"""
        
        for item, data in self.products.items():
            qty = data['var'].get() or 0
            if qty > 0:
                price = data['price']
                amount = qty * price
                subtotal += amount
                bill_content += f"{item:<12} {qty:>3} x ₹{price:<3} = ₹{amount}\n"
        
        # Add totals
        tax = subtotal * 0.05  # 5% tax
        total = subtotal + tax
        
        bill_content += f"""
{'-'*40}
Subtotal:           ₹{subtotal:.2f}
Tax (5%):           ₹{tax:.2f}
{'-'*40}
TOTAL:              ₹{total:.2f}
{'-'*40}

Payment: Cash
Change: ₹0.00

{'-'*40}
Thank you for shopping!
Visit us again soon! 😊
{'-'*40}
"""
        
        self.bill_text.insert("1.0", bill_content)
        messagebox.showinfo("Success", "Bill generated successfully!")
    
    def clear_all(self):
        self.name.set("")
        self.phone.set("")
        self.bill_id.set(f"B{random.randint(1000, 9999)}")
        
        for data in self.products.values():
            data['var'].set(0)
        
        self.total_var.set("₹0")
        self.bill_text.delete("1.0", tk.END)
        messagebox.showinfo("Success", "All data cleared!")
    
    def run(self):
        self.root.mainloop()

# Run the app
if __name__ == "__main__":
    app = SimpleBilling()
    app.run()

