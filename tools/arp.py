#!/usr/bin/python
"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 

#display ethe's ip and MAC
#return a list containning title and arp item
class arp:
    def __init__(self):
	    self.__name = 'arp'

    def getData(self):
        (status, output) = commands.getstatusoutput('if [ -e /usr/sbin/arp ] ; then /usr/sbin/arp ; else /sbin/arp ; fi | awk \'BEGIN {OFS=","} {print $1,$2,$3,$4,$5}\'')
        return output.split() 

    def testGetData(self,test):
        print test 

if __name__ == '__main__':
    a = arp()
    test = a.getData()
    a.testGetData(test)
