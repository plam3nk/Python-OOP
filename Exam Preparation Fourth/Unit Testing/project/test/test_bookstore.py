from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookStore(TestCase):

    def setUp(self) -> None:
        self.store = Bookstore(2)

    def test_correct_initialization(self):
        self.assertEqual(self.store.books_limit, 2)
        self.assertEqual(self.store.availability_in_store_by_book_titles, {})
        self.assertEqual(self.store.total_sold_books, 0)

    def test_books_limit_equal_or_below_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test_len_method(self):
        self.store.availability_in_store_by_book_titles = {'Book': 1}
        self.assertEqual(len(self.store), 1)

    def test_receive_book_if_there_is_not_enough_space_in_bookstore_raises_exception(self):
        self.store.availability_in_store_by_book_titles = {'Example': 2}

        with self.assertRaises(Exception) as ex:
            self.store.receive_book('Book', 1)

        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_with_enough_space_in_bookstore_returns_string(self):
        result = self.store.receive_book('Book', 2)

        self.assertEqual(self.store.availability_in_store_by_book_titles, {'Book': 2})
        self.assertEqual(result, "2 copies of Book are available in the bookstore.")

    def test_sell_book_that_is_not_available_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Book', 1)

        self.assertEqual(str(ex.exception), "Book Book doesn't exist!")

    def test_sell_book_not_enough_copies_raises_exception(self):
        self.store.availability_in_store_by_book_titles = {'Book': 1}

        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Book', 2)

        self.assertEqual(str(ex.exception), f"Book has not enough copies to sell. Left: 1")

    def test_sell_book_successfully_returns_string(self):
        self.store.availability_in_store_by_book_titles = {'Book': 2}
        result = self.store.sell_book('Book', 1)

        self.assertEqual(self.store.availability_in_store_by_book_titles, {'Book': 1})
        self.assertEqual(self.store.total_sold_books, 1)
        self.assertEqual(result, "Sold 1 copies of Book")

    def test_str_method(self):
        self.store.availability_in_store_by_book_titles = {'Book': 2}
        self.store.sell_book('Book', 1)

        string = ['Total sold books: 1', 'Current availability: 1', ' - Book: 1 copies']

        self.assertEqual(str(self.store), '\n'.join(string))


if __name__ == '__main__':
    main()