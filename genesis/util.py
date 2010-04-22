
import urllib2, urllib
from BeautifulSoup import BeautifulSoup
import time

def serializeTuples(entry):
    #print "TUPLES", entry
    d = {}
    for k, v in entry:
        if isinstance(v[0], basestring):
            d[k] = u''.join(v)
        else:
            d[k] = [serializeTuples(i) for i in v[0]]
    return d
    
    

def readTablePages(url):
    class Request(urllib2.Request):
        def get_method(self): return 'POST'

    while True:
        ph = urllib2.urlopen(url)
        page = ph.read()
        ph.close()
        if not 'verzeichnis' in page:
            print "Fetch failure, retry in 1 sec."
            time.sleep(1)
            continue
        soup = BeautifulSoup(page)
        table = soup.findAll('table', attrs={'class': 'verzeichnis'})[0]
        rows = table.findAll('tr')
        rows.reverse()
        rows.pop()
        if not len(rows):
            break
        for row in rows: 
            yield row
        if 'blaettern' in page:
            form = soup.findAll('form', attrs={'name': 'blaetternOben'})[0]
            url = Request(form.get('action'), 'forward.x=42&forward.y=23', {}) 
        else: break
