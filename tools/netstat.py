"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""
#!/usr/bin/python
import commands 

#display the living connections 
#return a list containning living connections 
class netstat:
    def __init__(self):
	    self.__name = 'netstat'

    def getData(self):
        (status, output) = commands.getstatusoutput('netstat -ntu | /usr/bin/awk \'NR>2 {sub(/:[^:]+$/, ""); print $5}\' | sort | uniq -c')
        #return output.split('\n') 
        return [i.strip() for i in output.split("\n")]

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = netstat()
    test = a.getData()
    a.testGetData(test)
