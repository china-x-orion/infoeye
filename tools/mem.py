"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""
#!/usr/bin/python
import commands 

#display the memory of total, used and free 
#return a list containning total, used and free memory 
class mem:
    def __init__(self):
	    self.__name = 'mem'

    def getData(self):
        (status, output) = commands.getstatusoutput('/usr/bin/free -tmo | /usr/bin/awk \'BEGIN {OFS=","} {print $1,$2,$3-$6-$7,$4+$6+$7}\'')
        return output.split()[1:] 

    def testGetData(self,test):
        print test 

if __name__ == '__main__':
    a = mem()
    test = a.getData()
    a.testGetData(test)
