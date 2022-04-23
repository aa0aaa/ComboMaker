#==================================================
import random 
import pyfiglet
import os
#==================================================
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
A = '\033[1;34m'
l = '\033[1;35m'

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
#==================================================
os.system('clear')
#==================================================
v1 = pyfiglet.figlet_format('       *  Charon *')
print(A+v1)
print(A+'       			 Charon - COMBO-MAKER'+'  ')
print(A+'       			 CH - @X_BlackMarket'+'  ')
print(A+'       			 Tele - @AA0AAA'+'  ')
print(A+'       			 Insta - @LUFFY_HB'+'\n'+'  ')
print(' '+Z1+'= '*20+' ')
#==================================================
print("""  """)
#==================================================
ask = input("""[1] Create USER Combo
[2] Create EMAIL Combo
 = = = = = = = = = = = = = = = = = = = = 
[+] Please Select What You Need : """)
#==================================================
if ask == "1":
	te = int(input('Enter Length Of USER : ')) 
	len = int(input('Enter Number Of USER : '))
	l = 0 
	on = 0 
	while l < len: 
		on += 1 
		c = '1234567890qwertyuiopasdfghjklzxcvbnm' 
		bot = ''.join(random.choice(c) for i in range(te)) 
		bot1 = bot + '' 
		print(f'[{on}]' + bot1) 
		with open('user.txt', 'a') as an: 
			an.write(bot1 + '\n') 
		if on == len: 
			exit()


#==================================================
if ask == "2":
	te = int(input('Enter Length Of Email : ')) 
	len = int(input('Enter Number Of Email : '))
	t1 = input('Enter Domin : ')
	l = 0 
	on = 0 
	while l < len: 
		on += 1 
		c = '1234567890qwertyuiopasdfghjklzxcvbnm' 
		bot = ''.join(random.choice(c) for i in range(te)) 
		bot1 = bot + '@' + t1 + '.com' 
		print(f'[{on}]' + bot1) 
		with open('combo.txt', 'a') as an: 
			an.write(bot1 + '\n') 
		if on == len: 
			exit()
