import utils

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    
    utils.splash("Factorial calc")
    
    n = utils.get_val_of_type("int", "n:")
    
    print "%d! = %d" % (n, factorial(n))
