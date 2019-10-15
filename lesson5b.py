
players =["niloy","sagar","imam","zahid","pritam","olive"]

for name in players:
	#Sprint(name)
	
	if name =='niloy':
		print(name.upper())
	else:
		print(name.lower())
age=17
if age <=18:
	print("You ere not eligible for vote")
else:
	print("You ere eligible for vote")
	
age=21
if age <=18:
	print("You ere not eligible for vote")
else:
	print("You ere eligible for vote")

	
'''month = int(input("Enter month value [1-3]: "))
if month==1:
	print('January')
elif month==2:
	print('February')
elif month==3:
	print('March')
else:
	print('Invalid')
number= list(range (1,50))
print(number) '''
for n in range(50):
	#print(n, end='\t')
#print(number)
	if n%2 !=0:
		print(n, end='\t')
for n in range(50):
	#print(n, end='\t')
#print(number)
	if n%2 ==0:
		print(n, end='\t')

number =list(range (1,11))
print ('The sum of value is:{}'.format(sum(number)))

sum=0
print ('The sum of value is:',end="")
for n in range(0,11):
	sum=sum+n
print(sum, end='\t')
print('\n')

#print ('The sum of value is:{}'.format(sum(sum)))
print(30*'=')
number =list(range (1,10))
print(number)

