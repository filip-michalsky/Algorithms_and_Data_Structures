
def gen_par(n,memo={}):
	if n ==1:
		return ['()']
	elif n in memo:
		return memo[n]
	else: 
		a = gen_par(n-1,memo)
		memo[n] = []
		# now for each member in a, I need to 
		# insert parentheses around, to the left and to the right, and take a set of it
		for i in a:
			memo[n].append('('+i+')')
			memo[n].append('()'+i)
			memo[n].append(i+'()')
			if len(i)>2:
				elem = 0
				while i[elem]!=')':
					memo[n].append('('+i[:elem]+')'+i[elem:])
					elem+=1
				while elem < len(i):
					memo[n].append(i[:elem]+'('+i[elem:]+')')
					elem +=1


		answer = memo[n]
		answer = list(set(answer))
		memo[n] = answer

		return memo[n]

ans = gen_par(4)
print(len(ans))
correct_out = ["(((())))","((()()))","((())())",\
"((()))()","(()(()))","(()()())","(()())()","(())(())",\
"(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

assert len(ans) == len(correct_out)