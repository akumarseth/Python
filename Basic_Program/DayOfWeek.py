# Python3 program to find day
# of a given date

def dayofweek(d, m, y):
	t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
	y -= m < 3
	return (( y + int(y / 4) - int(y / 100)
			+ int(y / 400) + t[m - 1] + d) % 7)

# Driver Code
day = dayofweek(24, 12, 1989)
print(day)
