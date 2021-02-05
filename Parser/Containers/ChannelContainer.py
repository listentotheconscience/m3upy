from .Channel import Channel
from .ChannelException import ChannelException

class ChannelContainer:
	def __init__(self):
		self.container = []

	def append(self, instance: Channel):
		# try:
		# 	if self.byName(instance.title):
		# 		return
		# except ChannelException:
		self.container.append(instance)

	def last(self):
		return self.container[-1]

	def byIndex(self, index: int) -> Channel:
		return self.container[index]

	def byName(self, name: str) -> Channel:
		for item in self.container:
			if name == item.title:
				return item

		raise ChannelException(f'{name} channel does not exists')

	def byGroup(self, group: str) -> list:
		output = []
		for item in self.container:
			if group == item.group:
				output.append(item)

		return output

	def __iter__(self):
		self.index = -1
		return self

	def __next__(self):
		if self.index < len(self.container) - 1:
			self.index += 1
			return self.byIndex(self.index)
		else:
			raise StopIteration()

	