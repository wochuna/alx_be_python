def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == '1':
            item = input("Enter item to add on the list: ")
            if item in shopping_list:
                print(f"ERROR.{item} is already in the list.")
            else:
                shopping_list.append(item)
                print(f"{item} has been added to the list.")
            pass
        elif choice == '2':
            item = input("Enter item to remove from the list: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list.")
            else:
                print(f"ERROR.{item} is not in the list or has already been removed.")
            pass
        elif choice == '3':
            print(f"{shopping_list}")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()