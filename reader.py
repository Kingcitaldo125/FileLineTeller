holder={}
with open("rotatePoint.py","r") as f:
	nchar=0
	line=1
	
	for l in f:
		nchar=len(l)
		holder[str(line)]=nchar
		line+=1

mLines=0
for k,v in holder.items():
	if v > mLines:
		mLines=v

for k,v in holder.items():
	if v==mLines:
		print("Line",k)
