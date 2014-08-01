import math as ma

def fiba(n=0):
	
	if n==0: return 0
	if n==1: return 1
	else:
		return fiba(n-2) + fiba(n-1)


def main():

	n_user = int(raw_input("n:"))

	print ">>> Calculating fib seq for n=%d" % n_user
	print "fib(%d) = %d" % (n_user, fiba(n_user))


if __name__ == "__main__":
	main()