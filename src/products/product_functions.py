from src.products.json_handler import JsonHandler


class ProductFunctions:
    @staticmethod
    def get_product_names(json_data):
        products = JsonHandler.extract_products(json_data)
        return [product.name for product in products]

    @staticmethod
    def filter_products_by_price(json_data, threshold):
        products = JsonHandler.extract_products(json_data)
        return [product.__dict__ for product in products if product.price >= threshold]
