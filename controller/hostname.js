/*
 * Author: love
 * E-Mail: zhifei@nfs.iscas.ac.cn
 */
var exec = require('child_process').exec;

$(function(){

cmd = "./tools/hostname.py"; 
	exec(cmd, function(error, stdout, stderr) {
		console.log(stdout);
		document.getElementById("os-hostname").innerHTML=stdout;
	});
})