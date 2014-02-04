#!/usr/bin/python3
# the roster contains the data from the RosterData object by using the 
# roster extracter to extraxt the information and put it into a easy to understand form

from saveToDb import Lesson
from saveToDb import MysqlDatabase

import os

class Roster :
    def __init__(self,path) :
        self.HTMLpage = self.getFile(path)
    def getFile(self,path) :
        print('opening: '+path)
        # get the class name
        filename = os.path.basename(path)
        self.classname = filename.split('_')[0]
        # open a filestream to read the data
        f = open(str(filepath),'r')
        HTML = f.read()
        f.close()
        return HTML
        #self.saveHTMLToDatabase(lessenroosterHTML,classname)
    def saveToDb(self) :
        roster = self.parseLesson(rosterHTML) 
        dates = self.getDateList(roster.lessonList)
        listWithLessons = []
        for i in range(1,12) : 
           startIndexData = (6 * i) + 1 
           for j in range(0,5) :    
                if len(roster.lessonList[startIndexData+j].dataList) > 0 :
                    listWithLessons.append(Lesson(self.className,dates[j][1],dates[j][0],str(i),roster.lessonList[startIndexData+j].toString()))

    #    # save to the database
    #    db = MysqlDatabase()
    #    db.saveLessonsToDb(listWithLessons)

