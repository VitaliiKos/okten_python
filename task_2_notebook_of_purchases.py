# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

import json


def display_all_items(items):
    print(f"{'ID':5} {'Name':20} {'Price'}")
    for item in items:
        print(f"{str(item['id']) :<5} {item['name'] :<20} {item['price']:<10}")


def add_purchase(items):
    if not items:
        purchase_id = 1
    else:
        purchase_id = items[-1]['id'] + 1
    purchase_name = input("Enter the title: ")
    price = float(input("Enter the price: "))
    purchase_item = {"id": purchase_id, "name": purchase_name, "price": price}
    items.append(purchase_item)
    save_file(items)
    print("A purchase has been added.")


def search_purchase_items(items):
    search_params = input("Enter your search query: ")
    result = [item for item in items if search_params.lower() in json.dumps(item).lower()]
    print(result)
    if result:
        display_all_items(result)
    else:
        print("The purchases not found.")


def delete_purchase(items):
    search_params = input("Enter the id or name or price of the purchase you want to delete: ")
    result = [item for item in items if search_params.lower() in json.dumps(item).lower()]
    if result:
        items.remove(result[0])
        save_file(items)
        print("The purchase has been removed.")
    else:
        print("The purchases not found.")


def show_most_expensive_item(items):
    if not items:
        print("The purchases not found.")
        return
    most_expensive_item = max(items, key=lambda x: x["price"])
    print(f"{'ID':5} {'Name':20} {'Price'}")
    print(f'{most_expensive_item["id"]:<5} {most_expensive_item["name"]:<20} {most_expensive_item["price"]:<10}')


def load_file():
    try:
        with open("purchases_note.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_file(items):
    with open("purchases_note.json", "w") as file:
        json.dump(items, file)


def main():
    items = load_file()
    while True:
        print("\n--- PURCHASES NOTE BOOK ---")
        print("1. Show all purchases")
        print("2. Add purchase")
        print("3. Search for purchases")
        print("4. Show the most expensive purchase")
        print("5. Remove purchase")
        print("6. Exit")
        choice = input("Your choice: ")
        if choice == "1":
            display_all_items(items)
        elif choice == "2":
            add_purchase(items)
        elif choice == "3":
            search_purchase_items(items)
        elif choice == "4":
            show_most_expensive_item(items)
        elif choice == "5":
            delete_purchase(items)
        elif choice == "6":
            break
        else:
            print("Incorrect choice. Try again.")


if __name__ == '__main__':
    main()
