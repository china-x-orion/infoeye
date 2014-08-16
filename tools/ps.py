#!/usr/bin/python
"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 

#display the server's current processes 
#return a list containning current processes
class ps:
    def __init__(self):
	    self.__name = 'ps'

    def getData(self):
        (status, output) = commands.getstatusoutput('/bin/ps aux | /usr/bin/awk \'NR > 1 {print $1, $2, $3, $4, $5, $6, $7, $8, $9,$10,$11}\'')
        return output 

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = ps()
    test = a.getData()
    a.testGetData(test)

