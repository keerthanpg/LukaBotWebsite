filelist= ["5.txt", "20.txt", "35.txt", "65.txt", "79.txt", "95.txt", "109.txt", "125.txt"]
i=0
g=open("data_t.js", "w")
for item in filelist:
	f=open(item, "r")
	lines=f.readlines()
	print(len(lines))
	array=[]	
	g.write("var data%d_t = [" %(i+1))
	g.write(str(array))
	for line in lines:
		line=line.split()
		line[0]=int(line[0])
		print(line[1])
		line[1]=float(line[1])
		line[2]=int(line[2])
		line[3]=int(line[3])
		line[4]=float(line[4])
		line[5]=float(line[5])
		line[6]=float(line[6])
		line[7]=float(line[7])		
		array.append(line)
		g.write("[%d,%0.2f,%d,%d,%0.2f,%0.2f,%0.2f,%0.2f]," %(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7]))
	print(line)
	g.write("];\n")
	i=i+1


