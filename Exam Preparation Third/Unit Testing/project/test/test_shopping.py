from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart('Brothers', 10)
        self.other = ShoppingCart('Oazis', 5)

    def test_correct_initialization(self):
        self.assertEqual(self.shopping_cart.shop_name, 'Brothers')
        self.assertEqual(self.shopping_cart.budget, 10)
        self.assertEqual(self.shopping_cart.products, {})

    def test_invalid_shop_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = 'br1others'

        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('Bacon', 200)

        self.assertEqual(str(ve.exception), f"Product Bacon cost too much!")

    def test_add_to_cart_successfully(self):
        result = self.shopping_cart.add_to_cart('Bacon', 2)

        self.assertEqual(self.shopping_cart.products['Bacon'], 2)
        self.assertEqual(result, "Bacon product was successfully added to the cart!")

    def test_remove_from_cart_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart('Cheese')

        self.assertEqual(str(ve.exception), "No product with name Cheese in the cart!")

    def test_remove_from_cart_successfully(self):
        self.shopping_cart.products = {'Bacon': 2, 'Cheese': 3}
        result = self.shopping_cart.remove_from_cart('Bacon')

        self.assertEqual(len(self.shopping_cart.products), 1)
        self.assertEqual(result, "Product Bacon was successfully removed from the cart!")

    def test_add_method(self):
        self.shopping_cart.products['Bacon'] = 2
        self.other.products['Cheese'] = 3

        new_shopping_cart = self.shopping_cart + self.other

        self.assertEqual(new_shopping_cart.shop_name, 'BrothersOazis')
        self.assertEqual(new_shopping_cart.budget, 15)
        self.assertEqual(new_shopping_cart.products, {'Bacon': 2, 'Cheese': 3})

    def test_buy_products_raises_value_error(self):
        self.shopping_cart.products['Bacon'] = 7
        self.shopping_cart.products['Cheese'] = 5

        total_sum = sum(self.shopping_cart.products.values())

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()

        self.assertEqual(str(ve.exception), f"Not enough money to buy the products!"
                                            f" Over budget with {total_sum - self.shopping_cart.budget:.2f}lv!")

    def test_buy_products_successfully(self):
        self.shopping_cart.products['Bacon'] = 2
        self.shopping_cart.products['Cheese'] = 3

        total_sum = sum(self.shopping_cart.products.values())

        result = self.shopping_cart.buy_products()

        self.assertEqual(result, f'Products were successfully bought! Total cost: {total_sum:.2f}lv.')


if __name__ == '__main__':
    main()