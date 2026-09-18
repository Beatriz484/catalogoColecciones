# System Name: Collectibles Catalog Manager

print("==========================================")
print("  WELCOME TO THE COLLECTIBLES CATALOG     ")
print("==========================================")
print()

catalog = []
TOTAL_ITEMS = 10
VALID_STATUSES = ["disponible", "reservada", "vendida"]

# ==========================================
# NIVEL I: CAPTURA Y VALIDACIONES (Parte 2, 3 y 12)
# ==========================================
for i in range(1, TOTAL_ITEMS + 1):
    print(f"--- Registering Item {i} of {TOTAL_ITEMS} ---")

    # Validation: Non-empty name
    name = input("Enter name: ").strip()
    while not name:
        print("Error: Name cannot be empty.")
        name = input("Enter name: ").strip()

    item_id = input("Enter ID: ").strip()
    category = input("Enter category: ").strip()

    # Validation: Numeric and positive price
    while True:
        try:
            price = float(input("Enter price: "))
            if price > 0:
                break
            else:
                print("Error: Price must be greater than zero.")
        except ValueError:
            print("Error: Invalid input. Price must be a number.")

    # Validation: Allowed status
    status = input("Enter status (disponible / reservada / vendida): ").strip().lower()
    while status not in VALID_STATUSES:
        print(f"Error: Status must be one of {VALID_STATUSES}.")
        status = input("Enter status (disponible / reservada / vendida): ").strip().lower()

    # Validation: Description containing 'usada' or 'certificada'
    description = input("Enter description (must contain 'usada' or 'certificada'): ").strip()
    while "usada" not in description.lower() and "certificada" not in description.lower():
        print("Error: Description must contain 'usada' or 'certificada'.")
        description = input("Enter description (must contain 'usada' or 'certificada'): ").strip()

    # Store item as a dictionary
    item = {
        "id": item_id,
        "name": name,
        "category": category,
        "price": price,
        "status": status,
        "description": description
    }

    catalog.append(item)
    print("Item registered successfully!\n")

# ==========================================
# NIVEL III: MENÚ INTERACTIVO Y MÉTRICAS (Parte 10 y 11)
# ==========================================
while True:
    print("\n==========================================")
    print("             MAIN MENU                    ")
    print("==========================================")
    print("1. Show all items")
    print("2. Show available items")
    print("3. Show average price and metrics")
    print("4. Exit")

    option = input("Select an option (1-4): ").strip()

    if option == "1":
        print("\n--- ALL ITEMS IN CATALOG ---")
        for idx, item in enumerate(catalog, start=1):
            print(
                f"{idx}. ID: {item['id']} | Name: {item['name']} | Category: {item['category']} | Price: ${item['price']} | Status: {item['status']} | Description: {item['description']}")

    elif option == "2":
        print("\n--- AVAILABLE ITEMS ('disponible') ---")
        found = False
        for idx, item in enumerate(catalog, start=1):
            if item["status"] == "disponible":
                print(f"{idx}. {item['name']} - ${item['price']}")
                found = True
        if not found:
            print("No available items found.")

    elif option == "3":
        print("\n--- CATALOG METRICS ---")
        total_items = len(catalog)
        available_count = sum(1 for item in catalog if item["status"] == "disponible")
        reserved_count = sum(1 for item in catalog if item["status"] == "reservada")
        sold_count = sum(1 for item in catalog if item["status"] == "vendida")

        total_price = sum(item["price"] for item in catalog)
        avg_price = total_price / total_items if total_items > 0 else 0

        print(f"Total items: {total_items}")
        print(f"Available items: {available_count}")
        print(f"Reserved items: {reserved_count}")
        print(f"Sold items: {sold_count}")
        print(f"Total price sum: ${total_price:.2f}")
        print(f"Average price: ${avg_price:.2f}")

    elif option == "4":
        print("\nExiting program... Goodbye!")
        break
    else:
        print("\nError: Invalid option. Please enter a number between 1 and 4.")
