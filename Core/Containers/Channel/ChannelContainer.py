from Core.Containers.Channel import Channel
from Core.Containers.Channel.exceptions import ChannelException
from Core.Containers import BaseContainer


class ChannelContainer(BaseContainer):
	def __init__(self):
		super().__init__()

	def append(self, instance: Channel):
		self._container.append(instance)

	def by_name(self, name: str) -> Channel:
		for item in self._container:
			if name == item.title:
				return item

		raise ChannelException(f'{name} channel does not exists')

	def by_group(self, group: str) -> list:
		output = []
		for item in self._container:
			if group == item.group:
				output.append(item)
		return output

	def by_name_list(self, name) -> list:
		output = []
		for item in self._container:
			if name == item.title:
				output.append(item)
		return output

	def update(self, title, by, value):
		for index, item in enumerate(self._container):
			if title.lower() == item.title.lower():
				if by == "title":
					self._container[index].title = value
				elif by == "group":
					self._container[index].group = value
				elif by == "url":
					self._container[index].url = value

	def __str__(self):
		output = ""
		for item in self._container:
			output += f'Title: {item.title}\n'
			output += f'Group: {item.group}\n'
			if item.vlcopt != '':
				output += f'Vlcopt: {item.vlcopt}\n'
			output += f'URL: {item.url}\n\n'
		return output