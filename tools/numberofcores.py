#!/usr/bin/python
"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""

import commands 

#display the users numberofCores 
#return a list containning numberofCores users
class numberofCores:
    def __init__(self):
	    self.__name = 'numberofCores'

    def getData(self):
        (status, resultNumberOfCores) = commands.getstatusoutput('/bin/grep -c ^processor /proc/cpuinfo')
        numberOfCores = resultNumberOfCores[0];

        return numberOfCores 

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = numberofCores()
    test = a.getData()
    a.testGetData(test)
