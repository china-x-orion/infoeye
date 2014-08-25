/*
 * Author: love
 * E-Mail: zhifei@nfs.iscas.ac.cn
 */

var exec = require('child_process').exec;

$(function(){

cmd = "./tools/loadavg.py"; 
	exec(cmd, function(error, stdout, stderr) {
		console.log(stdout);
		cpuRstPer = stdout.split('\n')[0].split(' ');
		cpuRst = stdout.split('\n')[1].split(' ');
		$("#cpu-1min-per").text(cpuRstPer[0]);
		$("#cpu-5min-per").text(cpuRstPer[1]);
		$("#cpu-15min-per").text(cpuRstPer[2]);
		$("#cpu-1min").text(cpuRstPer[0]);
		$("#cpu-5min").text(cpuRstPer[1]);
		$("#cpu-15min").text(cpuRstPer[2]);
	});
})
