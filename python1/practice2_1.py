"""
Second problem
coded by Junho Kim
"""

f=open("data.txt","r") #file open
lists=[]
dataform=[str,int,int] #dataform of the file

def a_precede_b (a,b): #telling the ordering
	for i in range(len(dataform)):
		if dataform[i]==int:
			if int(b[i])<int(a[i]):
				return False
			elif int(b[i])>int(a[i]):
				return True
			else:
				continue
		for j in range(min(len(a[i]),len(b[i]))):
			if a[i][j]>b[i][j]:
				return False
			elif a[i][j]<b[i][j]:
				return True
		if len(a[i])>len(b[i]):
			return False
		elif len(b[i])>len(a[i]):
			return True
	return True	

full=f.read() #flie reading
for l in full.split("\n"): #make txt file into lists
	lists.append(l.split(","))



#ordering according to the order telling
while True:
	ordering=input("Which ordering(ascending/descending):")
	if ordering=="ascending":
		for i in range(1,len(lists)):
			for j in range(i):
				if a_precede_b(lists[i],lists[j]):
					lists.insert(j,lists[i])
					del lists[i+1]
					break
		break
	elif ordering=="descending":
		for i in range(1,len(lists)):
			for j in range(i):
				if a_precede_b(lists[j],lists[i]):
					lists.insert(j,lists[i])
					del lists[i+1]
					break
		break
	print("Input Error")
result=""

#making info into string
for i in range(len(lists)):
	tmpi=""
	for j in range(len(dataform)):
		tmpj=""
		tmpj=(str)(lists[i][j])
		if(j!=0):
			tmpj=","+tmpj
		tmpi+=tmpj
	if(i!=0):
		tmpi="\n"+tmpi
	result+=tmpi
print(result)
	
f.close()
