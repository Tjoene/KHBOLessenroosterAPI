#!/usr/bin/python3

#needed for reading files
import sys

import LessonData
import RosterData
import HTMLRosterParser
import RosterExtractor
import Roster

listOfRosters = []
for i in range(1,len(sys.argv)) :
#    try :
    roster = Roster.Roster(sys.argv[i])
#    except :
#        print('error in :'+sys.argv[i])

