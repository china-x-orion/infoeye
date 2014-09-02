#!/usr/bin/python
"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""

import commands 

#display the users loadavg 
#return a list containning loadavg users
class loadavg:
    def __init__(self):
	    self.__name = 'loadavg'

    def getData(self):
        (status, resultNumberOfCores) = commands.getstatusoutput('/bin/grep -c ^processor /proc/cpuinfo')
        numberOfCores = resultNumberOfCores[0];

        (status, resultLoadAvg) = commands.getstatusoutput('/bin/cat /proc/loadavg | /usr/bin/awk \'{print $1","$2","$3}\'')
        #loadAvg = resultLoadAvg

        #print resultLoadAvg

        loadAvgList = [float(i) / int(numberOfCores) for i in resultLoadAvg.split(',')]
        loadAvgListPercent = [str(i * 100) for i in loadAvgList]

        #rst = ' '.join([str(i) for i in loadAvgListPercent])
        #rst = rst + '\n' + ' '.join([str(i) for i in loadAvgList]) 
        #print ','.join([str(i) for i in loadAvgListPercent +  loadAvgList])
        #print [loadAvgListPercent, loadAvgList]
        #print rst

        ######
        ## There is a bug
        ## The percent value is false
        ######
        print [[loadAvgList[i], loadAvgListPercent[i]] for i in range(len(loadAvgListPercent))]
        #print [[loadAvgListPercent[0], loadAvgList[0]]]
        #print "[[1,2], [3,4],[5,6]]" 
        #return rst

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test: 
                print i 
        else:
            print test 

if __name__ == '__main__':
    a = loadavg()
    test = a.getData()
    #a.testGetData(test)
