def skip_elements(elements):
	# code goes here
	even=[]
	for i, e in enumerate(elements):
		if i%2 == 0:
			even.append ("{e}".format(e=e))		
	return even


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
