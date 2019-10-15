
magicians =['charlie','chaplin','niloy']
for magician in magicians:
	print (magician, end = "\t")
	print ('\n')
for value in range (1,5):
	print (value)
number =list(range (1,10,3))
print(number)

digits =[1,2,3,40,5,26,7,8,9]

print ('The minimum value is:{}'.format(min(digits)))
print ('The maximum value is:{}'.format(max(digits)))
print ('The sum of value is:{}'.format(sum(digits)))

players =["niloy","sagar","imam","zahid","pritam","olive"]
print(players[3:5])
print(players[-1])
print(players[3:]) 
#copy to my players
my_players = players[:]
print(my_players)