#!/usr/bin/python

"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 

#display the connection status 
#return a list containning ping results
class ping:
    def __init__(self):
	    self.__name = 'ping'

    def getData(self):
        try:
            f = open('ping_hosts')
            hosts = f.readlines()
            f.close()
        except:
            hosts = ["baidu.com", "taobao.com", "weibo.com", "gnu.org", "github.com", "wikipedia.org"]
        pingCount = 2;


        output = [[h, commands.getstatusoutput('/bin/ping -qc' + str(pingCount) + ' ' + h + '| awk -F/ \'/^rtt/ { print $5 }\'')[1]] for h in hosts]
        print [[i, j] for i,j in output]
        #return [i + ' ' + j for i,j in output]

  
    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = ping()
    test = a.getData()
    #a.testGetData(test)

