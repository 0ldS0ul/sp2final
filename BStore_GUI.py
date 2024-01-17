import customtkinter as ctk
from tkinter import ttk 
import tkinter as tk
from BStore_Database import DvdDb

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class BStore(ctk.CTk):
    def __init__(self, database):
        super().__init__()
        
        self.coolbg = ctk.CTkLabel(self, bg_color="#2C3531",width=1350, height=750)
        self.coolbg.place(x=0, y=0)

        self.coolbg = ctk.CTkLabel(self, bg_color="#242424",width=350, height=1050)
        self.coolbg.place(x=0, y=0)
        
        self.db = database

        self.title('DvD Store') 
        self.geometry('1350x750') 

        self.font = ("Courier", 12)

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('Treeview', 
                        font=self.font, 
                        foreground='black',
                        background='#D1E8E2',
                        fieldlbackground='#D1E8E2')

        self.style.map('Treeview', background=[('selected', '#116466')])

        self.tree = ttk.Treeview(self, height=15)

        self.tree['columns']=["ID", "Name", "Year", "Genre", "Price", "Available"]
        self.tree.column("#0", stretch=tk.NO, width=0)
        self.tree.column("ID", anchor=tk.CENTER, width=50)
        self.tree.column("Name", anchor=tk.CENTER, width=150)
        self.tree.column("Year", anchor=tk.CENTER, width=50)
        self.tree.column("Genre", anchor=tk.CENTER, width=150)
        self.tree.column("Price", anchor=tk.CENTER, width=75)
        self.tree.column("Available", anchor=tk.CENTER, width=50)

        self.tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.tree.heading("Name", text="Name", anchor=tk.CENTER)
        self.tree.heading("Year", text="Year", anchor=tk.CENTER)
        self.tree.heading("Genre", text="Genre", anchor=tk.CENTER)
        self.tree.heading("Price", text="Price", anchor=tk.CENTER)
        self.tree.heading("Available", text="Available", anchor=tk.CENTER)

        self.tree.place(x=375, y=40, width=950, height=650)

        # title label
        self.title_en = ctk.CTkLabel(self, 
                                     font=("Courier", 26), 
                                     text="DvD STORE DATABASE", 
                                     text_color="#FFCB9A",
                                     height=50)
        self.title_en.place(x=40, y=30)

        # id entry box
        self.num_en = ctk.CTkEntry(self, 
                                   font=self.font, 
                                   placeholder_text="Enter ID", 
                                   fg_color="#116466",
                                   border_color="#D1E8E2",
                                   border_width=2,
                                   width=250)
        self.num_en.place(x=60, y=100)

        # name entry box
        self.name_en = ctk.CTkEntry(self, 
                                    font=self.font, 
                                    placeholder_text="Enter DvD Name", 
                                    fg_color="#116466",
                                    border_color="#D1E8E2",
                                    border_width=2,
                                    width=250)
        self.name_en.place(x=60, y=150)

        # year entry box
        self.year_en = ctk.CTkEntry(self, 
                                    font=self.font, 
                                    placeholder_text="Enter Year", 
                                    fg_color="#116466",
                                    border_color="#D1E8E2",
                                    border_width=2,
                                    width=250)
        self.year_en.place(x=60, y=200)

        # genre drop down list/combo box
        self.genre_items = ["Enter Genre","Horror", "Action", "Romance", "Kids", "Fantasy", "Local"]
        self.genre_en = ctk.CTkComboBox(self, 
                                        values=self.genre_items, 
                                        font=self.font, 
                                        fg_color="#116466",
                                        border_color="#D1E8E2",
                                        border_width=2,
                                        width=250)
        self.genre_en.place(x=60, y=250)

        # price entry box
        self.price_en = ctk.CTkEntry(self, 
                                     font=self.font, 
                                     placeholder_text="Enter Price", 
                                     fg_color="#116466",
                                     border_color="#D1E8E2",
                                     border_width=2,
                                     width=250)
        self.price_en.place(x=60, y=300)

        # availability drop down list/combo box
        self.avail_items = ["Enter Availability", "No Stock", "In Stock"]
        self.avail_en = ctk.CTkComboBox(self, 
                                        values=self.avail_items, 
                                        font=self.font, 
                                        fg_color="#116466",
                                        border_color="#D1E8E2",
                                        border_width=2,
                                        width=250)
        self.avail_en.place(x=60, y=350)

        # buttons
        self.fgbutton_color = "#FFCB9A"
        self.button_text_color= "#FFCB9A"
        self.button_border_color = "#D1E8E2"
        self.button_border_width = 2
        self.button_text_color = "#2C3531"
        self.button_hover_color= "#D9B08C"

        self.fgbutton_color2 = "#D1E8E2"
        self.button_text_color2= "#FFCB9A"
        self.button_border_color2 = "#FFCB9A"
        self.button_border_width2 = 2
        self.button_text_color2 = "#2C3531"
        self.button_hover_color2= "gray"

        self.add = ctk.CTkButton(self, 
                                 corner_radius=20, 
                                 width=250, 
                                 font=self.font, 
                                 fg_color=self.fgbutton_color,
                                 border_color=self.button_border_color,
                                 border_width=self.button_border_width,
                                 text_color=self.button_text_color,
                                 hover_color=self.button_hover_color,
                                 text="Add Entry", 
                                 command=self.add_entry)
        self.add.place(x=60, y=400)

        self.up = ctk.CTkButton(self, 
                                corner_radius=20, 
                                width=250, 
                                font=self.font, 
                                fg_color=self.fgbutton_color,
                                border_color=self.button_border_color,
                                border_width=self.button_border_width,
                                text_color=self.button_text_color,
                                hover_color=self.button_hover_color,
                                text="Update Entry", 
                                command=self.up_entry)
        self.up.place(x=60, y=450)

        self.delete = ctk.CTkButton(self, 
                                    corner_radius=20, 
                                    width=250, 
                                    font=self.font, 
                                    fg_color=self.fgbutton_color,
                                    border_color=self.button_border_color,
                                    border_width=self.button_border_width,
                                    text_color=self.button_text_color,
                                    hover_color=self.button_hover_color,
                                    text="Delete Entry", 
                                    command=self.del_entry)
        self.delete.place(x=60, y=502)

        self.imp = ctk.CTkButton(self, 
                                 corner_radius=20, 
                                 width=250, 
                                 font=self.font, 
                                 fg_color=self.fgbutton_color2,
                                 border_color=self.button_border_color2,
                                 border_width=self.button_border_width2,
                                 text_color=self.button_text_color2,
                                 hover_color=self.button_hover_color2,
                                 text="Import CSV", 
                                 command=self.import_csv)
        self.imp.place(x=60, y=550)

        self.exp = ctk.CTkButton(self, 
                                 corner_radius=20, 
                                 width=250, 
                                 font=self.font, 
                                 fg_color=self.fgbutton_color2,
                                 border_color=self.button_border_color2,
                                 border_width=self.button_border_width2,
                                 text_color=self.button_text_color2,
                                 hover_color=self.button_hover_color2,
                                 text="Export as CSV", 
                                 command=self.exportc)
        self.exp.place(x=60, y=600)

        self.exp = ctk.CTkButton(self, 
                                 corner_radius=20, 
                                 width=250, 
                                 font=self.font, 
                                 fg_color=self.fgbutton_color2,
                                 border_color=self.button_border_color2,
                                 border_width=self.button_border_width2,
                                 text_color=self.button_text_color2,
                                 hover_color=self.button_hover_color2,
                                 text="Export as JSON", 
                                 command=self.exportj)
        self.exp.place(x=60, y=650)

    def reload_tree(self):
        print("Operation: Updating Tree...")
        data = self.db.display_data()
        self.tree.delete(*self.tree.get_children())
        for entry in data:
            self.tree.insert(parent='', index=tk.END, values=entry)

    def add_entry(self):
        print("Operation: Adding Entry...")
        id = self.num_en.get()
        name = self.name_en.get()
        year = self.year_en.get()
        genre = self.genre_en.get()
        price = self.price_en.get()
        avail = self.avail_en.get()

        if not (id and name and year and genre and price and avail):
            print("ERROR: failure to input all fields")
            pass
        elif self.db.num_check(id) == True:
            print("ERROR: trying to add an id that already exists")
            pass
        else:
            self.db.add_item(id,name,year,genre,price,avail)
            print(self.db.display_data())
            self.reload_tree()
            print(f"ID {id} Successfully Added")

    def up_entry(self):
        print("Operation: Updating Entry...")
        id = self.num_en.get()
        name = self.name_en.get()
        year = self.year_en.get()
        genre = self.genre_en.get()
        price = self.price_en.get()
        avail = self.avail_en.get()

        if not (id and name and year and genre and price and avail):
            print("ERROR: failure to input all fields")
            pass
        elif self.db.num_check(id) == False:
            print("ERROR: trying to update an id that doesn't exist")
            pass
        else:
            self.db.add_item(id,name,year,genre,price,avail)
            print(self.db.display_data())
            self.reload_tree()
            print(f"ID {id} Successfully Updated")

    def del_entry(self):
        id = self.num_en.get()
        print("Operation: Deleting Entry...")
        if self.db.num_check(id) == True:
            self.db.deleteItem(id)
            print(f"ID {id} Successfully Deleted")
            self.reload_tree()
        else:
            print("ERROR: trying to delete an unexisting item")

    def exportc(self):
        self.db.exportcsv()
        print("CSV File Created")
        print(f"Data exported to {self.db.file}")

    def import_csv(self):
        self.db.importcsv()
        print(f"CSV File Imported from {self.db.file}")
        self.reload_tree()
        print(self.db.database)

    def exportj(self):
        self.db.extract_to_json()
        print("JSON File Created")
        print(f"Data exported to {self.db.fileJSON}")


        
        