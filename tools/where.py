#!/usr/bin/python
"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""

import commands 

#display the software 
#return a list containning installed software
class whereissoftware:
    def __init__(self):
	    self.__name = 'whereissoftware'

    def getData(self):
        (status, output) = commands.getstatusoutput('dpkg -l | awk \'{print$2, $3}\'')
        return output 

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = whereissoftware()
    test = a.getData()
    a.testGetData(test)
