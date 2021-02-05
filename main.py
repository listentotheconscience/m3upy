from Parser import Parser
from Parser import PlaylistFormer

if __name__ == '__main__':
	p = Parser([
		"https://webhalpme.ru/dlis/m.php?p=9216655",
		"https://iptvm3u.ru/listru.m3u",
		"http://iptvbarmen.tk/auto.nogrp.m3u",
		"https://iptvm3u.ru/onelist.m3u",
		"https://iptvm3u.ru/hdlist.m3u",
		"https://smarttvnews.ru/apps/freeiptv.m3u",
		])
	# p.test()
	pf = PlaylistFormer(p.container)#, filter=['Discovery Science', 'Охота и рыбалка'])
	pf.form()