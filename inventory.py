import requests


# define Python user-defined exceptions
class NotEnoughQuantity(Exception):
    "Raised when the quantity is less than the amount to decrease"
    pass


class Inventory:
    """
    Inventory class - Sample
    """

    raise_amt = 1.10
    price_rate = 1.30

    def __init__(self, name: str, type: str, cost: float, quantity: int = 0):
        self.name = name
        self.type = type
        self.cost = cost
        self.price = cost * self.price_rate
        self.quantity = quantity

    @property
    def code(self):
        return f'{self.type}-{self.name}'

    @property
    def inventory_total_cost(self):
        return self.cost * self.quantity

    @property
    def inventory_total_price(self):
        return self.price * self.quantity

    def apply_raise(self):
        self.price = round(self.price * self.raise_amt, 2)
    
    def var_quantity(self, how_many):
        self.quantity += how_many
    
    def increment_quantity(self, increment):
        self.var_quantity(increment)

    def decrease_quantity(self, decrease):
        if decrease > self.quantity:
            raise NotEnoughQuantity

        self.var_quantity(-decrease)
        
    def check_system(self):
        response = requests.get(f'https://mysystem.com/{self.code}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'