#!/usr/bin/python

import commands 

"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""
#display the issue 
#return a list containning issue string 
class issue:
    def __init__(self):
	    self.__name = 'issue'

    def getData(self):
        (status, output) = commands.getstatusoutput('/usr/bin/lsb_release -ds;/bin/uname -r')
        print ' '.join(output.split("\n"))
        #return ' '.join(output.split("\n"))

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = issue()
    test = a.getData()
    #a.testGetData(test)
