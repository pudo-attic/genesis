import codecs

from suds.client import Client
from suds import WebFault



# Relevant URLs
R_ExportService_2009 = "https://www-genesis.destatis.de/genesisWS/services/ExportService_2009?wsdl"
R_TestService = "https://www-genesis.destatis.de/genesisWS/services/TestService?wsdl"
R_ExportService = "https://www-genesis.destatis.de/genesisWS/services/ExportService?wsdl"
R_RechercheService = "https://www-genesis.destatis.de/genesisWS/services/RechercheService?wsdl"
R_DownloadService = "https://www-genesis.destatis.de/genesisWS/services/DownloadService?wsdl"
R_RechercheService_2009 = "https://www-genesis.destatis.de/genesisWS/services/RechercheService_2009?wsdl"
R_DownloadService_2009 = "https://www-genesis.destatis.de/genesisWS/services/DownloadService_2009?wsdl"

# Reference Login
ODN_USER = u"GK105862"
ODN_PASS = u"roFl0815"
LANG = u"de"

testService = Client(R_TestService)
rechercheService = Client(R_RechercheService_2009)
dlService = Client(R_DownloadService_2009, retxml=True)
exportService = Client(R_ExportService_2009)

# dlService
#            DiagrammDownload(xs:string kennung, xs:string passwort, xs:string name, xs:string bereich, xs:string format, xs:byte diagrammTyp, xs:boolean zeichnePunkte, xs:byte zoom, xs:boolean wertefokus, xs:string startjahr, xs:string endjahr, xs:string zeitscheiben, xs:string regionalmerkmal, xs:string regionalschluessel, xs:string sachmerkmal, xs:string sachschluessel, xs:string sachmerkmal2, xs:string sachschluessel2, xs:string sachmerkmal3, xs:string sachschluessel3, xs:boolean auftrag, xs:string stand, xs:string sprache, )
#            ErgebnisDiagrammDownload(xs:string kennung, xs:string passwort, xs:string name, xs:string bereich, xs:string format, xs:byte diagrammTyp, xs:boolean zeichnePunkte, xs:byte zoom, xs:boolean wertefokus, xs:string sprache, )
#            ErgebnisDownload(xs:string kennung, xs:string passwort, xs:string name, xs:string bereich, xs:string format, xs:boolean komprimieren, xs:string sprache, )
#            ErgebnisKarteDownload(xs:string kennung, xs:string passwort, xs:string name, xs:string bereich, xs:boolean gitternetz, xs:byte klassenanzahl, xs:byte klasseneinteilung, xs:byte reihenauswahl, xs:string sprache, )
#            ExcelDownload(xs:string kennung, xs:string passwort, xs:string name, xs:string bereich, xs:boolean komprimieren, xs:boolean transponieren, xs:string startjahr, xs:string endjahr, xs:string zeitscheiben, xs:string regionalmerkmal, xs:string regionalschluessel, xs:string sachmerkmal, xs:string sachschluessel, xs:string sachmerkmal2, xs:string sachschluessel2, xs:string sachmerkmal3, xs:string sachschluessel3, xs:boolean auftrag, xs:string stand, xs:string sprache, )
#            KarteDownload(xs:string kennung, xs:string passwort, xs:string name, xs:string bereich, xs:boolean gitternetz, xs:byte klassenanzahl, xs:byte klasseneinteilung, xs:byte reihenauswahl, xs:string regionalmerkmal, xs:string regionalschluessel, xs:boolean auftrag, xs:string stand, xs:string sprache, )
#            TabellenDownload(xs:string kennung, xs:string passwort, xs:string name, xs:string bereich, xs:string format, xs:boolean komprimieren, xs:boolean transponieren, xs:string startjahr, xs:string endjahr, xs:string zeitscheiben, xs:string regionalmerkmal, xs:string regionalschluessel, xs:string sachmerkmal, xs:string sachschluessel, xs:string sachmerkmal2, xs:string sachschluessel2, xs:string sachmerkmal3, xs:string sachschluessel3, xs:boolean auftrag, xs:string stand, xs:string sprache, )
#            ZeitreihenDownload(xs:string kennung, xs:string passwort, xs:string name, xs:string bereich, xs:string format, xs:boolean komprimieren, xs:boolean transponieren, xs:string startjahr, xs:string endjahr, xs:string zeitscheiben, xs:string regionalmerkmal, xs:string regionalschluessel, xs:string sachmerkmal, xs:string sachschluessel, xs:string sachmerkmal2, xs:string sachschluessel2, xs:string sachmerkmal3, xs:string sachschluessel3, xs:boolean auftrag, xs:string stand, xs:string sprache, )
    
#"21311-0004"	Studierende: Deutschland, Semester, Nationalitaet,
#Geschlecht, Angestrebte Abschlusspruefung
#Available time period:	WS 1998/99-WS 2008/09   

#stat = "51000-0001"
#out = dlService.service.TabellenDownload(ODN_USER, ODN_PASS, stat, "All", "xls", False, 
#                                         False, "1800", "2011", "*", "*", "*", "*", "*", "*", "*", "*", "*", False, "", "de")
#print "OUT", out
#boundary = out.split("\r\n")[1]
#parts = out.split(boundary)
#(hdr, csv) = parts[2].split("\r\n\r\n", 1)
#fh = codecs.open('tab-%s.xls' % stat, 'w', 'utf-8')
#fh.write(csv.decode('latin-1'))
#fh.close()
#s1, s2, s3, s4, s5, b6, b7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, b19, s20, s21,                                          
  
 
 
