#!/usr/bin/python

"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 
import time

#display ethe's bandwidth of each interface 
#return a list containning bandwidth of each interfaces
#[interface, rx_bytes, tx_bytes]
#the bandwidth is bytes
class BANDWIDTH:
    """
    constructor function
    """
    def __init__(self):
        self.__name = 'BANDWIDTH'

    def getdata(self):
        """
        Get the execute results
        """
        
        interfaces = commands.getstatusoutput('ls /sys/class/net')[1]
        interfaces = interfaces.split('\n')
        
        time.sleep(5);
        
        results = []
        for iface in interfaces:
            tx_start= commands.getstatusoutput("cat /sys/class/net/" + iface + "/statistics/tx_bytes")[1]

            rx_start= commands.getstatusoutput("cat /sys/class/net/" + iface + "/statistics/rx_bytes")[1]
            
            time.sleep(2);

            tx_end = commands.getstatusoutput("cat /sys/class/net/" + iface + "/statistics/tx_bytes")[1]
            rx_end = commands.getstatusoutput("cat /sys/class/net/" + iface + "/statistics/rx_bytes")[1]
            
            results.append([iface, int(rx_end.strip()) - int(rx_start.strip()), int(tx_end.strip()) - int(tx_start.strip())])
            #results.append([iface, int(rx_end.strip()) - int(rx_start.strip()), int(tx_end.strip()) - int(tx_start.strip())])


        tmp = []
        for i in results:
            if i[1] and i[2]: 
               tmp = [j for j in i]
               break
        ##############
        ##please remind it
        ##############
        if len(tmp) == 0:
            tmp = ['wlan0', 0, 0]
        print tmp

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
    OBJ = BANDWIDTH()
    DATA = OBJ.getdata()
    #OBJ.testgetdata(DATA)

