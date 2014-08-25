#!/usr/bin/python

"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 
import requests

#display ethe's ip and MAC
#return a list containning title and IP item
class IP:
    """
    constructor function
    """
    def __init__(self):
        self.__name = 'IP'

    def getdata(self):
        """
        Get the execute results
        """
        status, result = commands.getstatusoutput('/bin/ip -oneline link show | /usr/bin/awk \'{print $2}\' | /bin/sed "s/://"')

        output = [] 

        #tset when there is no ip commands
        #status = 1
        if status != 0:
        #It didn't work with "ip" , so we do it with ifconfig
            ifstatus, result = commands.getstatusoutput('/sbin/ifconfig | /bin/grep -B1 "inet addr" | /usr/bin/awk \'{ if ( $1 == "inet" ) { print $2 } else if ( $2 == "Link" ) { printf "%s:",$1 } }\' | /usr/bin/awk -F: \'{ print $1}\'')

        #tset when can not get the local ip address 
        #result = ""
        if len(result.strip()):
            for interface in result.split("\n"):
                for family in "inet", "inet6":
                #Now use that list to get the ip-adresses
                    ifstatus, ifoutput = commands.getstatusoutput(' /bin/ip -oneline -family ' + family  + ' addr show ' + interface + ' | /bin/grep -v fe80 | /usr/bin/awk \'{print $2","$4}\'')
                    if ifoutput.strip():
                        output.append(ifoutput)

        else:
            result = "N/A"
            #Get external adress
        
            result2 = requests.get('http://ipecho.net/plain');
            output = 'external ip, ' + result2.content
                    
        return output

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
    OBJ = IP()
    DATA = OBJ.getdata()
    OBJ.testgetdata(DATA)

