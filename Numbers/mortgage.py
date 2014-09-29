import utils

class mortgage(object):
    """docstring for mortgage"""
    def __init__(self, deposit, interest, total):
        super(mortgage, self).__init__()
        self.deposit_ = deposit
        self.total_ = total
        self.balance_ = 0.
        self.interest_ = interest
        self.nTerms_ = None

    def calc_monthly(self, nTerms):
        self.balance_ = (self.total - self.deposit_) * 1.+self.interest_
        
        

if __name__ == "__main__":
    utils.splash("Mortgage Calculator")
