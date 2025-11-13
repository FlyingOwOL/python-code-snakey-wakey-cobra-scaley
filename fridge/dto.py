from model import fridge as fridge_model

def put_item():
    fridge_instance = fridge_model.fridge()
    location = input("Where do you want to put the item? (freezer/shelf): ").strip().lower()
    item = input("Enter the name of the item to put: ").strip()
    if location == "freezer":
        compartment = input("Which compartment? (top_compartment/bottom_compartment): ").strip().lower()
        fridge_instance.put_item_in_freezer(item, compartment)
        print(f"Item '{item}' added to {compartment} of the freezer.")
    elif location == "shelf":
        shelf = input("Which shelf? (top_shelf/middle_shelf/bottom_shelf): ").strip().lower()
        fridge_instance.put_item_in_shelf(item, shelf)
        print(f"Item '{item}' added to {shelf} of the shelves.")
    else:
        print("Invalid location. Please choose either 'freezer' or 'shelf'.")

def take_item():
    fridge_instance = fridge_model.fridge()
    fridge_instance.display_items_in_fridge()
    location = input("Where do you want to take the item from? (freezer/shelf): ").strip().lower()
    item = input("Enter the name of the item to take: ").strip()
    if location == "freezer":
        compartment = input("Which compartment? (top_compartment/bottom_compartment): ").strip().lower()
        taken_item = fridge_instance.take_item_from_freezer(item, compartment)
        if taken_item:
            print(f"Item '{item}' taken from {compartment} of the freezer.")
        else:
            print(f"Item '{item}' not found in {compartment} of the freezer.")
    elif location == "shelf":
        shelf = input("Which shelf? (top_shelf/middle_shelf/bottom_shelf): ").strip().lower()
        taken_item = fridge_instance.take_item_from_shelf(item, shelf)
        if taken_item:
            print(f"Item '{item}' taken from {shelf} of the shelves.")
        else:
            print(f"Item '{item}' not found in {shelf} of the shelves.")
    else:
        print("Invalid location. Please choose either 'freezer' or 'shelf'.")