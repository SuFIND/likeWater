from lab.basic_data import TongHuaShunService
from lab.THS_query_question import TongHuaShunQuestionBuilder
import lab.filter_logic as fl
global globalState
globalState = {}


def initDataSource(THSUrl):
    globalState['THSService'] = TongHuaShunService(THSUrl)


def getSource(THSService, year, month, day):
    tool0 = TongHuaShunQuestionBuilder(year, month, day)
    rs0 = tool0.buildHukubaStockQuery()
    THSService.buildForm(rs0, 100)
    apiData0 = THSService.buildStockRequest()
    return apiData0


def dataPipeLine(data, pipeLine=None):
    if pipeLine is None:
        pipeLine = []
    buffData = data
    method = {
        'filterCycleIndustry': {'func': fl.filterCycleIndustry, 'args': [buffData]},
        # 'filterBearCondition01': {'func': None, 'args': None},
        # 'filterBearCondition02': {'func': None, 'args': None},
        # 'filterBearCondition03': {'func': None, 'args': None},
    }
    for one in pipeLine:
        if one in method:
            func = method[one]['func']
            args = method[one]['args']
            buffData = func(*args)


if __name__ == '__main__':
    THS_url = 'http://search.10jqka.com.cn/unifiedwap/unified-wap/result/get-stock-pick'
    initDataSource(THS_url)
    THSService = globalState['THSService']
    data = getSource(THSService, 2020, 5, 28)
    dataPipeLine(data, pipeLine=['filterCycleIndustry'])