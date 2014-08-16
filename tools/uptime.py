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
            daysornot = str(days) + 'days' + 's' if days > 1 else ''
            uptime_rst += daysornot + ' '	
		
        if hours > 0:
            hoursornot = str(hours) + 'hour' + 's' if hours > 1 else '' 
            uptime_rst += hoursornot + ' '	
		
        if minutes > 0:
            minutesornot = str(minutes) + 'minute' + 's' if minutes > 1 else '' 
            uptime_rst += minutesornot + ' '
            
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

