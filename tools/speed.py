#!/usr/bin/python
"""
Author:rockylinux
E-mail:Jingzheng.W@gmail.com
"""
import commands 
import socket 
import time
import sys

#display the network speed
#return a list containning the download and upload speed 
class SPEED:
    """
    constructor function
    """
    def __init__(self):
        self.__name = 'SPEED'

    def getdata(self):
        """
        Get the execute results
        """
        
        mb = 1000000;

        """
        Configure download & upload hosts.
        This array exist just to give some choice and flexibility to the user.
        """
        
        """
        * A /dev/null type service to POST blobs which will discard data after reading is recommended.
        * If you know of such service please let me know.
        * This one here has some very cool features. Visit the site for more options like custom server status_code response etc.
        * Change or remove resource query string dir=... if you do not wont your request logged.
        """
        upload = {"0" : {'hostname' : 'posttestserver.com', \
                         'resource' : '/post.php?dir=linuxdash',\
                         'size' : 1, 'timeout' : 30}}
        """
        A big(~10MB) CDN hosted( e.g CloudFlare ) blob would be preferable for high availability and consistent performance.
        """
        download = {\
                    #IPv4 & IPv6 Port: 80, 81, 8080 IPv6
                    "0" : {'hostname' : 'download.thinkbroadband.com',\
                           'resource' : '/10MB.zip',\
                           'size' : 10, 'timeout' : 30},

                    "1" : {'hostname' : 'cachefly.cachefly.net',\
                           'resource' : '/10MB.test',\
                           'size' : 10, 'timeout' : 30},
                    "2" : {'hostname' : 'speedtest.sea01.softlayer.com',\
                           'resource' : '/downloads/test10.zip',\
                           'size' : 10, 'timeout' : 30},
                    "3" : {'hostname' : 'download.thinkbroadband.com',\
                           'resource' : '/50MB.zip',\
                           'size' : 50, 'timeout' : 120}\
                   }

        dChosenHost = "2"
        dHostname = download.get(dChosenHost).get('hostname')
        dResource = download.get(dChosenHost).get('resource')
        dTimeout = download.get(dChosenHost).get('timeout')
        dPort = 80;
        
        outDownload = "GET " + dResource + " HTTP/1.1\r\n"
        outDownload += "Host: " + dHostname + "\r\n"
        outDownload += "Connection: Close\r\n\r\n"
        chunkSize = 1024
        
        speedDownstream = 0
        speedUpstream = 0
        
        realDownloadSize = 0
        
        startDownload = time.time() 
        
        #timeout here only applies while connecting the socket
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(dTimeout)
            sock.connect((dHostname, dPort))
            sock.send(outDownload)
            
            data = ""
            while 1:
                revs =  sock.recv(chunkSize)
                if revs:
                    data += revs
                else:
                    break
                
            """
                /*
                 * $realDownloadSize is calculated to make sure we are estimating the speed on the real download size.
                 * If the connection goes down before completing the download we will still be able to calculate the speed
                 * correctly based on the partial download.
                 * There is some confusion between MB and MiB too. Many blobs declared as x MB seems to be x MiB.
                 */
             """
                
            endDownload = time.time() 
            realDownloadSize = sys.getsizeof(data)
            timeDownload = endDownload - startDownload
                
            #print realDownloadSize / 1024, len(data), timeDownload
                
            if (timeDownload):
                speedDownstream = realDownloadSize / 1024 / timeDownload

        except:
            print "except"
            pass


            """
            if (!$fpDownload) {
                echo "$errstr ($errno)<br />\n";
            } else {
                fwrite($fpDownload, $outDownload);
                /* timeout here applies for reading/writing data over the socket */
                stream_set_timeout($fpDownload, $dTimeout);
                while (!feof($fpDownload)) {
                    $strFile .= fread($fpDownload, $chunkSize);
                }
                endDownload = time.time() 
                fclose($fpDownload);
                /*
                 * $realDownloadSize is calculated to make sure we are estimating the speed on the real download size.
                 * If the connection goes down before completing the download we will still be able to calculate the speed
                 * correctly based on the partial download.
                 * There is some confusion between MB and MiB too. Many blobs declared as x MB seems to be x MiB.
                 */
                $realDownloadSize = strlen($strFile);
                $timeDownload = $endDownload - $startDownload;
                if ($timeDownload) {
                    $speedDownstream = ($realDownloadSize / $timeDownload);
                }
            }

            // Proceed to upload only if we actually have something to do upload
            if ($realDownloadSize) {

                $uChosenHost = 0;
                $uHostname = $hosts['upload'][$uChosenHost]['hostname'];
                $uResource = $hosts['upload'][$uChosenHost]['resource'];
                $uSize = $hosts['upload'][$uChosenHost]['size'] * $mb;
                $uTimeout = $hosts['upload'][$uChosenHost]['timeout'];
                $uPort = 80;

                $outUpload = "POST {$uResource} HTTP/1.1\r\n";
                $outUpload .= "Host: {$uHostname}\r\n";
                $outUpload .= "Content-type: application/x-www-form-urlencoded\r\n";
                $outUpload .= "Content-length: " . $realDownloadSize . "\r\n";
                $outUpload .= "Accept: */*\r\n\r\n";
                $data = urlencode($strFile);

                $startUpload = microtime(true);

                $fpUpload = fsockopen($uHostname, $uPort, $errno, $errstr, $uTimeout);
                if (!$fpUpload) {
                    echo "$errstr ($errno)<br />\n";
		    $speedUpstream = "n/a";
                } else {
                    fwrite($fpUpload, $outUpload);
                    stream_set_timeout($fpUpload, $uTimeout);
                    $writeSize = fwrite($fpUpload, $data, $uSize);

                    if ($writeSize) {
                        $endUpload = microtime(true);
                        fclose($fpUpload);

                        $timeUpload = $endUpload - $startUpload;
                        if ($timeUpload) {
                            $speedUpstream = ($writeSize / $timeUpload);
                        }

                    }
                }
            }

            $speed = array(
                'upstream' => $speedUpstream,
                'downstream' => $speedDownstream,
            );
        
        return "XXX"#output.split("\n")[1] 
        """

        return "Download speed " + str(speedDownstream) + "KB/s"

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
    OBJ = SPEED()
    DATA = OBJ.getdata()
    OBJ.testgetdata(DATA)

