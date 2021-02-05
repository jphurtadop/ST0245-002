def gcd_euclid(p, q):
	if q == 0:
		return p
	else:
		return gcd_euclid(q, p%q)

