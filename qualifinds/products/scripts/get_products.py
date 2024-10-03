from dataclasses import dataclass

import requests
import json
import csv

@dataclass
class Product:
    allergens: str
    sku: str
    vegan: str
    kosher: str
    organic: str
    vegetarian: str
    gluten_free: str
    lactose_free: str
    package_quantity: str
    unit_size: str
    net_weight: str

def get_custom_attributes_values():
    url = "https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json"

    response = requests.get(url)
    if response.status_code != 200:
        return None

    json_data = response.json()

    data = []
    for i in json_data.get('allVariants', [{}]):
        attributes_raw = i.get('attributesRaw', [])
        custom_attribute = next(
            (i['value'] for i in attributes_raw if i.get('name') == 'custom_attributes'),
            None
        )


        data.append(json.loads(custom_attribute['es-CR']))

    return data

def json_to_product(json_data):
    allergens = str([i['name'] for i in json_data['allergens']['value']])
    sku = json_data['sku']['value']
    vegan = str(json_data['vegan']['value'])
    kosher = str(json_data['kosher']['value'])
    organic = str(json_data['organic']['value'])
    vegetarian = str(json_data['vegetarian']['value'])
    gluten_free = str(json_data['gluten_free']['value'])
    lactose_free = str(json_data['lactose_free']['value'])
    package_quantity = str(json_data['package_quantity']['value'])
    unit_size = str(json_data['unit_size']['value'])
    net_weight = str(json_data['net_weight']['value'])

    return Product(
        allergens=allergens,
        sku=sku, vegan=vegan,
        kosher=kosher,
        organic=organic,
        vegetarian=vegetarian,
        gluten_free=gluten_free,
        lactose_free=lactose_free,
        package_quantity=package_quantity,
        unit_size=unit_size,
        net_weight=net_weight)

def run():
    values = get_custom_attributes_values()

    with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(
            ['allergens', 'sku', 'vegan', 'kosher', 'organic', 'vegetarian', 'gluten_free', 'lactose_free',
             'package_quantity', 'unit_size', 'net_weight'])

        for i in values:
            product = json_to_product(i)
            writer.writerow([
                product.allergens,
                product.sku,
                product.vegan,
                product.kosher,
                product.organic,
                product.vegetarian,
                product.gluten_free,
                product.lactose_free,
                product.package_quantity,
                product.unit_size,
                product.net_weight
            ])

    print("Archivo CSV creado exitosamente.")
