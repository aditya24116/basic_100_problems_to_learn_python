# 🚀 Problem 23/100 — Inventory Management System

# Ab difficulty ek level aur badhegi.

# Problem Statement

# Ek shop ka inventory banao.

# User se pehle pucho:
#     Enter number of products:

# Phir har product ke liye:

# * Product Name
# * Quantity

# Store as:
#     {
#     "Pen": 20,
#     "Book": 15,
#     "Laptop": 5
# }
    
# Phir menu dikhana:
#     1. Search Product
#     2. Update Quantity
#     3. Exit
    
# Example

# Search:
#     Enter product name: Pen

#     Quantity: 20
    
# Update:
#     Enter product name: Pen
#     Enter new quantity: 30
    
# Output:
#     Updated Successfully!

def create_dictionay(number_of_products):
    for i in range(number_of_products):
        name = input("Enter product name:")
        quantity = int(input("Enter product quantity:"))
        products_details[name] = quantity
    show_inventory(products_details)

def show_inventory(products_details):
    print("\n----- Current Inventory -----")

    for key, value in products_details.items():
        print(f"{key} : {value}")
def add_product(products_details):
    new_product = input("Enter product name:")
    if new_product in products_details:
        print("Product already exists.")
    else:
        quantity = int(input("Enter product quantity:"))
        products_details[new_product] = quantity
    show_inventory(products_details)
def search_product(products_details):
    product_name = input("Enter product name:")
    if product_name in products_details:
        print(product_name,":",products_details[product_name])
    else:
        print("Product not found.")
def update_product(products_details):
    update_product_name = input("Enter product name:")
    if update_product_name in products_details:
        new_quantity = int(input("Enter new quantity:"))
        products_details[update_product_name]=new_quantity
        print("Updated Successfully!")
    else:
        print("Product not found!")
    show_inventory(products_details)
number_of_products = int(input("Enter number of products:"))
products_details = {}
create_dictionay(number_of_products)
while True:
    print("\n===== MENU =====")
    print("1. Add New product:")
    print("2. Search Product:")
    print("3. Update Quantity:")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_product(products_details)
    elif choice == 2:
        search_product(products_details)
    elif choice == 3:
        update_product(products_details)
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Choose a valid option:")
