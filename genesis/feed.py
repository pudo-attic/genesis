
import re
import feedparser

from common import * 
from util import loadStatistik


def loadModifiedStatistiken():
    d = feedparser.parse(DESTATIS_FEED)
    STAT_ID = re.compile("\d{5}")
    stats = []
    for entry in d.entries:
        match = STAT_ID.search(entry['title'])
        stats.append(int(match.group(0)))
    return list(set(stats))
    
    
def updateLocalFromFeed():
    for statistik in loadModifiedStatistiken():
        loadStatistik(str(statistik))
        yield statistik


if __name__ == '__main__':
    from tabelle import loadTabellenDaten
    for s in updateLocalFromFeed():
        for tabelle in s.get('tabellen', []):
            loadTabellenDaten(tabelle.get('code'))
        