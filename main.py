class Category:
    title: str
    description: str
    products: list
    total_category = 0
    total_unique = 0

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.__products = products
        Category.total_category += 1
        Category.total_unique += len(set(self.products))

    def __len__(self):
        count_products = 0
        for product in self.__products:
            count_products += product.quantity
        return count_products

    def __str__(self):
        return f'{self.title}, количество продуктов: {len(self)} шт.'

    def adding_product(self, new_product):
        if new_product.quentity == 0:
            raise ValueError('Нельзя складывать товары с нулевым количеством!')
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.total_unique += 1
        else:
            raise TypeError('Нельзя к продукту добавлять лишние объекты')

    @property
    def getting_list_of_product(self):
        updated_product = ''
        for product in self.__products:
            updated_product += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
        return updated_product

    @property
    def products(self):
        return self.__products

    def average(self):
        getting_sum = 0
        try:
            for product in self.__products:
                getting_sum += product.price
            result = getting_sum / len(self.__products)
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
        self.__price = float(price)
        self.quantity = quantity

    def __str__(self):
        return f'{self.title}, {self.price} руб. Остаток: {self.quantity}.'

    def __add__(self, other):
        if self.__class__ == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError('Нельзя складывать продукты разных типов')

    @classmethod
    def creating_product(cls, product_data: dict):
        return cls(**product_data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена введена некорректно')
        elif new_price > self.__price:
            self.__price = new_price
            print('Цена повышена')
        elif new_price < self.__price:
            user_answer = input('Подтвердите понижение цены: y/n ')
            if user_answer == 'y':
                self.__price = new_price
                print('Цена понижена')
