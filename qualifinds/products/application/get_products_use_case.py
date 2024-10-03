import requests
from bs4 import BeautifulSoup

from products.domain.products_repository import ProductsRepository


class GetProductsUseCase:

    def __init__(self, repository: ProductsRepository):
        self.repository = repository

    def execute(self, url: str):
        return self.repository.get_products()
