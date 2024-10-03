from abc import abstractmethod, ABC


class ProductsRepository(ABC):

    @abstractmethod
    def get_products(self):
        pass