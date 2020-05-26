from decimal import Decimal
from dateutil.parser import parse


def transNumber(val):
    rst = val
    try:
        if val in ['--', '-', None]:
            val = '0'
        buff = str(val)
        rst = Decimal(buff)
    except:
        pass
    return rst


def transStr(val):
    rst = val
    try:
        rst = str(val)
    except:
        pass
    return rst


def transDatetime(val):
    rst = val
    try:
        rst = parse(val)
    except:
        pass
    return rst
