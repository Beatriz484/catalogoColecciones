# System Name: Collectibles Catalog Manager

print("==========================================")
print("  WELCOME TO THE COLLECTIBLES CATALOG     ")
print("==========================================")
print()

# Catalog storage using a list of dictionaries
catalog = []

# Requesting 10 collectible items directly from terminal
TOTAL_ITEMS = 10

for i in range(1, TOTAL_ITEMS + 1):
    print(f"--- Registering Item {i} of {TOTAL_ITEMS} ---")

    item_id = input("Enter ID: ")
    name = input("Enter name: ")
    category = input("Enter category: ")
    price = float(input("Enter price: "))
    status = input("Enter status (disponible / reservada / vendida): ")
    description = input("Enter description (must contain 'usada' or 'certificada'): ")

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

# Part 4: Unique categories using a set
categories_set = set()
for item in catalog:
    categories_set.add(item["category"])

# Part 5: Display full catalog information
print("\n==========================================")
print("         FULL CATALOG DISPLAY             ")
print("==========================================")

for item in catalog:
    print(
        f"ID: {item['id']} | Name: {item['name']} | Category: {item['category']} | Price: ${item['price']} | Status: {item['status']} | Description: {item['description']}")

print("\n--- GENERAL CATALOG SUMMARY ---")
print(f"Total items in catalog: {len(catalog)}")
print(f"Unique categories: {categories_set}")
print(f"Total unique categories count: {len(categories_set)}")