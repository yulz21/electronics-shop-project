from src.item import Item


class Phone(Item):
    """
    Класс для наименования товара смартфон в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):

        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим карт у смартфона.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Возвращает отладочную информацию об экземпляре класса"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @classmethod
    def __check_sim_num(cls, number_of_sim):  # Класс-метод, возвращающий True, если количество сим карт больше 0.
        return number_of_sim > 0

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if not self.__check_sim_num(number_of_sim):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = number_of_sim


