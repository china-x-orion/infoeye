"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""
#!/usr/bin/python
import commands 

#display the users lastlog 
#return a list containning lastlog users
class lastlog:
    def __init__(self):
	    self.__name = 'lastlog'

    def getData(self):
        (status, output) = commands.getstatusoutput('/usr/bin/lastlog --time 365')
        rst = output.split("\n")[1].split()
        user = rst[0] 
        userfrom = ''
        if len(rst) > 8:
            userfrom = rst[2]
        elif len(rst) > 7:
            userfrom = rst[1]
        else:
            userfrom = 'localhost'
        return user + ", " + userfrom  + ", " + ' '.join(rst[-6:])
        

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = lastlog()
    test = a.getData()
    a.testGetData(test)
