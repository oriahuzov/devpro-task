import json

from src.products.product import Product


class JsonHandler:
    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def extract_products(json_data):
        product_list = json_data.get("products", [])
        return [Product(**product_data) for product_data in product_list]

