import utils

def get_sum_digits(val):
    val_str = str(val)
    total = 0
    for i in val_str:
        total += int(i)
    return total

def is_happy(num):
    while num >= 10:
        num = get_sum_digits(num)

    return True if num == 1 else False

if __name__ == "__main__":
    utils.splash("Happy Numbers")
    
    num = utils.get_val_of_type("int", "Number:")

    if num > 0.:
        if is_happy(num):
            print "%d is a happy number!" % num
        else:
            print "%d is a sad number." % num
    else:
        print "Finding first 8 happy numbers...\n"
        found = 0
        num = 10
        while found < 8:
            if is_happy(num):
                print num
                found += 1
            num += 1
