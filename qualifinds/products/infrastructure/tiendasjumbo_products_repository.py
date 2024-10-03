import requests
from bs4 import BeautifulSoup

from products.domain.products_repository import ProductsRepository


class TiendasJumboProductsRepository(ProductsRepository):

    def __init__(self, url: str):
        self.url = url

    def get_products(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            sections = soup.find_all('article', class_='vtex-product-summary-2-x-element')
            products = []
            for section in sections:
                name = section.find('h3').get_text().strip()
                price = section.find(class_='tiendasjumboqaio-jumbo-minicart-2-x-pp_container').get_text()
                price_without_discount = section.find(
                    class_='tiendasjumboqaio-jumbo-minicart-2-x-cencoPriceWithoutDiscount')

                if price_without_discount:
                    product_data = {
                        'name': name,
                        'promo_price': price.replace('\xa0', ' ').strip(),
                        'price': price_without_discount.get_text().replace('\xa0', ' ').strip()
                    }
                else:
                    product_data = {
                        'name': name,
                        'price': price.replace('\xa0', ' ').strip(),
                    }

                products.append(product_data)

            return products
        return []
