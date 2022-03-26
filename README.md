# Cumulative Sum

Calculates the cumulative sum for a [datetime, size] array

    with open('data/no2.csv', 'r') as f:
        rows = []
        for tr in f:
            dt,val,*_ = tr.split(';')
            match = re.search(r'[\d\.]+',val)
            if match:
                dt = parser.parse(dt).timestamp()
                rows.append([dt, float(val)])


    cs = Cumsum(rows,100000)
    cs[946910000]
