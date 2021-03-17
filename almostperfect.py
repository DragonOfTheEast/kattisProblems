from math import sqrt
while True:
	try:
		n = int(input())
	except:
		break
	
	ans = 0
	val = sqrt(n)
	i = 1
	while i <= val:
		if n%i == 0:
			if i == n/i:
				ans += i
			else:
				ans += i
				ans += n/i
		i = i +  1
	ans -= n 
	if ans == n:
		print(f'{n} perfect')
	elif abs(n-ans) <= 2:
		print(f'{n} almost perfect')
	else:
		print(f'{n} not perfect')	
		
	
