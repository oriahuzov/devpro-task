# The test task for Dev.Pro

This project demonstrates a basic setup for testing product-related functions using pytest.

## Project Structure

The project is organized into the following directories:

- `src/products`: Contains modules related to product operations.
  - `product.py`: Defines the `Product` class.
  - `json_handler.py`: Implements the `JsonHandler` class for reading and writing JSON data.
  - `product_functions.py`: Contains the `ProductFunctions` class with methods for product-related operations.

- `tests`: Contains test modules.
  - `test_product_functions.py`: Test cases for the functions in `product_functions.py`.

- `main.py`: Script to run the tests using pytest.

- `pytest.ini`: Configuration file for pytest.

## How to Run Tests

To run this project, you'll need to have the following Python libraries installed:

- [pytest](https://pypi.org/project/pytest/) (version 6.2.4)
- [pytest-html](https://pypi.org/project/pytest-html/) (version 3.1.1)

### Installation / Running tests / Reporting


```bash
You can install the required libraries using `pip`. Run the following command in your project's virtual environment:

pip install pytest==6.2.4 pytest-html==3.1.1

Execute the tests using the main.py script:

python main.py

View HTML Report:

open report.html  # On Unix/Linux

start report.html  # On Windows
