# Cumulative Sum

Calculates the cumulative sum for a [datetime, size] array

    from dateutil import parser
    import re

    with open('data/no2.csv', 'r') as f:
        rows = []
        for tr in f:
            dt,val,*_ = tr.split(';')
            match = re.search(r'[\d\.]+',val)
            if match:
                dt = parser.parse(dt).timestamp()
                rows.append([dt, float(val)])


    # cum sum over 24 hours
    cs = Cumsum(rows,86400)
    cs[946910000]