# rechercheService   
#            AuftraegeKatalog(xs:string kennung, xs:string passwort, xs:string listenLaenge, xs:string sprache, )
#            BegriffeKatalog(xs:string kennung, xs:string passwort, xs:string filter, xs:string listenLaenge, xs:string sprache, )
#            DatenKatalog(xs:string kennung, xs:string passwort, xs:string filter, xs:string bereich, xs:string listenLaenge, xs:string sprache, )
#            ErgebnisKatalog(xs:string kennung, xs:string passwort, xs:string filter, xs:string bereich, xs:string listenLaenge, xs:string sprache, )
#            MerkmalAuspraegungenKatalog(xs:string kennung, xs:string passwort, xs:string name, xs:string auswahl, xs:string bereich, xs:string listenLaenge, xs:string sprache, )
#            MerkmalsKatalog(xs:string kennung, xs:string passwort, xs:string filter, xs:string kriterium, xs:string typ, xs:string bereich, xs:string listenLaenge, xs:string sprache, )
#            Recherche(xs:string luceneString, xs:string kennung, xs:string passwort, xs:string listenLaenge, xs:string sprache, xs:string kategorie, )
#            StatistikKatalog(xs:string kennung, xs:string passwort, xs:string filter, xs:string kriterium, xs:string listenLaenge, xs:string sprache, )
#            TabellenKatalog(xs:string kennung, xs:string passwort, xs:string filter, xs:string bereich, xs:string listenLaenge, xs:string sprache, )
#            ZeitreihenKatalog(xs:string kennung, xs:string passwort, xs:string filter, xs:string bereich, xs:string listenLaenge, xs:string sprache, )

#for range(10000, 99999):

#rec = rechercheService.service.BegriffeKatalog(ODN_USER, ODN_PASS, "11111", "100", "de", )
#print rec

#  
rec = rechercheService.service.MerkmalsKatalog(ODN_USER, ODN_PASS, "VER013", "code", "*", "Alle", "100", "de", )
print rec

    
    
#[tr for tr in read_pages('https://www-genesis.destatis.de/genesis/online?sequenz=suche&option=statistiken&selectionname=Jahre')]
        
    

#print "------------------------------------------------"
#rec = rechercheService.service.TabellenKatalog(ODN_USER, ODN_PASS, "12612-*", "Alle", "100", "de")
#rec = rechercheService.service.TabellenKatalog(ODN_USER, ODN_PASS, "*", "Alle", "100-120", "de")
#print len(rec.tabellenKatalogEintraege)
#print dir(rec.tabellenKatalogEintraege[0])
#print dir(rec.tabellenKatalogEintraege)


#rec = rechercheService.service.StatistikKatalog(ODN_USER, ODN_PASS, "00001", "", "100", "de")
#print rec
#print dir(rec)

#for i in range(0, 999):
#    x = "%05d" % i
#    print x

#rec = rechercheService.service.BegriffeKatalog(ODN_USER, ODN_PASS, "VER013", "100", "de")
#print rec

#rec = rechercheService.service.DatenKatalog(ODN_USER, ODN_PASS, "12612", "Alle", "1000", "de")
#print rec
# Keine Berechtigung !

#rec = exportService.service.ObjektExport(ODN_USER, ODN_PASS, "statistik", "12612", "", "", False, "de", )
#print rec

#print exportService
#DatenExport(xs:string kennung, xs:string passwort, xs:string namen, xs:string bereich, xs:string format, xs:boolean werte, xs:boolean metadaten, xs:boolean zusatz, xs:string startjahr, xs:string endjahr, xs:string zeitscheiben, xs:string regionalmerkmal, xs:string regionalschluessel, xs:string sachmerkmal, xs:string sachschluessel, xs:string sachmerkmal2, xs:string sachschluessel2, xs:string sachmerkmal3, xs:string sachschluessel3, xs:string stand, xs:string sprache, )
#ErgebnisExport(xs:string kennung, xs:string passwort, xs:string name, xs:string bereich, xs:string format, xs:boolean komprimieren, xs:string sprache, )
#ObjektExport(xs:string kennung, xs:string passwort, xs:string typ, xs:string namen, xs:string format, xs:string umfang, xs:boolean zusatz, xs:string sprache, )
#TabellenExport(xs:string kennung, xs:string passwort, xs:string namen, xs:string bereich, xs:string format, xs:boolean strukturinformation, xs:boolean komprimieren, xs:boolean transponieren, xs:string startjahr, xs:string endjahr, xs:string zeitscheiben, xs:string regionalmerkmal, xs:string regionalschluessel, xs:string sachmerkmal, xs:string sachschluessel, xs:string sachmerkmal2, xs:string sachschluessel2, xs:string sachmerkmal3, xs:string sachschluessel3, xs:string stand, xs:boolean auftrag, xs:string sprache, )
#ZeitreihenExport(xs:string kennung, xs:string passwort, xs:string namen, xs:string bereich, xs:string format, xs:boolean strukturinformation, xs:boolean komprimieren, xs:boolean transponieren, xs:string startjahr, xs:string endjahr, xs:string zeitscheiben, xs:string regionalmerkmal, xs:string regionalschluessel, xs:string sachmerkmal, xs:string sachschluessel, xs:string sachmerkmal2, xs:string sachschluessel2, xs:string sachmerkmal3, xs:string sachschluessel3, xs:string stand, xs:boolean auftrag, xs:string sprache, )
