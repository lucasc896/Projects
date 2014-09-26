import utils

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    
    utils.splash("Factorial calc")
    
    n = None
    while not n:
        try:
            n = int(raw_input("n:"))
        except ValueError:
            print "Silly. Enter an int."
            n = None
    
    print "%d! = %d" % (n, factorial(n))
