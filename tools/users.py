#!/usr/bin/python
"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 

#display the users, type and home 
#return a list containning the users, type and home 
class users:
    def __init__(self):
	    self.__name = 'users'

    def getData(self):
        (status, output) = commands.getstatusoutput('/usr/bin/awk -F: \'{ if ($3<=499) print "system,"$1","$6; else print "user,"$1","$6; }\' < /etc/passwd')
        return output.split() 

    def testGetData(self,test):
        print test 

if __name__ == '__main__':
    a = users()
    test = a.getData()
    a.testGetData(test)
