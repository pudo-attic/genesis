
from suds.client import *
from suds import *

# Relevant URLs
R_ExportService_2009 = "https://www-genesis.destatis.de/genesisWS/services/ExportService_2009?wsdl"
R_TestService = "https://www-genesis.destatis.de/genesisWS/services/TestService?wsdl"
R_ExportService = "https://www-genesis.destatis.de/genesisWS/services/ExportService?wsdl"
R_RechercheService = "https://www-genesis.destatis.de/genesisWS/services/RechercheService?wsdl"
R_DownloadService = "https://www-genesis.destatis.de/genesisWS/services/DownloadService?wsdl"
R_RechercheService_2009 = "https://www-genesis.destatis.de/genesisWS/services/RechercheService_2009?wsdl"
R_DownloadService_2009 = "https://www-genesis.destatis.de/genesisWS/services/DownloadService_2009?wsdl"

STAT_INFO_URL = "https://www-genesis.destatis.de/genesis/online?sequenz=statistikInfo&selectionname=%s&sprache=de"
DESTATIS_FEED = "https://www-genesis.destatis.de/genesis/online/news?language=de"

# Reference Login
ODN_USER = u"GK105862"
ODN_PASS = u"roFl0815"
LANG = u"de"

CKAN_API_KEY = "37b5d553-36b7-4f6b-9290-ccbc4aae412f"
CKAN_URL = "http://de.ckan.net/api"

#API_KEY = "c919d7d1-180f-47ae-8338-a10863182d5c"
#URL = "http://ckan.net/api"

testService = None
def makeTestService():
    global testService
    if testService is None:
        testService = Client(R_TestService)
    return testService
    
rechercheService = None
def makeRechercheService():
    global rechercheService
    if rechercheService is None:
        rechercheService = Client(R_RechercheService_2009)
    return rechercheService
    
dlService = None
def makeDownloadService():
    global dlService
    if dlService is None:
        dlService = Client(R_DownloadService_2009, retxml=True)
    return dlService
    
exportService = None
def makeExportService():
    global exportService
    if exportService is None:
        exportService = Client(R_ExportService_2009)
    return exportService