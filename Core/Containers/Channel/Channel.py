from dataclasses import dataclass


@dataclass
class Channel:
	title: str
	group: str
	vlcopt: str
	url: str
