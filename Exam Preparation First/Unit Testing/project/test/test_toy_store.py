from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_correct_initialization(self):
        for key in range(ord("A"), ord("G") + 1):
            self.assertIsNone(self.store.toy_shelf[chr(key)])

        self.assertEqual(7, len(self.store.toy_shelf))

    def test_add_toy_to_not_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("L", "Bakugan")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_that_is_already_on_shelf_raises_exception(self):
        self.store.add_toy('A', 'Bakugan')
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'Bakugan')

        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_to_a_full_shelf_raises_exception(self):
        self.store.add_toy('A', 'Ben10')
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'Bakugan')

        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_successfully_returns_string(self):
        result = self.store.add_toy('A', 'Bakugan')

        self.assertEqual(result, f"Toy:Bakugan placed successfully!")
        self.assertEqual(self.store.toy_shelf['A'], 'Bakugan')

    def test_remove_toy_from_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('L', 'Ben10')

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_non_existing_toy_from_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('B', 'Ben10')

        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_successfully_returns_string(self):
        self.store.add_toy('A', 'Bakugan')
        result = self.store.remove_toy('A', 'Bakugan')

        self.assertEqual(None, self.store.toy_shelf['A'])
        self.assertEqual(result, "Remove toy:Bakugan successfully!")


if __name__ == '__main__':
    main()