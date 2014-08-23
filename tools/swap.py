#!/usr/bin/python
"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 

#display the server's swap 
#return a swap string
class swap:
    def __init__(self):
	    self.__name = 'swap'

    def getData(self):
        (status, output) = commands.getstatusoutput('/bin/cat /proc/swaps | /usr/bin/tail -n +2 | /usr/bin/awk \'{print $1","$2","$3","$4","$5}\'')
        return output.split() 

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = swap()
    test = a.getData()
    a.testGetData(test)
