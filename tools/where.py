"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""
#!/usr/bin/python
import commands 

#display the software 
#return a list containning installed software
class whereissoftware:
    def __init__(self):
	    self.__name = 'whereissoftware'

    def getData(self):
        (status, output) = commands.getstatusoutput('dpkg -l | awk \'{print$2","$3}\'')
        return output 

    def testGetData(self,test):
        print test 

if __name__ == '__main__':
    a = whereissoftware()
    test = a.getData()
    a.testGetData(test)
