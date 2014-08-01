def is_prime(val = None):

	if val == 1:
		return False
	for i in range(2, 1+val/2):
		if val%i == 0:
			return False

	return True

def get_prime_factors(num = 0):
	
	facts = []

	if num == 0:
		return None

	for i in range(1, 1+num/2):
		if num%i == 0:
			if is_prime(i):
				facts.append(i)

	return facts

def main():

	p_facts = get_prime_factors(int(raw_input("Test num:")))

	if p_facts:
		print "prime factors:"
		for i in p_facts:
			print i
	else:
		print "None found"

if __name__ == "__main__":
	main()