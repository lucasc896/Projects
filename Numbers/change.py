import utils
import math as ma

#+++++++++++++++++++++++++#
# TO-DO
# 1. add some error handling of user inputs
#+++++++++++++++++++++++++#

def coin_calc(val = 0.):

    # change val from pounds to pence for int calcs
    val = int(val*100)

    # ordered list of available coins
    coin_types = [200, 100, 50, 20, 10, 5, 2, 1]
    change = {}
    print "Change for:", val

    bal = val
    for coin in coin_types:
        n_coin = 0
        while coin <= bal:
            n_coin += 1
            bal -= coin
            
        change[coin] = n_coin
    utils.dict_printer(change)
    calcd = 0.
    for key in change:
        calcd += key*change[key]

    if calcd != val:
        print "Something went wrong."
        print val, calcd

    utils.dict_printer(change)


if __name__ == "__main__":

    utils.splash("Change calculator")

    cost = float(raw_input("Cost:"))
    payment = float(raw_input("Payment:"))

    if payment >= cost:
        # coin_calc(payment-cost)
    else:
        exit("Customer not paid enough money.")

