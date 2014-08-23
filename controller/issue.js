/*
 * Author: love
 * E-Mail: zhifei@nfs.iscas.ac.cn
 */

var exec = require('child_process').exec;

$(function(){

cmd = "./tools/issue.py"; 
	exec(cmd, function(error, stdout, stderr) {
		console.log("helloword");
		console.log(stdout);
		console.log("helloword");
		document.getElementById("os-info").innerHTML=stdout;
	});
})
