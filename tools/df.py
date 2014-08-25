#!/usr/bin/python
"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""

import commands 

#display the users diskfree 
#return a list containning diskfree users
class diskfree:
    def __init__(self):
	    self.__name = 'diskfree'

    def getData(self):
        (status, output) = commands.getstatusoutput('/bin/df -Ph | sed -n \'2,$p\' | awk \'BEGIN {OFS=","} {print $1,$2,$3,$4,$5,$6}\'')
        return output.split() 

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = diskfree()
    test = a.getData()
    a.testGetData(test)
