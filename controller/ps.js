var exec = require('child_process').exec;
var cmd = "python ../tools/loadavg.py";
	exec(cmd, function(error, stdout, stderr) {
		console.log(stdout);
		cpuRstPer = stdout.split('\n')[0].split(' ');
		console.log("&&&&&&&&&&" + cpuRstPer[2]);
		for (var i=0; i<3; i++){
			console.log(cpuRstPer[i]);
		}
		cpuRstFlo = stdout.split('\n')[1].split(' ');
		console.log(cpuRstPer);
//		document.getElementById("os-info").value=stdout;
	});

