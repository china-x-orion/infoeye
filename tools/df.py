"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""
#!/usr/bin/python
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
        print test 

if __name__ == '__main__':
    a = diskfree()
    test = a.getData()
    a.testGetData(test)
