# Campus Lost & Found Management System
# Using Dictionaries and Functions

items = {}

lost_count = 101
found_count = 201


# Function to display the menu
def display_menu():
    print("\n" + "=" * 48)
    print("       COLLEGE LOST & FOUND SYSTEM")
    print("=" * 48)
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. View Lost Items")
    print("4. View Found Items")
    print("5. Search for an Item")
    print("6. Match Lost and Found Items")
    print("7. Claim Found Item")
    print("8. View Item Details")
    print("9. Delete Item")
    print("10. Exit")


# Function to report a lost or found item
def report_item(item_type):
    global lost_count, found_count

    print(f"\n========== REPORT {item_type.upper()} ITEM ==========")

    student = input("Enter Student Name : ").strip()
    name = input("Enter Item Name    : ").strip()
    location = input("Enter Location     : ").strip()
    date = input("Enter Date         : ").strip()
    description = input("Enter Description  : ").strip()

    if not all([student, name, location, date, description]):
        print("\nAll fields are required!")
        return

    if item_type == "Lost":
        item_id = "L" + str(lost_count)
        lost_count += 1
    else:
        item_id = "F" + str(found_count)
        found_count += 1

    items[item_id] = {
        "id": item_id,
        "name": name,
        "student": student,
        "location": location,
        "date": date,
        "description": description,
        "status": item_type,
        "type": item_type,
        "claimant": ""
    }

    print(f"\n{item_type} item reported successfully!")
    print("Item ID :", item_id)
    print("Status  :", item_type)


# Function to display an item's summary
def display_item(item):
    print("\nItem ID :", item["id"])
    print("Item    :", item["name"])
    print("Student :", item["student"])
    print("Location:", item["location"])
    print("Date    :", item["date"])
    print("Status  :", item["status"])


# Function to view lost or found items
def view_items(item_type):
    print(f"\n========== {item_type.upper()} ITEMS ==========")

    found = False

    for item in items.values():
        if item["type"] == item_type:
            display_item(item)
            found = True

    if not found:
        print("No", item_type.lower(), "items available.")


# Function to search for an item
def search_item():
    print("\n========== SEARCH ITEM ==========")

    search_name = input("Enter Item Name: ").strip().lower()

    if not search_name:
        print("Please enter an item name.")
        return

    found = False

    print("\nSearch Result:")

    for item in items.values():
        if search_name in item["name"].lower():
            display_item(item)
            found = True

    if not found:
        print("No matching items found.")


# Function to match lost and found items
def match_items():
    print("\n========== MATCH LOST & FOUND ITEMS ==========")

    lost_items = [
        item for item in items.values()
        if item["type"] == "Lost"
        and item["status"] == "Lost"
    ]

    found_items = [
        item for item in items.values()
        if item["type"] == "Found"
        and item["status"] == "Found"
    ]

    matched = False

    for lost in lost_items:
        for found in found_items:

            if (
                lost["name"].lower() == found["name"].lower()
                and lost["location"].lower()
                == found["location"].lower()
            ):
                print("\nLost Item ID  :", lost["id"])
                print("Lost Item     :", lost["name"])
                print("Lost Location :", lost["location"])

                print("\nFound Item ID :", found["id"])
                print("Found Item    :", found["name"])
                print("Found Location:", found["location"])

                print("\nPossible Match Found!")
                print("Item Name and Location are matching.")

                choice = input(
                    "\nDo you want to confirm this match? (yes/no): "
                ).strip().lower()

                if choice == "yes":
                    lost["status"] = "Matched"
                    found["status"] = "Matched"

                    print("\nMatch confirmed successfully!")
                    print("Lost Item Status  :", lost["status"])
                    print("Found Item Status :", found["status"])

                matched = True
                break

        if matched:
            break

    if not matched:
        print("No matching lost and found items available.")


# Function to claim a found item
def claim_item():
    print("\n========== CLAIM FOUND ITEM ==========")

    item_id = input("Enter Found Item ID: ").strip().upper()

    if item_id not in items:
        print("\nItem not found!")
        return

    item = items[item_id]

    if item["type"] != "Found":
        print("This is not a found item.")
        return

    if item["status"] == "Claimed":
        print("This item has already been claimed.")
        return

    if item["status"] != "Matched":
        print("Item must be matched before it can be claimed.")
        return

    print("\nItem Found!")
    print("Item     :", item["name"])
    print("Found By :", item["student"])
    print("Location :", item["location"])
    print("Status   :", item["status"])

    claimant = input("\nEnter claimant name: ").strip()

    if not claimant:
        print("Claimant name cannot be empty.")
        return

    item["claimant"] = claimant
    item["status"] = "Claimed"

    # Update the corresponding lost item
    for lost in items.values():
        if (
            lost["type"] == "Lost"
            and lost["status"] == "Matched"
            and lost["name"].lower() == item["name"].lower()
            and lost["location"].lower() == item["location"].lower()
        ):
            lost["status"] = "Claimed"
            break

    print("\nItem successfully claimed!")
    print("Claimant :", claimant)
    print("Item     :", item["name"])
    print("Item ID  :", item["id"])
    print("Status   :", item["status"])


# Function to view complete item details
def view_item_details():
    print("\n========== VIEW ITEM DETAILS ==========")

    item_id = input("Enter Item ID: ").strip().upper()

    if item_id not in items:
        print("\nItem not found!")
        return

    item = items[item_id]

    print("\nItem Details")
    print("-" * 35)
    print("Item ID     :", item["id"])
    print("Item Name   :", item["name"])
    print("Student     :", item["student"])
    print("Location    :", item["location"])
    print("Date        :", item["date"])
    print("Description :", item["description"])
    print("Status      :", item["status"])

    if item["claimant"]:
        print("Claimant    :", item["claimant"])

    print("-" * 35)


# Function to delete an item
def delete_item():
    print("\n========== DELETE ITEM ==========")

    item_id = input("Enter Item ID: ").strip().upper()

    if item_id not in items:
        print("\nItem not found!")
        return

    item = items[item_id]

    print("\nItem Found!")
    print("Item    :", item["name"])
    print("Student :", item["student"])
    print("Status  :", item["status"])

    choice = input(
        "\nAre you sure you want to delete this item? (yes/no): "
    ).strip().lower()

    if choice == "yes":
        del items[item_id]
        print("\nItem deleted successfully!")
    else:
        print("Deletion cancelled.")


# Main function
def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            report_item("Lost")

        elif choice == "2":
            report_item("Found")

        elif choice == "3":
            view_items("Lost")

        elif choice == "4":
            view_items("Found")

        elif choice == "5":
            search_item()

        elif choice == "6":
            match_items()

        elif choice == "7":
            claim_item()

        elif choice == "8":
            view_item_details()

        elif choice == "9":
            delete_item()

        elif choice == "10":
            print("\n" + "=" * 48)
            print("       THANK YOU FOR USING")
            print("       COLLEGE LOST & FOUND SYSTEM")
            print("=" * 48)
            break

        else:
            print("\nInvalid choice! Please enter 1 to 10.")


# Start the program
if __name__ == "__main__":
    main()