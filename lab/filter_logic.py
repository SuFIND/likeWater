from lab.utils.common import getValueWithDefault
from lab.const.THS_const import cycleIndustry


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
