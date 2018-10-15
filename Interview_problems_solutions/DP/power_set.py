def p(l):
    if not l: return [[]]
    return p(l[1:]) + [[l[0]] + x for x in p(l[1:])]


my_set = [1,2,3]

ans = p(my_set)

print(ans)


 # print(subset)
 #    if len(subset)==0:
 #    	return None

 #    for elem in subset:
 #    	temp = subset.copy()
 #    	temp.remove(elem)
 #    	if len(temp)>0:
 #    		powerset.append(power_set(temp,powerset))

 #     # after adding all of the children, add self to the super set
 #    powerset.append(subset)
 #    return powerset