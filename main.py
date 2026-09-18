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
# ==========================================
# NIVEL II – Filtros, operadores y strings
# ==========================================

# Parte 6: Filtrar piezas por estado
print("\n--- PARTE 6: FILTRAR POR ESTADO ---")
for status_to_search in ["disponible", "reservada", "vendida"]:
    print(f"\nPiezas con estado '{status_to_search}':")
    found = False
    for item in catalog:
        if item["status"].lower() == status_to_search:
            print(f"- {item['name']} | Precio: ${item['price']}")
            found = True
    if not found:
        print(f"No se encontraron piezas con el estado '{status_to_search}'.")

# Parte 7: Filtrar piezas por precio mínimo
print("\n--- PARTE 7: FILTRAR POR PRECIO MÍNIMO ---")
min_price_input = input("Ingresa un precio mínimo para filtrar el catálogo: ")
min_price = float(min_price_input)

print(f"\nPiezas con precio superior a ${min_price}:")
found_price = False
for item in catalog:
    if item["price"] > min_price:
        print(f"- {item['name']}: ${item['price']}")
        found_price = True

if not found_price:
    print("No hay piezas que superen ese precio.")

# Parte 8: Aplicar operadores lógicos
print("\n--- PARTE 8: REGLAS LÓGICAS ---")
for item in catalog:
    # Regla 1: Publicación (Precio > 0 y estado es disponible)
    can_publish = item["price"] > 0 and item["status"].lower() == "disponible"

    # Regla 2: Revisión (Estado es reservada O vendida)
    needs_review = item["status"].lower() == "reservada" or item["status"].lower() == "vendida"

    print(f"Pieza '{item['name']}': ¿Publicable? {can_publish} | ¿Requiere revisión? {needs_review}")

print("\nPiezas NO vendidas:")
for item in catalog:
    if item["status"].lower() != "vendida":
        print(f"- {item['name']} (Estado: {item['status']})")

# Parte 9: Manipulación de strings
print("\n--- PARTE 9: MANIPULACIÓN DE STRINGS ---")
if len(catalog) > 0:
    first_item = catalog[0]

    # 1 y 2. Concatenación e Interpolación
    print("Concatenación: " + first_item["name"] + " - Categoría: " + first_item["category"])
    print(f"Interpolación: {first_item['name']} - Precio: ${first_item['price']}")

    # 3 y 4. Separación de etiquetas
    raw_tags = input("\nIntroduce etiquetas separadas por comas (ej. retro,anime,limited): ")
    tags_list = raw_tags.split(",")
    print("Lista de etiquetas procesadas:", tags_list)

    # 5. Reemplazar la palabra 'usada' por 'certificada'
    original_desc = first_item["description"]
    updated_desc = original_desc.replace("usada", "certificada")
    print("Descripción actualizada:", updated_desc)

    # 6 y 7. Formatos de nombre de usuario
    user_name_input = input("\nIntroduce un nombre de usuario: ")
    clean_user = user_name_input.strip()
    print("Sin espacios:", clean_user)
    print("En minúsculas:", clean_user.lower())
    print("En mayúsculas:", clean_user.upper())
    print("Formato Título:", clean_user.title())

    # 8. Normalizar el nombre de la primera pieza
    normalized_item_name = first_item["name"].strip().title()
    print("Nombre de pieza normalizado:", normalized_item_name)