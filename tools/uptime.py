#!/usr/bin/python
"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 

#display server's time 
#return a time string
class uptime:
    def __init__(self):
	    self.__name = 'time'

    def getData(self):
        (status, output) = commands.getstatusoutput('cat /proc/uptime')
        totalSeconds = output.split()[0]
        totalMinutes = float(totalSeconds) / 60
        totalHours = totalMinutes / 60
        days = int( totalHours / 24 )
        hours = int( totalHours - ( days * 24 ) )
        minutes = int(totalMinutes - (days * 60 * 24) - (hours * 60) )
        uptime_rst = ''
        if days:
            dornot = 's' if days > 1 else ''
            daysornot = str(days) + 'day' + dornot
            uptime_rst = uptime_rst + daysornot  + ' '
		
        if hours > 0:
            hornot = 's' if hours > 1 else ''
            hoursornot = str(hours) + 'hour' + hornot 
            uptime_rst = uptime_rst + hoursornot + ' '	
		
        if minutes > 0:
            mornot = 's' if minutes > 1 else ''
            minutesornot = str(minutes) + 'minute' + mornot
            uptime_rst = uptime_rst + minutesornot + ' '
            
        return uptime_rst 

    def testGetData(self,test):
        if type(test) == type([]):
            for i in test:
                print i
        else:
            print test 

if __name__ == '__main__':
    a = uptime()
    test = a.getData()
    a.testGetData(test)

