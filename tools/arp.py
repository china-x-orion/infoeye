#!/usr/bin/python

"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 

#display ethe's ip and MAC
#return a list containning title and arp item
class ARP:
    """
    constructor function
    """
    def __init__(self):
        self.__name = 'ARP'

    def getdata(self):
        """
        Get the execute results
        """
        output = commands.getstatusoutput(\
        'if [ -e /usr/sbin/arp ] ; then /usr/sbin/arp ;\
        else /sbin/arp ; fi | awk \'BEGIN {OFS=","} \
        {print $1,$2,$3,$4,$5}\'')[1]
        print [i.split(",") for i in output.split("\n")[1:]]
        #return [i.split(",") for i in output.split("\n")[1:]]

    def testgetdata(self, test):
        """
        Test whether the function is work
        """
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    OBJ = ARP()
    DATA = OBJ.getdata()
    #OBJ.testgetdata(DATA)
