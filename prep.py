outPutSh = "#!/bin/bash\n"
for k in range(0,23):
	outPutSh+="python run.py "+str(1000*k)+" "+str(1000*k+1000)+" &\n"
outPut = open("goGetIt.sh","w")
outPut.write(outPutSh)
outPut.close()
