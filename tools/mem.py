#!/usr/bin/python
"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""

import commands 

#display the memory of total, used and free 
#return a list containning total, used and free memory 
class mem:
    def __init__(self):
	    self.__name = 'mem'

    def getData(self):
        (status, output) = commands.getstatusoutput('/usr/bin/free -tmo | /usr/bin/awk \'BEGIN {OFS=","} {print $1,$2,$3-$6-$7,$4+$6+$7}\'')
        #print [int(i.replace(",","")) /1024/  1024 /1024 for i in output.split()[1:]] 
        #return output.split()[1:] 
        print output.split()[1].split(",") 

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = mem()
    test = a.getData()
    #a.testGetData(test)
