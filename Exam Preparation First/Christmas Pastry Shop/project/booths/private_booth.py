from project.booths.booth import Booth


class PrivateBooth(Booth):
    @property
    def get_price_per_person(self):
        return 3.50

    def reserve(self, number_of_people: int) -> None:
        self.price_for_reservation = self.get_price_per_person * number_of_people
        self.is_reserved = True
        