t=()
while 1:
	item=input('enter item')
	t=t+(item,)
	c=input('do you want to continue y/n')
	if c.lower()=='n':
		break
print(t)
