import math as ma
from sys import exit

# currently only works for up to certain number of decimal places
# consider changing to class based design to make use of shared variables

def check_decimal_places(val=None):

	ctr = 0
	while abs(val)<1:
		val *= 10
		ctr += 1
	return ctr

def calculate_pi(a=None,b=None,t=None):
	return ma.pow(a+b, 2)/(4*t)

def gauss_legendre(dec = 1, n=0, a = 1., b = float(1./ma.sqrt(2)), t = float(1./4.), p = 1.):
	'''implement the gauss-legendre series'''

	this_pi = calculate_pi(a, b, t)

	n_dec = check_decimal_places(float(this_pi - ma.pi))

	if dec < n_dec:
		print dec, n_dec
		print this_pi, type(this_pi)
		return this_pi

	#create dictionary of new values
	out = {
		"n": n+1,
		"a": 0.5*(a+b),
		"b": ma.sqrt(a*b),
		"t": t - p*ma.pow(a-0.5*(a+b), 2),
		"p": 2*p
	}
	# recalculate
	return gauss_legendre(**out)

def main():

	n_decimal = int(raw_input("Number of decimal places?"))

	print "Calculating pi to %d decimal places..."

	my_pi = gauss_legendre(dec = n_decimal)
	print type(my_pi)

	print "pi = %f" % my_pi

if __name__ == "__main__":
	main()
