import tkinter as tk

class HotelMenu:
    def __init__(self, window):
        self.window = window
        self.window.title("Restro Menu System")
        self.window.geometry("550x420")
        self.window.config(bg="#f7f7f7")
        self.window.resizable(False, False)

        self.menu = {
            "Pizza": 500,
            "Boiled Egg": 25,
            "Momo": 150,
            "Pasta": 100,
            "Coffee": 150,
            "Coke": 200,
        }

        self.order_total = 0
        self.setup_ui()

    def setup_ui(self):
        title_label = tk.Label(
            self.window, 
            text="Welcome to Dipesh Restro", 
            font=("Arial Bold", 18), 
            bg="#f7f7f7", 
            fg="#2c3e50"
        )
        title_label.pack(pady=15)

        main_container = tk.Frame(self.window, bg="#f7f7f7")
        main_container.pack(fill="both", expand=True, padx=20)

        left_menu_frame = tk.LabelFrame(
            main_container, 
            text=" Select Items ", 
            font=("Arial Bold", 11), 
            bg="#f7f7f7", 
            padx=10, 
            pady=10
        )
        left_menu_frame.pack(side="left", fill="both", expand=True, padx=10, pady=5)

        for item, price in self.menu.items():
            item_button = tk.Button(
                left_menu_frame, 
                text=f"{item} — Rs. {price}", 
                font=("Arial", 11), 
                bg="#ffffff", 
                relief="groove", 
                anchor="w", 
                padx=15,
                pady=2,
                command=lambda val=item: self.add_item_to_order(val)
            )
            item_button.pack(fill="x", pady=4)

        right_order_frame = tk.LabelFrame(
            main_container, 
            text=" Your Current Order ", 
            font=("Arial Bold", 11), 
            bg="#f7f7f7", 
            padx=10, 
            pady=10
        )
        right_order_frame.pack(side="right", fill="both", expand=True, padx=10, pady=5)

        self.order_listbox = tk.Listbox(right_order_frame, font=("Arial", 10), bg="#ffffff", bd=1)
        self.order_listbox.pack(fill="both", expand=True, pady=5)

        self.bill_label = tk.Label(
            right_order_frame, 
            text="Total Bill: Rs. 0", 
            font=("Arial Bold", 13), 
            bg="#f7f7f7", 
            fg="#27ae60"
        )
        self.bill_label.pack(pady=5)

        clear_button = tk.Button(
            right_order_frame, 
            text="Clear Order", 
            font=("Arial", 10), 
            bg="#e74c3c", 
            fg="white", 
            relief="flat",
            command=self.reset_order
        )
        clear_button.pack(fill="x", pady=2)

    def add_item_to_order(self, item_name):
        price = self.menu[item_name]
        self.order_total += price
        
        self.order_listbox.insert(tk.END, f"{item_name} (Rs. {price})")
        self.bill_label.config(text=f"Total Bill: Rs. {self.order_total}")

    def reset_order(self):
        self.order_total = 0
        self.order_listbox.delete(0, tk.END)
        self.bill_label.config(text="Total Bill: Rs. 0")

if __name__ == "__main__":
    main_window = tk.Tk()
    app = HotelMenu(main_window)
    main_window.mainloop()
