
def dp_multiply(num1,num2):

	if num1 ==0 or num2 == 0:
		return 0

	if num2 == 1:
		return num1
	else:
		return num1 + dp_multiply(num1,num2-1)


