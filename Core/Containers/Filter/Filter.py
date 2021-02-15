class Filter:
    def __init__(self, category: str, instance):
        if category is 'change_group':
            if isinstance(instance, list):
                self.type = category
                self.value = instance
                return
            raise AttributeError('instance param must be dict')
        elif category is 'required':
            if isinstance(instance, str):
                self.type = category
                self.value = instance
                return
            raise AttributeError('instance param must be str')
        elif category is 'groups':
            if isinstance(instance, str):
                self.type = category
                self.value = instance
                return
            raise AttributeError('instance param must be str')
        elif category is 'blacklist':
            if isinstance(instance, str):
                self.type = category
                self.value = instance
                return
            raise AttributeError('instance param must be str')
        else:
            raise AttributeError('Available categories is change_group, required, groups, blacklist')