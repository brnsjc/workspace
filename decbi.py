import bencoder,json
from pprint import pprint

f = open("Gemini Man (2019) [WEBRip] [720p] [YTS.LT].torrent", "rb")
d = bencoder.decode(f.read())

pprint(d)