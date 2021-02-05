import requests
import re
from .Containers import ChannelContainer
from .Containers import Channel

class Parser:
	def __init__(self, url: list):
		self.url = url
		self.container = ChannelContainer()
		self._parse()


	def _contents(self) -> str:
		output = ''
		for url in self.url:
			r = requests.get(url)
			output += r.text
		return output


	@property
	def pretty(self):
		return self._contents().split("\n")

	def _parse(self):
		BLACKLIST = [
		 '#EXTGRP:18',
		 'group-title="18"',
		 "#EXTM3U",
		 "#EXTGRP:Украина",
		 '#EXTGRP:Другое',
		 '#EXTGRP:Для ForkPlayer'
		]
		title = group = vlcopt = url = ""
		for item in self.pretty:
			if item in BLACKLIST:
				title = group = vlcopt = url = ""
				continue
			if item.startswith("#EXTINF"):
				if title == "" or group == "" or url == "":
					pass
				else:
					self.container.append(Channel(title, group, vlcopt, url))
					title = group = url = ""
				title = item.split(",")[-1].strip().lower()
				if "group-title" in item:
					group = re.search(r'group-title="[a-zA-Zа-яёА-ЯЁ0-9-+\s.]+"', item)
					if group:
						group = group.group().split('=')[1]
						group = re.sub(r'"', '', group)
	
			if item.startswith("#EXTGRP"):
				group = item.split(":")[-1].strip()


			if item.startswith('#EXTVLCOPT'):
				vlcopt = item.split(":")[-1].strip()

			if item.startswith("http"):
				url = item.strip()

	def test(self):
		# print(self.container.container)
		with open('test.txt', 'w', encoding='utf-8') as f:
			for item in self.container.container:
				f.write(f'Title:{item.title}\nGroup:{item.group}\nVlcopt:{item.vlcopt}\nURL:{item.url}\n\n')

		print(len(self.container.container))

	def write(self):
		with open("playlist.m3u", "w", encoding="utf-8") as f:
			f.write(self.pretty)