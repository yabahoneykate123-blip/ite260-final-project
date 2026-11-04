# ITE 260 Final Project - CDO Campus Lost & Found Tracker
# Honey Kate C. Yaba (FA2-BSIT1-02) - PHINMA Cagayan de Oro College

items = ["1. PHINMA COC Student ID (Unclaimed)", "2. Scientific Calculator (Unclaimed)"]

while True:
    print("\n--- CDO CAMPUS LOST & FOUND TRACKER ---")
    print("1. View Items  |  2. Report Item  |  3. Exit")
    choice = input("Enter choice (1-3): ")
    if choice == "1":
        for item in items:
            print(item)
    elif choice == "2":
        new_item = input("Enter found item name: ")
        items.append(f"{len(items) + 1}. {new_item} (Unclaimed)")
        print("Item added successfully!")
    elif choice == "3":
        print("Thank you!")
        break
      
