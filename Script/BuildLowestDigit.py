# Python program to build the smallest number by removing n digits from a given number

 # A recursive function that removes 'n' characters from 'str'
 # to store the smallest possible number in 'res'
def buildLowestNumberRec(str, n, res) :
	# If there are 0 characters to remove from str,
	# append everything to result
	if (n == 0) :
		res.append(str)
		return
	length = len(str)
	 # If there are more characters to remove than string
	# length, then append nothing to result
	if (length <= n) :
		return
	# Find the smallest character among first (n+1) characters
	#  of str.
	minIndex = 0
	for i in range(n):
		if (str[i] < str[minIndex]) :
			minIndex = i

	 # Append the smallest character to result
	res += (str[minIndex])

	# substring starting from minIndex+1 to str.length() - 1.
	new_str = str[minIndex+1:length-minIndex]

	 # Recur for the above substring and n equals to n-minIndex
	buildLowestNumberRec(new_str, n-minIndex, res)

# A wrapper over buildLowestNumberRec()
def buildLowestNumber(str, n):
    res = "";
    # Note that result is passed by reference
    buildLowestNumberRec(str, n, res)
    return res

# Driver program to test above function
str = "121198"
n = 2
buildLowestNumber(str, n)
