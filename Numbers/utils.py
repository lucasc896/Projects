import math as ma

def splash(title = "program splash", author = "Chris Lucas"):
    # can definitely clean up

    length = len(title)
    # if length is odd, add whitespace
    if length%2:
        title += " "
        length = len(title)

    width = length+16
    print "=" * width
    print "*%s*" % (" "*(width-2))
    print "*%s%s%s*" % (" "*((width-2-length)/2), title, " "*((width-2-length)/2)) # change to format!
    print "*%s*" % (" "*(width-2))
    print "=" * width

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

# for dev testing
if __name__ == "__main__":
    splash("helloxss")