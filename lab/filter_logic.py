from lab.utils.common import getValueWithDefault
from lab.const.THS_const import cycleIndustry
import re


def filterCycleIndustry(data):
    newData = []
    for dataOne in data:
        canSave = True
        industry = getValueWithDefault(dataOne, 'industry', '')
        if industry in cycleIndustry:
            canSave = False
        if canSave:
            newData.append(dataOne)
    return newData


def filterFundamentals(data):
    newData = []
    for dataOne in data:
        canSave = True
        for k, v in dataOne.items():
            reRst0 = re.match('operating_income\(YoY GR\)\[(?P<time>.*)\]', k)
            if reRst0:
                if v < 0:
                    canSave = False
                    break
            reRst1 = re.match('net_profit_attributable_to_shareholders_of_parent_company\(YoY GR\)\[(?P<time>.*)\]', k)
            if reRst1:
                if v < 0:
                    canSave = False
                    break

        if canSave:
            newData.append(dataOne)
    return newData


def filterBearCondition01(data):
    newData = []
    for dataOne in data:
        cache = {
            'operating_income': [],
            'accounts_receivable': []
        }
        for k, v in dataOne.items():
            reRst = re.match('(?P<name>.*)\[(?P<time>.*)\]', k)
            if reRst:
                buff = reRst.groupdict()
                buff['val'] = v
                if buff.get('name') not in cache:
                    continue
                cache[buff['name']].append(buff)
        operatingIncome = cache['operating_income']
        accountsReceivable = cache['accounts_receivable']
        operatingIncome.sort(key=lambda x: x['time'], reverse=True)
        operatingIncome = [one['val'] for one in operatingIncome]
        accountsReceivable.sort(key=lambda x: x['time'], reverse=True)
        accountsReceivable = [one['val'] for one in accountsReceivable]

        # 营业收入增长额 和 应收账款增长额
        operatingIncomeBuff = diffSub(operatingIncome)
        accountsReceivableBuff = diffSub(accountsReceivable)

        prevRst = None
        isBad = False
        for idx, one in enumerate(operatingIncomeBuff):
            a = accountsReceivableBuff[idx]
            b = operatingIncomeBuff[idx]
            currRst = a - b
            if prevRst is None:
                prevRst = currRst
                continue
            if prevRst > 0 and currRst > 0:
                isBad = True
                break

        if not isBad:
            newData.append(dataOne)
    return newData


def diffSub(tgt: list):
    rst = []
    tgtMaxIdx = len(tgt) - 1
    for idx, one in enumerate(tgt):
        if tgtMaxIdx == idx - 1:
            rst.append(0)
        base = one
        diff = tgt[idx - 1]
        new = base - diff
        rst.append(new)
    return rst
