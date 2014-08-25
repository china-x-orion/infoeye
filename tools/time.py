#!/usr/bin/python

"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 


#display the server's time
#return a time string
class servertime:
    def __init__(self):
	    self.__name = 'time'

    def getData(self):
        (status, output) = commands.getstatusoutput('date')
        return output 

    def testGetData(self,test):
        print test

if __name__ == '__main__':
    a = servertime()
    test = a.getData()
    a.testGetData(test)
