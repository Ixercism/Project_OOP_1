class Category:
    title: str
    description: str
    products: list


    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.products = products
        self.total_category = 0
        self.total_unique = 0


class Product:
    title: str
    description: str
    price: float
    quantity: int


    def __init__(self, title, description, price, quantity):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
