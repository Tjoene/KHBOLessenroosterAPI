#!/usr/bin/python3
from saveToDb import Lesson
from saveToDb import MysqlDatabase

#needed for reading files
import sys
import os

class LessonData:
    def __init__(self) :
        self.dataList = []
    def add(self,parameter):
        self.dataList.append(parameter)
    def reset(self) :
        for data in self.dataList :
            self.dataList.remove(data)
    def printConsole(self) :
        print('----------------------------')
        for arg in self.dataList :
            print (arg)
    def toString(self) :
        data =  '/'.join(self.dataList)
        #after getting the data remove all unwanted chars LOLZZZ
        data = data.replace(',','')
        data = data.replace('\'','')
        return data

class Roster:
    def __init__(self) :
        self.lessonList = []
        self.bufferlesson = LessonData()
    def add(self,parameter) :
        self.bufferlesson.add(parameter)
    def final(self) :
        self.lessonList.append(self.bufferlesson)
    def reset(self) : 
        self.bufferlesson = LessonData()
    def printConsole(self) :
        for lesson in self.lessonList :
            lesson.printConsole()

from html.parser import HTMLParser

class lessonParser(HTMLParser):
    def resetParams(self) :
        self.roster = Roster()
        self.readData=0 
        self.sortOfData = 0
    def handle_starttag(self, tag, attrs):
        if (tag=='table'):
            self.roster.reset()
        elif tag=='font' and attrs[0][1]=="2" :
            self.readData=1
        else :        
            self.readData=0
    def handle_data(self, data):
        if(self.readData==1): 
            #filter out unneeded information
            output = data.replace('\n','')
            if output !='' :
                self.roster.add(output)
    def handle_endtag(self, tag):
        if (tag=='table'):
            self.roster.final()


def parseLes(html) :
    parserLessenrooster = lessonParser(strict=False) 
    parserLessenrooster.resetParams()
    parserLessenrooster.feed(html)
    return parserLessenrooster.roster

def getDateList (lessonDataList) :
    dates = []
    for i in range(1,6) :
        numbers = lessonDataList[i].dataList[0].split(' ') 
        numbers = numbers[1].split('/')
        dates.append(numbers)
    
    return dates

def saveHTMLToDatabase(rosterHTML,className) :
    roster = parseLes(rosterHTML) 
    dates = getDateList(roster.lessonList)
    listWithLessons = []
    for i in range(1,12) : 
        startIndexData = (6 * i) + 1 
        for j in range(0,5) :    
            if len(roster.lessonList[startIndexData+j].dataList) > 0 :
                listWithLessons.append(Lesson(className,dates[j][1],dates[j][0],str(i),roster.lessonList[startIndexData+j].toString()))
    # save to the database
    db = MysqlDatabase()
    db.saveLessonsToDb(listWithLessons)

def saveFile(filepath) : 
    print('parsing: '+filepath)
    filename = os.path.basename(filepath)
    classname = filename.split('_')[0]
    filepath = str(filepath)
    f = open(filepath,'r')
    lessenroosterHTML = f.read()
    saveHTMLToDatabase(lessenroosterHTML,classname)
    os.remove(filepath)
    f.close()

# make sure command works with multple files
for i in range(1,len(sys.argv)) :
    try :
        saveFile(sys.argv[i])
    except :
        print('error in :'+sys.argv[i])
    


