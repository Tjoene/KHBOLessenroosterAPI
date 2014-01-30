#!/usr/bin/python

import requests
import os

#lol needed because prog of rosters is retard and uses strange chars LOL 
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

s = requests.Session()
s.get('https://lessenroosters.khbo.be')

url = 'https://idp.kuleuven.be/idp/view/login.htm'
postfields = {"username": str(sys.argv[2]), "password": str(sys.argv[3]),  "remember": "false"}
r = s.post(url,params=postfields)

#after getting the page i get a page
#wich i need to submit
jsRelay = r.text

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    RelayState=''
    SAMLResponse=''
    url=''
    def handle_starttag(self, tag, attrs):
        if tag=="form":
            self.url = attrs[0][1]
        if tag=="input":
            if len(attrs) > 2 :
                if len(attrs[0])> 1 :
                    if attrs[1][1]== 'RelayState' :
                        self.RelayState = attrs[2][1]
                    if attrs[1][1]== 'SAMLResponse' :
                        self.SAMLResponse = attrs[2][1]

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(jsRelay)

#after parsing continue session
postfields = {"RelayState" : parser.RelayState ,"SAMLResponse" : parser.SAMLResponse}
s.post(parser.url,data=postfields)

classes = ["1AI1BO1","1AI1BO2","1AI1BO3","1AI1EI","1AI1EO","1AI1LVA1","1AI1LVA2","1AI1LVA3","1AI1ME1","1AI1ME2","1AI2KOA1","1AI2KOA2","1AI2KOA3","1AI2KOA4","1SIALPEM1","1SIALPEM2","1SIATME","1SIBOBO","1SIBOLM","1SICHKV","1SIEMEN","1SILVEOEO","1SIEOETEN","1SILVEN","1SILVKV","1SILVME","1SIMEKV","1SIMEME","1SIMOKV","1SIMOME","1SITIEO1","1SITIEO2","2AGMLT","2AI1BO1","2AI1BO2","2AI1CC","2AI1EI","2AI1EO","2AI1LA","2AI1LLT1","2AI1LLT2","2AI1LLT3","2AI1LV1","2AI1LV2","2AI1ME1","2AI1ME2","2AI1ME3","2AI2KOA1","2AI2KOA2","2AI2KOA3","2AI2KOA4","2AI2KOBO","2AI2KOEM","2AI2KOEO","2AI2KOKV","3AGMLT","3AI1CC","3AI1EI","3AI1EO","3AI1LA","3AI1LLT1","3AI1LLT2","3AI1LLT3","3AI1MA","3AI1MM","3AI2BB","3AI2BL","3AI2EO","3AI2KV","3AI2MM","4MI2BO","4MI2EI","4MI2EO","4MI2KV","4MI2ML","4MI2MM","4MI2NA","4MI2NE","KAHOSLB","KAHOSLK","KHLimburg","MANAMAAV","MANAMAIKV","POSTG_GLOB_REL","VTIO","1SIMEET"]

print ('saving to: '+sys.argv[1])

for period in range (6,12):
    for classnumber in range (0 , len(classes)) :
        zeroClassnumber = str(classnumber + 1).zfill(5)  
        zeroPeriod = str(period).zfill(2)
        url ='https://lessenroosters.khbo.be/iwt/lesrooster_periode3_sem2/lesrooster/'+zeroPeriod+'/c/c'+zeroClassnumber+'.htm'  
        r= s.get(url)
        # save to a file
        filename = classes[classnumber]+"_"+str(period)
        filepath = os.path.join(sys.argv[1] , filename)
        print (filepath)
        try :
            f = open(filepath , 'w' )
            htmlpage = r.text
            f.write(htmlpage)
            f.close()
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)

# example command to test the script would be
# ./Lessenrooster ./dirtosaveto username passwd
