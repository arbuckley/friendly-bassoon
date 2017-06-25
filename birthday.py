# Nice birthday outputs 

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
			'August', 'September', 'October', 'November', 'December']

days = [i for i in range(1, 32)]

def print_birthday(date):
	'''Outputs one's birthday, given the string of their birthday as "MM/DD/YYYY"'''
	
	bd_info = date.split('/')
	month = months[int(bd_info[0]) - 1]
	day = str(days[int(bd_info[1]) - 1])
	year = str(bd_info[2])

	print ("You were born " + month + ' ' + day + ', ' + year)

print_birthday('07/05/1997')