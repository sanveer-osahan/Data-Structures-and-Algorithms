def print_combinations(inp, cstr, i, n):
	if n==0:
		print("".join(cstr))

	else:
		digit = int(inp[0])
		alphabets = numpad[digit-1]
		for each in alphabets:
			cstr[i] = each
			print_combinations(inp[1:], cstr, i+1,n-1)


numpad = [  '', 'ABC', 'DEF',
			'GHI', 'JKL', 'MNO',
			'PQRS', 'TUV', 'WXYZ'
		]

inp = "234567234567"
n = len(inp)
istr = ['']*n
print_combinations(inp, istr, 0,n)


