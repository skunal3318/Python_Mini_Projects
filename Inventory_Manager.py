# Mini Inventory Manager

inventory = {}

def add_product():
    product = input("Enter product name: ").strip().capitalize()
    quantity = int(input(f"Enter quantity for {product}: "))
    if product in inventory:
        print("Product already exists. Updating quantity...")
        inventory[product] += quantity
    else:
        inventory[product] = quantity
    print(f"{product} now has {inventory[product]} items.\n")

def update_stock():
    product = input("Enter product name to update: ").strip().capitalize()
    if product in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[product] = quantity
        print(f"Updated {product} stock to {quantity}.\n")
    else:
        print(f"{product} not found in inventory!\n")

def show_low_stock(threshold=10):
    print(f"\n📦 Products with stock below {threshold}:")
    low_stock = [item for item, qty in inventory.items() if qty < threshold]
    if low_stock:
        for item in low_stock:
            print(f"{item} → {inventory[item]} units")
    else:
        print("All products have sufficient stock.\n")

def view_inventory():
    print("\n📋 Current Inventory:")
    for product, qty in inventory.items():
        print(f"{product} → {qty} units")
    print()

# Main Loop
def menu():
    while True:
        print("\n====== Inventory Manager ======")
        print("1. Add Product")
        print("2. Update Stock")
        print("3. Show Low Stock Items")
        print("4. View Inventory")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_product()
        elif choice == '2':
            update_stock()
        elif choice == '3':
            threshold = int(input("Enter low stock threshold (default 10): ") or 10)
            show_low_stock(threshold)
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            print("Exiting Inventory Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
