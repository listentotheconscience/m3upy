from Core.Containers.Filter.FilterContainer import FilterContainer


class FilterParser:
    def __init__(self, fdata: str):
        self.fdata = fdata
        self.__container = FilterContainer()
        self.category = None
        self.__parse()

    @property
    def container(self) -> FilterContainer:
        return self.__container

    def __parse(self):
        data = self.fdata.split("\n")
        for line in data:
            if line.startswith("CHANGE_GROUP:"):
                self.category = 'change_group'
                continue
            elif line.startswith('REQUIRED:'):
                self.category = 'required'
                continue
            elif line.startswith('GROUPS'):
                self.category = 'groups'
                continue
            elif line.startswith('BLACKLIST:'):
                self.category = 'blacklist'
                continue

            if self.category == 'change_group':
                if '=>' in line:
                    line = line.strip().split('=>')
                    channel = line[0].strip()
                    group = line[1].strip()
                    self.__container.append([channel, group], self.category)
                else:
                    continue
            elif self.category in ('required', 'groups', 'blacklist'):
                line = line.strip().split(',')
                if len(line) >= 1:
                    for item in line:
                        self.__container.append(item.strip(), self.category)
                else:
                    continue
