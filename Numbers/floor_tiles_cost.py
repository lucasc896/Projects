import math as ma

# note all sizes in m^2
# all costs in pounds

def get_details():

    return {'w': get_value("Width:", float),
            'h': get_value("Height:", float),
            'cost': get_value("Cost per tile:", float),}

def get_value(text = "enter_val", expected_type = None):

    while True:
        r_in = raw_input(text)
        try:
            r_in = expected_type(r_in)
            return r_in
        except ValueError:
            print "Incorrect variable type entered. Expected: %s" % expected_type


def get_cost(d = {}):
    
    for key in ['w', 'h', 'cost', 'tile_area']:
        assert key in d

    total_cost = d['w']*d['h']*d['cost']/d['tile_area']
    return total_cost



if __name__ == "__main__":
    vals = get_details()
    vals['tile_area'] = 0.04 #0.2m squared tiles

    print "\n   > Total cost: %.2f\n" % get_cost(vals)