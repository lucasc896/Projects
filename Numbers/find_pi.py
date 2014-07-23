import math as ma

def check_decimal_places(val=None):
	#FIXME: some sweet way to check the num decimal places

def calculate_pi(a=None,b=None,t=None):
	return ma.pow(a+b, 2)/(4*t)

def gauss_legendre(dec = 1, n=0, a = 1., b = float(1./ma.sqrt(2)), t = float(1./4.), p = 1.):
	
	this_pi = calculate_pi(a, b, t)

	print "n=%d: %.20f" % (n, this_pi)
	n_dec = check_decimal_places(float(this_pi - ma.pi))

	if dec < n_dec:
		return

	if n < 5:
		#create dictionary of new values
		out = {
			"n": n+1,
			"a": 0.5*(a+b),
			"b": ma.sqrt(a*b),
			"t": t - p*ma.pow(a-0.5*(a+b), 2),
			"p": 2*p
		}
		# recalculate
		gauss_legendre(**out)

	return



def main():
	n_decimal = int(raw_input("Number of decimal places?"))

	print "Calculating pi to %d decimal places..."

	gauss_legendre(dec = n_decimal)

if __name__ == "__main__":
	main()
