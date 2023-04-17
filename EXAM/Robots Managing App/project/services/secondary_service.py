from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=15)

    def details(self):
        result = [f'{self.name} Secondary Service:']
        if self.robots:
            result.append(f'Robots: {" ".join(str(r.name) for r in self.robots)}')

        else:
            result.append(f'Robots: none')

        return '\n'.join(result)