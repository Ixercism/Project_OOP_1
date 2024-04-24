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

    def __len__(self):
        count_products = 0
        for product in self.products:
            count_products += product.quantity
        return count_products

    def __str__(self):
        return f'{self.title}, количество продуктов: {len(self)} шт.'

    def adding_product(self, new_product):
        if new_product.quentity == 0:
            raise ValueError('Нельзя складывать товары с нулевым количеством!')
        if isinstance(new_product, Product):
            self.products.append(new_product)
            Category.total_unique += 1
        else:
            raise TypeError('Нельзя к продукту добавлять лишние объекты')

    @property
    def getting_list_of_product(self):
        updated_product = ''
        for product in self.products:
            updated_product += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
        return updated_product

    @property
    def products(self):
        return self.products

    def average(self):
        getting_sum = 0
        try:
            for product in self.products:
                getting_sum += product.price
            result = getting_sum / len(self.products)
            return result
        except ZeroDivisionError:
            return 0


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

    def __str__(self):
        return f'{self.title}, {self.price} руб. Остаток: {self.quantity}.'

    def __add__(self, other):
        if self.__class__ == type(other):
            return self.price * self.quantity + other.__price * other.quantity
        raise TypeError('Нельзя складывать продукты разных типов')

    @classmethod
    def creating_product(cls, product_data: dict):
        return cls(**product_data)
