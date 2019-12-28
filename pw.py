
password = 'a123456'
i = 3  # Three chances

while True:
	pw = input('pls input password: ')
	if pw == password:
		print('success')
		break #escap while loop
	else: 
		i = i-1
		print('Wrong password! You have', i , 'chances')
		if i == 0:
			break
	

