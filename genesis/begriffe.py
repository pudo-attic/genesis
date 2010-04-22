
from util import readTablePages
import simplejson as json 
import codecs

BEGRIFFE_URL = "https://www-genesis.destatis.de/genesis/online?operation=begriffeVerzeichnis"

def fetchBegriffeText():
    for tr in readTablePages(BEGRIFFE_URL):
        begriff = tr.findAll('a')[0].get('id').encode('utf-8')
        #print begriff.decode('ascii', 'replace')
        yield begriff

def writeAllBegriffe():
    fh = codecs.open("begriffe.js", "w", "utf-8")
    begriffe = [b for b in fetchBegriffeText()]
    fh.write(json.dumps(begriffe))
    fh.close()
    
def allBegriffe():
    fh = codecs.open("begriffe.js", "r", "utf-8")
    begr = json.loads(fh.read())
    fh.close()
    return begr
    

if __name__ == '__main__':
    writeAllBegriffe()