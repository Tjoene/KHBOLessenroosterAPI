#!/usr/bin/python3
# the roster extracter extracts the informtion from the rosterdata to be used to form a roster

class RosterExtracter : 
    def __init__(HTMLpage) :
        parserLessenrooster = HTMLRosterParser() 
        parserLessenrooster.feed(html)
        self.roster = parserLessenrooster.roster
    def extractDates (self,lessonDataList) :
        dates = []
        for i in range(1,6) :
            numbers = lessonDataList[i].dataList[0].split(' ') 
            numbers = numbers[1].split('/')
            dates.append(numbers)
        return dates
    def removeFile(self) :
        #os.remove(filepath)
        print('remove')

