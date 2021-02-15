import os

from Core.App import App
from Core.Parser import Parser
from Core.Pinger import Pinger
from Core.Filter import FilterParser, Filter
from Core.PlaylistFormer import PlaylistFormer
from Config import Config

if __name__ == '__main__':
	app = App()

	# register users config file
	app.config.from_object(Config)

	# initialize some consts
	FILTER_FILENAME = os.path.join(app.config['ROOT_DIR'], app.config['PLAYLIST_FILTER_FILE'])
	FILTER_FDATA = open(FILTER_FILENAME, 'r', encoding='utf-8').read()
	# initialize modules
	parser = Parser(app)
	app.register_module(parser)
	filter_parser = FilterParser(FILTER_FDATA)
	app.register_module(filter_parser)
	pinger = Pinger(app)
	app.register_module(pinger)
	ftr = Filter(app)
	app.register_module(ftr)

	playlist_former = PlaylistFormer(app.container).form('playlist.m3u')
