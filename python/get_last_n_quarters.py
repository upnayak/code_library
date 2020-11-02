def get_last_n_quarters(quarter, n):
    """
    Keyword arguments:
    quarter -- quarter of the year ex: 20201, 20204, 20193 etc
    n -- number of quarter to go back from the input

    output: 
    -- list of last n quarters

    Example: 
    >>>get_last_n_quarters('20201', 6)
    ['20194', '20193', '20192', '20191', '20184', '20183']
    """
    thisYear = int(quarter[:4])
    quarterStart = int(quarter[-1])
    last_n_quarters=[]
    for _ in range(n):
        quarterStart -= 1
        if (quarterStart <= 0):
            thisYear -= 1
            quarterStart = 4
        last_n_quarters.append("{}{}".format(thisYear,quarterStart))
    return last_n_quarters

get_last_n_quarters('20201', 6)
