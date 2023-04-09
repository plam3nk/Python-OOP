from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred,
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int) -> str:
        try:
            horse = next(filter(lambda h: h.name == horse_name, self.horses))

            raise Exception(f"Horse {horse_name} has been already added!")

        except StopIteration:
            if horse_type in self.VALID_HORSE_TYPES:
                horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
                self.horses.append(horse)

                return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int) -> str:
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

            raise Exception(f"Jockey {jockey_name} has been already added!")

        except StopIteration:
            self.jockeys.append(Jockey(jockey_name, age))

            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str) -> str:
        try:
            horse_race = next(filter(lambda hr: hr.race_type == race_type, self.horse_races))

            raise Exception(f"Race {race_type} has been already created!")

        except StopIteration:
            self.horse_races.append(HorseRace(race_type))

            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = list(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, self.horses))[-1]

        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            horse_race = next(filter(lambda hr: hr.race_type == race_type, self.horse_races))

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            horse_race = next(filter(lambda hr: hr.race_type == race_type, self.horse_races))

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if 2 > len(horse_race.jockeys):
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = max(horse_race.jockeys, key=lambda jockey: jockey.horse.speed)
        return f"The winner of the {race_type} race, with a speed of" \
               f" {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."


