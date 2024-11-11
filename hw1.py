class ItemManager:
    def __init__(self):
        self.items = []

    def add_item(self, name, description, contact_info):
        self.items.append({
            'name': name,
            'description': description,
            'contact_info': contact_info
        })
        print(f"Item '{name}' added successfully.")

    def delete_item(self, name):
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                print(f"Item '{name}' deleted successfully.")
                return
        print(f"Item '{name}' not found.")

    def display_items(self):
        if not self.items:
            print("No items to display.")
            return
        for item in self.items:
            print(f"Name: {item['name']}, Description: {item['description']}, Contact Info: {item['contact_info']}")

    def find_item(self, name):
        for item in self.items:
            if item['name'] == name:
                print(f"Item found: Name: {item['name']}, Description: {item['description']}, Contact Info: {item['contact_info']}")
                return
        print(f"Item '{name}' not found.")

def main():
    manager = ItemManager()
    while True:
        print("\nCommands: add, delete, display, find, exit")
        command = input("Enter command: ").strip().lower()

        if command == "exit":
            print("Exiting the program.")
            break
        elif command == "add":
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            contact_info = input("Enter contact info: ")
            manager.add_item(name, description, contact_info)
        elif command == "delete":
            name = input("Enter item name to delete: ")
            manager.delete_item(name)
        elif command == "display":
            manager.display_items()
        elif command == "find":
            name = input("Enter item name to find: ")
            manager.find_item(name)
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()