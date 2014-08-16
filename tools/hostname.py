"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""
#!/usr/bin/python
import commands 

#display the users serverhostname 
#return a list containning serverhostname users
class serverhostname:
    def __init__(self):
	    self.__name = 'serverhostname'

    def getData(self):
        (status, output) = commands.getstatusoutput('hostname')
        return output.split() 

    def testGetData(self,test):
        print test 

if __name__ == '__main__':
    a = serverhostname()
    test = a.getData()
    a.testGetData(test)
