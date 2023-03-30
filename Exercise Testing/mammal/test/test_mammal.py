from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Ivan", "Cat", "Meow")

    def test_correct_initializing(self):
        self.assertEqual("Ivan", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("Meow", self.mammal.sound)

    def test_if_make_sound_return_correct_msg(self):
        self.assertEqual("Ivan makes Meow", self.mammal.make_sound())

    def test_if_get_kingdom_return_correct_msg(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_if_info_returns_correct_msg(self):
        self.assertEqual("Ivan is of type Cat", self.mammal.info())

if __name__ == '__main__':
    main()