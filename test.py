
def gcd(str1, str2):
	
	if(len(str1) < len(str2)):
		return gcd(str2, str1)	
	elif(not str1.startswith(str2)):
		return ""
	elif(len(str2) == 0):
		return str1
	else:
		return gcd(str1[len(str2):], str2)
	
