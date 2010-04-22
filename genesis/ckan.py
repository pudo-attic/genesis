
import simplejson as json 
import codecs
import re
from ckanclient import CkanClient
from common import * 
from statistik import allLocalStatistik


CLEAN_S = re.compile("(KENNUNG|PASSWORT|kennung|passwort)=[^&]*&")
def urlRemoveAuthInfo(url):
    return CLEAN_S.sub("", url)
        
#print "CLEAN", clean_url("https://www-genesis.destatis.de/genesis/online?sequenz=tabelleAufbau&selectionname=12631-0001&KENNUNG=GK105862&PASSWORT=roFl0815&sprache=de")
#print "CLEAN", clean_url("https://www-genesis.destatis.de/genesisWS/services/ExportService_2009?method=ObjektExport&kennung=GK105862&passwort=roFl0815&typ=statistik&namen=12631&format=&umfang=&zusatz=false&sprache=de")

def statistikToPackage(statistik):
    pkg = {}
    pkg['version'] = "0.3"
    pkg['maintainer'] = "Open Data Network / Friedrich Lindenberg"
    pkg['maintainer_email'] = "friedrich@pudo.org"
    pkg['author'] = "Statistisches Bundesamt, Wiesbaden 2010"
    pkg['author_email'] = "genesis-online@destatis.de"
    pkg['license'] = "OKD Compliant::Other (Attribution)" #11
    pkg['groups'] = ["de-statistik", "odn"]
    pkg['tags'] = ["statistik", "destatis", "deutschland"]
    pkg['title'] = stat.get("inhalt")
    pkg['name'] = "destatis-statistik-" + str(stat.get("code"))
    pkg['notes'] = stat.get("langtext")
    pkg['url'] = ""
    
    resources = []
    def link_as_resource(link):
        res = {}
        if link.get('zieltyp') == 'Webservice':
            return 
        detail, data = link.get('titel').split(':', 1)
        detail = re.compile("Deep-Link zu[rm]? ").sub("", detail)
        detail = re.compile(" der (Tabelle|Statistik)").sub("", detail)
        desc = "%s (%s)" % (data, detail)
        desc = desc.replace("\n", " ")
        res['description'] = desc
        res['url'] = urlRemoveAuthInfo(link.get('href'))
        res['format'] = link.get('contenttype').split(";", 1)[0]
        res['hash'] = ''
        resources.append(res)
    
    for link in stat.get('links'):
        if 'Aufbau' in link.get('titel') and not 'Webservice' in link.get('zieltyp'):
            pkg['url'] = urlRemoveAuthInfo(link.get('href'))
        else:
            link_as_resource(link)
    
    for table in stat.get('tabellen'):
        if table.get('abrufbar') == 'true':
            for link in table.get('links'):
                link_as_resource(link)
            
    pkg['resources'] = resources
    return pkg

def submitStatistik(statistik, ckan):
    package = statistikToPackage(statistik)
    print "Submitting", package.get('name'), "..."
    old = ckan.package_entity_get(pkg.get('name'))
    if ckan.last_status != 404:
        ckan.package_entity_put(pkg)
    else:
        ckan.package_register_post(pkg)
    if ckan.last_status != 200:
        print "RET", ckan.last_status, "MSG", ckan.last_body


def submitLocalStatistiken(url=None, api_key=None):
    url = url if url else CKAN_URL
    api_key = api_key if api_key else CKAN_API_KEY
    ckan = CkanClient(base_location=url, api_key=api_key)
    for statistik in allLocalStatistik():
        submitStatistik(statistik)
        