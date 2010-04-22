import codecs
import simplejson as json 
from pprint import pprint
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
from common import * 
from util import serializeTuples
from glob import glob

def allLocalStatistik():
    for file in glob("statistiken/*.js"):
        fh = codecs.open(file, 'r', 'utf-8')
        stat = json.loads(fh.read())
        yield stat
        fh.close()

def loadStatistikLangtext(statistik):
    url = STAT_INFO_URL % statistik
    soup = BeautifulSoup(urlopen(url))
    texte = soup.findAll(attrs={'class': 'langtext'})
    text = u'\n'.join([t.contents[0] if len(t.contents) else '\n' for t in texte])
    return text
    
#loadStatistikLangtext("12612")

def loadAllStatistik():
    # TODO Load EVAS registry instead.
    # https://erhebungsdatenbank.destatis.de/eid/Tabelle.html?filterStatus=freigegebenegesperrteEIDs&tabellenName=TabelleEvas&chooseFilterEvas=AlleEvas
    for i in range(00000, 99999):
        statistik = "%05d" % i
        loadStatistik(statistik)


def writeStatistik(statistik, data):
    outfile = codecs.open("statistiken/%s.js" % statistik, 'w', 'utf-8')
    outfile.write(json.dumps(data))
    outfile.close()


def loadStatistik(statistik):
    from tabelle import loadTabellenForStatistik
    print "Load Statistik", statistik, "..."
    stat = makeRechercheService().service.StatistikKatalog(ODN_USER, ODN_PASS, statistik, "", "100", "de")
    try:
        d = serializeTuples(stat.statistikKatalogEintraege)
        d['tabellen'] = loadTabellenForStatistik(statistik)
        d['langtext'] = loadStatistikLangtext(statistik)
        writeStatistik(statistik, d)
        return d
    except AttributeError, ae:
        print "ERR", ae
        return 
    
if __name__ == '__main__':
    loadAllStatistik()