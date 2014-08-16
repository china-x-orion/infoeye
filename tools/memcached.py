"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""
#!/usr/bin/python
import commands 

#display the memcached 
#return a list containning memcached 
class memcached:
    def __init__(self):
	    self.__name = 'memcached'

    def getData(self):
        (status, output) = commands.getstatusoutput('echo "stats" | nc -w 1 127.0.0.1 11211 | awk \'BEGIN {}/bytes/{line[j++] = $2 ":" $3 }END{ for(i=0;i<j;i++) print line[i]; }\'')
        return output

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = memcached()
    test = a.getData()
    a.testGetData(test)
