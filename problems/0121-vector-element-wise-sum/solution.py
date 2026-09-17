def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	if len(a)==len(b):
		for i in range(0,len(a)):
			a[i]=a[i]+b[i]
		return a
	return -1