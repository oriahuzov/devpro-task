import pytest
import logging

from src.products.json_handler import JsonHandler
from src.products.product_functions import ProductFunctions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def sample_json_data():
    return JsonHandler.read_json('src/tests/sample_data.json')


@pytest.fixture
def expected_product_names():
    return ["Pizza", "Sushi", "Burger", "Pad Thai"]


@pytest.fixture
def expected_filtered_products():
    return [{"id": 2, "name": "Sushi", "category": "Japanese", "price": 24.99}]


def test_get_product_names(sample_json_data, expected_product_names):
    logger.info("Running test_get_product_names")
    actual_product_names = ProductFunctions.get_product_names(sample_json_data)
    assert actual_product_names == expected_product_names
    logger.info("Test test_get_product_names passed")


def test_filter_products_by_price(sample_json_data, expected_filtered_products):
    logger.info("Running test_filter_products_by_price")
    actual_filtered_products = ProductFunctions.filter_products_by_price(sample_json_data, 15.0)
    assert actual_filtered_products == expected_filtered_products
    logger.info("Test test_filter_products_by_price passed")
