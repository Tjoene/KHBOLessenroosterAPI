#!/usr/bin/python3
# containts the list with all the lessons in a consisntent way
# objects from this class are formed by the HTMLRosterParser

class RosterData:
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

