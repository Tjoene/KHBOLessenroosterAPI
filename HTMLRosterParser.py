#!/usr/bin/python3
# makes a list out of the raw HTML with all the valuable data present in a consistent way
# this will be further worked out by the HTML Roster

from html.parser import HTMLParser

class HTMLRosterParser(HTMLParser):
    def __init__(self) :
        #call the super constructor
        super(HTMLRosterParser,self).__init__()
        self.rosterData = RosterData()
        self.readData=0 
        self.sortOfData = 0
    def handle_starttag(self, tag, attrs):
        if (tag=='table'):
            self.rosterData.reset()
        elif tag=='font' and attrs[0][1]=="2" :
            self.readData=1
        else :        
            self.readData=0
    def handle_data(self, data):
        if(self.readData==1): 
            #filter out unneeded information
            output = data.replace('\n','')
            if output !='' :
                self.rosterData.add(output)
    def handle_endtag(self, tag):
        if (tag=='table'):
            self.rosterData.final()

