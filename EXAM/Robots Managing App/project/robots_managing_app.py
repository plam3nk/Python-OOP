from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {
        'MainService': MainService,
        'SecondaryService': SecondaryService,
    }

    VALID_ROBOT_TYPES = {
        'MaleRobot': MaleRobot,
        'FemaleRobot': FemaleRobot
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(filter(lambda r: r.name == robot_name, self.robots))
        service = next(filter(lambda s: s.name == service_name, self.services))
        if robot.__class__.__name__ == 'MaleRobot' and service.__class__.__name__ == 'SecondaryService':
            return "Unsuitable service."

        if robot.__class__.__name__ == 'FemaleRobot' and service.__class__.__name__ == 'MainService':
            return "Unsuitable service."

        if service.capacity == len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
            service.robots.remove(robot)
            self.robots.append(robot)

            return f"Successfully removed {robot_name} from {service_name}."

        except StopIteration:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        number_fed_robots = 0
        for robot in service.robots:
            robot.eating()
            number_fed_robots += 1

        return f"Robots fed: {number_fed_robots}."

    def service_price(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        price = 0
        for robot in service.robots:
            price += robot.price

        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())

        return '\n'.join(str(x) for x in result)


