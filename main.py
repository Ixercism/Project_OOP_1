class Category:
    title: str
    description: str
    products: list
    total_category: int
    total_unique: int
    all_categories: list


    def __init__(self, title, description, products, total_category, total_unique):
        self.title = title
        self.description = description
        self.products = products
        self.total_category = total_category
        self.total_unique = total_unique
        self.all_categories = title


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
