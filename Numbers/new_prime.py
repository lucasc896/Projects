import math as ma
import utils

if __name__ == "__main__":

    # start the number at 1
    my_num = 1
    
    while True:
        if utils.is_prime(my_num):
            print "> Prime number found: %d" % my_num
            if not utils.choice("Find another?", "y"):
                break
        # increment is prime not found or user wants to continue
        my_num += 1
