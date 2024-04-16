class Category:
    title: str
    description: str
    products: list
    total_category = 0
    total_unique = 0


    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.products = products
        Category.total_category += 1
        Category.total_unique += len(set(self.products))


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
