import subprocess
return_code =0
#return_code = subprocess.call(["echo Hello World"], shell=True)
#return_code = subprocess.check_output("echo Hello World", stderr=subprocess.STDOUT, shell=True)




return_code = subprocess.check_output("c:/cygwin64/bin/run.exe rsync -avzh /cygdrive/s/CinemaFlowWorks /cygdrive/s/CinemaFlowWorks1", stderr=subprocess.STDOUT, shell=True)



print(return_code)
