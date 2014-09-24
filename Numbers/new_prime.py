import math as ma

def is_prime(val = None):

    if val == 1:
        return False
    for i in range(2, 1+val/2):
        if val%i == 0:
            return False

    return True

def choice(text = "Do?", default = ""):

    if default == "y":
        choices = "Y/n"
    elif default == "n":
        choices = "y/N"
    else:
        choices = "y/n"

    while True:
        r_in = raw_input("%s [%s]" % (text, choices))

        if not r_in:
            r_in = default

        if r_in in ['y', 'Y', 'yes', 'Yes']:
            return True
        elif r_in in ['n', 'N', 'no', 'No']:
            return False


if __name__ == "__main__":

    my_num = 1
    
    while True:
        if is_prime(my_num):
            print "> Prime number found: %d" % my_num
            if not choice("Find another?", "y"):
                break
        my_num += 1
