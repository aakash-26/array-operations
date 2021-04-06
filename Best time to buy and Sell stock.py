
"""
Best time to buy and Sell stock
"""

print("\n ---------- Best time to buy and Sell stock ----------")


def return_sell_day(l):
    buy_day = None
    req_day = None
    flag = True
    if len(l) > 1:
        for z in l:
            if flag:
                if not buy_day:
                    buy_day = z

                elif z > buy_day:
                    buy_day = z

                elif z < buy_day:
                    flag = False
        req_day = l.index(buy_day)

    return req_day


def return_buy_day(l):
    buy_day = None
    req_day = None
    flag = True
    if len(l) > 1:
        for z in l:
            if flag:
                if not buy_day:
                    buy_day = z

                elif z < buy_day:
                    buy_day = z

                elif z > buy_day:
                    flag = False
        req_day = l.index(buy_day)

    return req_day


def stock(a):
    # print("a",a)
    res = []
    b = return_buy_day(a)
    # print("b",b)
    if b is not None:
        # print("inside b")
        s = return_sell_day(a[b:])
        if s:
            # print("b s",b,s)
            res.append([a[b], a[s]])
            # print("res 0",res)
            a = a[s + 1:]
            if len(a) > 1:

                res += stock(a)
                return res
            else:
                # print("res 1",res)
                return res

    else:
        # print("res 2",res)
        return res


if __name__ == "__main__":

    a = [100, 180, 260, 310, 40, 535, 695]
    s = stock(a)
    # print("stock",stock(a))

    if s:
        for days in s:
            print("Day of buy : ", a.index(days[0]) + 1)
            print("Day of sell : ", a.index(days[1]) + 1)
            print("")

