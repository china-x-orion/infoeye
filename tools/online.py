#!/usr/bin/python
"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""

import commands 

#display the users online 
#return a list containning online users
class online:
    def __init__(self):
	    self.__name = 'online'

    def getData(self):
        (status, output) = commands.getstatusoutput('/usr/bin/w -h | /usr/bin/awk \'{print $1","$2","$4","$5}\'')
        return output.split() 

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = online()
    test = a.getData()
    a.testGetData(test)
