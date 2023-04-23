import csv


CSV_FILE_PATH = '../src/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = 'Item'
        if self.__check_len(name):
            self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @classmethod
    def __check_len(cls, name):
        return len(name) <= 10

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if self.__check_len(name):
            self.__name = name
        else:
            raise ValueError('Длина наименования товара превышает 10 символов')

    def __repr__(self):
        """Возвращает отладочную информацию об экземпляре класса"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Возвращает пользовательскую информацию об экземпляре класса"""
        return f"{self.name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        Item.all = []
        with open(CSV_FILE_PATH, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(value) -> int:
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(value))
