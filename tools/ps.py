#!/usr/bin/python

"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 

#display the server's current processes 
#return a list containning current processes
class ps:
    def __init__(self):
	    self.__name = 'ps'

    def getData(self):
        (status, output) = commands.getstatusoutput('/bin/ps aux | /usr/bin/awk \'NR > 0 {print $1, $2, $3, $4, $5, $6, $7, $8, $9,$10,$11}\'')
        
        return output
        #return output.replace("\n",".").split()
        #rstl = output.split("\n")[1:]
        #return [','.join(i.split())for i in rstl]

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 
    
    def getFormatData(sele, data):
        a1 = data.split("\n")[1:]
        print "Array("
        for i in range(len(a1)):
            #s1 = "[" + str(i) + "]=> array(" + a1[i] + "," 
            s1 = "[" + str(i) + "] => array(" 
            print s1
            #print "[" + str(i) + "]=> array(" + a1[i] + "," 
            a2 = a1[i].split()
            for j in range(len(a2)):
                print "[" + str(j) + "] => " + a2[j] 
            print ")" 
        print ")"
    
    def getFormatData2(sele, data):
        print [i.split() for i in data.split("\n")[1:]]

if __name__ == '__main__':
    a = ps()
    test = a.getData()
    #a.testGetData(test)
    a.getFormatData2(test)
