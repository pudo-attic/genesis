import codecs
from serialize import serializeTuples
from common import * 

def loadTabellenForStatistik(statistik, with_data=False):
    tabn = makeRechercheService().service.TabellenKatalog(ODN_USER, ODN_PASS, "%s-*" % statistik, 
                                                          "Alle", "100", "de")
    data = []
    if hasattr(tabn.tabellenKatalogEintraege, 'abrufbar'):
        data.append(serializeTuples(tabn.tabellenKatalogEintraege))
    else:
        for t in tabn.tabellenKatalogEintraege:
            data.append(serializeTuples(t))
    if with_data:
        for t in data:
            loadTabellenDaten(t.get('code'))
    return data


def loadTabellenDaten(tabelle):
    print "Loading data for table", tabelle, "..."
    out = makeDownloadService().service.TabellenDownload(ODN_USER, ODN_PASS, tabelle, "All", "datencsv", False, 
                                             False, "1800", "2011", "*", "*", "*", "*", "*", "*", 
                                             "*", "*", "*", False, "", "de")
    boundary = out.split("\r\n")[1]
    parts = out.split(boundary)
    (hdr, csv) = parts[2].split("\r\n\r\n", 1)
    data = unicode(csv.decode('latin-1'))
    writeTabellenDaten(tabelle, data)
    return data


def writeTabellenDaten(tabelle, data):
    outfile = codecs.open("tabellen/%s.csv" % tabelle, 'w', 'utf-8')
    outfile.write(data)
    outfile.close()
    
if __name__ == '__main__':
    from statistik import allLocalStatistik
    for statistik in allLocalStatistik():
        for tabelle in statistik.get('tabellen', []):
            loadTabellenDaten(tabelle.get('code'))
