from .Containers import ChannelContainer

class PlaylistFormer:
	def __init__(self, container: ChannelContainer, filter:list=None):
		self.container = container
		self.filter = list(map(lambda item: item.lower(), filter)) if filter is not None else None

	def form(self):
		with open('playlist.m3u', 'w', encoding='utf-8') as f:
			f.write('#EXTM3U\n\n')
			BLACKLIST = ['Для ForkPlayer']
			for item in self.container:
				if self.filter:
					if item.title.lower() in self.filter:
						if item.group not in BLACKLIST:
							f.write(f'#EXTINF:-1,{item.title.title()}\n')
							f.write(f'#EXTGRP:{item.group}\n')
							if item.vlcopt != '':
								f.write(f'#EXTVLCOPT:{item.vlcopt}\n')
							f.write(f'{item.url}\n\n')
				else:
					if item.group not in BLACKLIST:
						f.write(f'#EXTINF:-1,{item.title.title()}\n')
						f.write(f'#EXTGRP:{item.group}\n')
						if item.vlcopt != '':
							f.write(f'#EXTVLCOPT:{item.vlcopt}\n')
						f.write(f'{item.url}\n\n')