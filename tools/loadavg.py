"""
Author:  rockylinux
E-Mail:  Jingzheng.W@gmail.com 
"""
#!/usr/bin/python
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
        loadAvg = resultLoadAvg

        loadAvgList = [float(i) / int(numberOfCores) for i in loadAvg.split(',')]
        loadAvgListPercent = [str(i/100) + "%" for i in loadAvgList]

        return [loadAvgListPercent, loadAvgList]

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = loadavg()
    test = a.getData()
    a.testGetData(test)
