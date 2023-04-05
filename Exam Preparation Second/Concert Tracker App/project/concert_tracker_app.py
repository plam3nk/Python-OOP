from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        musician = [m for m in self.musicians if m.name == name]
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        if musician:
            raise Exception(f"{name} is already a musician!")

        musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = [b for b in self.bands if b.name == name]

        if band:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = [c for c in self.concerts if c.place == place]

        if concert:
            raise Exception(f"{place} is already registered for {genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = [m for m in self.musicians if m.name == musician_name][0]
        band = [b for b in self.bands if b.name == band_name][0]

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        musician = [m for m in band.members if m.name == musician_name][0]

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]

        singers = [m for m in band.members if isinstance(m, Singer)]
        drummers = [m for m in band.members if isinstance(m, Drummer)]
        guitarists = [m for m in band.members if isinstance(m, Guitarist)]

        if not (singers and drummers and guitarists):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        can_play_concert = True

        for singer in singers:
            if concert.genre == 'Rock':
                if "sing high pitch notes" not in singer.skills:
                    can_play_concert = False
            elif concert.genre == 'Metal':
                if "sing low pitch notes" not in singer.skills:
                    can_play_concert = False
            elif concert.genre == 'Jazz':
                if ("sing high pitch notes " and "sing low pitch notes") not in singer.skills:
                    can_play_concert = False

        for drummer in drummers:
            if concert.genre == 'Rock':
                if "play the drums with drumsticks" not in drummer.skills:
                    can_play_concert = False
            elif concert.genre == 'Metal':
                if "play the drums with drumsticks" not in drummer.skills:
                    can_play_concert = False
            elif concert.genre == 'Jazz':
                if "play the drums with drum brushes" not in drummer.skills:
                    can_play_concert = False

        for guitarist in guitarists:
            if concert.genre == 'Rock':
                if "play rock" not in guitarist.skills:
                    can_play_concert = False
            elif concert.genre == 'Metal':
                if "play metal" not in guitarist.skills:
                    can_play_concert = False
            elif concert.genre == 'Jazz':
                if "play jazz" not in guitarist.skills:
                    can_play_concert = False

        if not can_play_concert:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        else:
            profit = (concert.audience * concert.ticket_price) - concert.expenses

            return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
