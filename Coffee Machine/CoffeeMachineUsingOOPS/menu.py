class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.ingredients = {
            "Water": water,
            "Milk": milk,
            "Coffee": coffee
        }
        
class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
        MenuItem(name = "Latte", water = 200, milk = 150, coffee = 24, cost = 2.5),
        MenuItem(name = "espresso", water = 50, milk = 0, coffee = 18, cost = 1.5),
        MenuItem(name = "Cappuccino", water = 250, milk = 50, coffee = 24, cost = 3),
        ]
        
    def get_items(self):
        """Return all the names of the available menu items."""
        option = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if is exists, otherwise returns None."""
        for item in self.menu:
            if item.name == order_name:
                return items
            print("Sorry, that item is not available right now.")