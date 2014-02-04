#!/usr/bin/python3
# contains the data from one square in the roster and is present in
# the list on the roster data

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

