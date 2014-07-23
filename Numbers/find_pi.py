import math as ma

def calculate_pi(a=None,b=None,t=None):

	return ma.pow(a+b, 2)/(4*t)

def gauss_legendre(n=0, a = 1.,	b = float(1./ma.sqrt(2)), t = float(1./4.), p = 1.):
	
	print "n=%d: %f" % (n, calculate_pi(a, b, t))

	if n < 5:
		out = {
			"n": n+1,
			"a": 0.5*(a+b),
			"b": ma.sqrt(a*b),
			"t": t - p*ma.pow(a-0.5*(a+b), 2),
			"p": 2*p
		}
		gauss_legendre(**out)

	return



def main():
	# n_decimal = int(raw_input("Number of decimal places?"))

	# print "Calculating pi to %d decimal places..."

	gauss_legendre()

if __name__ == "__main__":
	main()
