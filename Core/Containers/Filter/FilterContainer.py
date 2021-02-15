from Core.Containers.BaseContainer import BaseContainer
from Core.Containers.Filter import Filter


class FilterContainer(BaseContainer):
    def __init__(self):
        super().__init__()

    def append(self, instance, category: str):
        self._container.append(Filter(category, instance))
        return self

    def __str__(self):
        output = ''
        for item in self._container:
            output += f'Type: {item.type} Value: {item.value}\n'

        return output
