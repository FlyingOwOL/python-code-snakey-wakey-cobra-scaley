class fridge:

    # freezer and shelves structure
    freezer = {
        'top_compartment': [],
        'bottom_compartment': []
    }
    shelves = {
        'top_shelf': [],
        'middle_shelf': [],
        'bottom_shelf': []
    }

    ''' Attributes
    freezer_temperature : int
    shelve_temperature : int
    '''
    def __init__(self):
        self.freezer_temperature = -18  # Default freezer temperature in Celsius
        self.shelve_temperature = 4     # Default shelf temperature in Celsius
    
    def display_items_in_fridge(self):
        print("Freezer Contents:")
        for compartment, items in self.freezer.items():
            print(f"  {compartment}: {items}")
        print("Shelf Contents:")
        for shelf, items in self.shelves.items():
            print(f"  {shelf}: {items}")

    def put_item_in_freezer(self, item, compartment):
        self.freezer[compartment].append(item)

    def put_item_in_shelf(self, item, shelf):
        self.shelves[shelf].append(item)

    def take_item_from_freezer(self, item, compartment):
        if item in self.freezer[compartment]:
            self.freezer[compartment].remove(item)
            return item
        return None

    def take_item_from_shelf(self, item, shelf):
        if item in self.shelves[shelf]:
            self.shelves[shelf].remove(item)
            return item
        return None

