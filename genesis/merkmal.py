
from util import readTablePages, serializeTuples
import simplejson as json 
import codecs
from common import *
from pprint import pprint

MERKMALE_URL = "https://www-genesis.destatis.de/genesis/online?operation=merkmaleVerzeichnis"

def loadMerkmal(merkmal):
    data = makeRechercheService().service.MerkmalsKatalog(ODN_USER, ODN_PASS, merkmal, "code", "*", "Alle", "100", "de", )
    data = serializeTuples(data.merkmalsKatalogEintraege)
    pprint(data)
    for link in data.get('links', []):
        if "Tabellen mit Vorkommen des Merkmals" in link.get('titel'):
            data['tabellen'] = [t for t in loadMerkmalTabellen(link.get('href'))]
    pprint(data)
    
def loadMerkmalTabellen(href):
    for tr in readTablePages(href):
           yield tr.findAll('a')[0].get('id')
    
if __name__ == '__main__':
    loadMerkmal("MONAT") #"VER013")