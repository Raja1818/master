s=open("sample_input.txt","r")                              #Opening the file
for line in s:						    #Traversing the file
	if "Number of employees" in line:
		list1=line.split(":")			    #Spliting the input value and storing
		a=int(list1[1])
	elif "Goodies and Prices:" in line:		
		dist={}					    #Intializing the Dictionary
	elif line=="\n":
		pass					    #Ignoring the empty lines
	else:
		list2=line.split(":")
		d=int(list2[1])				    #Storing data into the Dictionary (goodies as a 'key' and price as a 'values')
		dist[list2[0]]=d
temp={}
d2=sorted(dist.values())				    #Sorting in acsending order based on values
d4=sorted(dist.items(),key=lambda x:x[1])
for i in range(0,len(d2)-a+1):
	temp[i]=d2[i+a-1]-d2[i]				    #Storing the diffirence between highest and lowest goodies price
d3=min(temp.items(),key=lambda x:x[1])
b=int(d3[0])						    #Finding the minimum diffirence between highest and lowest goodies price
l=str(d3[1])
e=open("sample_output.txt","w")				    #Creating the output file
e.write("The goodies selected for distribution are: \n \n") #writing into the output file
for j in range(b,b+a):
	out=d4[j]
	g= str(out[0])
	p=str(out[1])
	e.write(g+":"+p+"\n")
e.write("\n \nAnd the difference between the chosen goodie with highest price and the lowest price is"+l)
e.close()						    #Closing the file
