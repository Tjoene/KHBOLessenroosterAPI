#!/usr/bin/python3

class Lesson :
    def __init__ ( self,classLesson,month,day,hour,data ) :
        self.classLesson = classLesson 
        self.month = month
        self.day = day
        self.hour = hour
        self.data = data 

import pymysql
class MysqlDatabase :
    def saveLessonsToDb (self, listLessons) :
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='db_lessenrooster')
        cur = conn.cursor() 
        for lesson in listLessons :
            query = "INSERT INTO lessons (class,month,day,hour,data) VALUES ('"+lesson.classLesson + "' , '"+lesson.month+"' , '"+lesson.day+"' , '"+lesson.hour+"' , '"+lesson.data+"');"
            print (query)
            cur.execute(query)
    
        conn.commit() 
        conn.close()

# test the function
def testSave() :
    l1 = Lesson ('testClass','1','1','1','blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah')
    l2 = Lesson ('testClass2','1','1','1','blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah')
    l3 = Lesson ('testClass3','1','1','1','blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah')
    testList = [ l1 ,l2 ,l3  ]
    saveLessonsToDb(testList)

#testSave()

