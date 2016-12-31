import random #for toss
import os
import sys
p=['0','1','2','3','4','5','6','7','8','9']
def make_board():
	print("     |     |")
	print ('__'+p[1]+'__|__'+p[2]+'__|__'+p[3]+'__')
	print("     |     |")
	print ('__'+p[4]+'__|__'+p[5]+'__|__'+p[6]+'__')
	print("     |     |")
	print ('  '+p[7]+'  |  '+p[8]+'  |  '+p[9]+'  ')
def win():
	if(p[1]==p[2]==p[3]):
		return True
	elif(p[4]==p[5]==p[6]):
		return True
	elif(p[7]==p[8]==p[9]):
		return True
	elif(p[1]==p[4]==p[7]):
		return True
	elif(p[2]==p[5]==p[8]):
		return True
	elif(p[3]==p[6]==p[9]):
		return True
	elif(p[1]==p[5]==p[9]):
		return True
	elif(p[3]==p[5]==p[7]):
		return True
	else:
		return False
make_board()
print("Player A play with 'X' and Player B play With '0'")
print("Coin toss to decide which player move first")
coin=['A','B']
winner=coin[random.randint(0,1)]
print("Player "+winner+" move First")
for i in range(9):
	if(winner=='B'):
		
		print("Player B Which position you want to insert '0' ?")
		tr=True
		while(tr==True):
			x=int(input())
			if(x>9 or x<1):
				print("Invalid Location try again")
			elif(p[x]=='X'or (p[x]=='0')):
				print("Position already filled try again")
			else:
				p[x]='0'
				tr=False		
		make_board()
		if(win()):
			print("Player B wins")
			break
		winner='A'
		#os.system('clear')
	else:
		#os.system('clear')
		print("Player A Which position you want to insert 'X' ?")
		tr=True
		while(tr==True):
			x=int(input())
			if(x>9 or x<1):
				print("Invalid Location try again")
			elif(p[x]=='X'or (p[x]=='0')):
				print("Position already filled try again")
			else:
				p[x]='X'
				tr=False		
		make_board()
		if(win()):
			print("Player A wins")
			break
		winner='B'