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
        'filterCycleIndustry': {'func': fl.filterCycleIndustry, 'exArgs': []},
        'filterFundamentals': {'func': fl.filterFundamentals, 'exArgs': []},
        'filterBearCondition01': {'func': fl.filterBearCondition01, 'exArgs': []},
        # 'filterBearCondition02': {'func': None, 'args': None},
        # 'filterBearCondition03': {'func': None, 'args': None},
    }
    for one in pipeLine:
        if one in method:
            func = method[one]['func']
            exArgs = method[one]['exArgs']
            args = [buffData] + exArgs
            buffData = func(*args)
    return buffData


if __name__ == '__main__':
    THS_url = 'http://search.10jqka.com.cn/unifiedwap/unified-wap/result/get-stock-pick'
    initDataSource(THS_url)
    THSService = globalState['THSService']
    data = getSource(THSService, 2020, 5, 28)
    rst = dataPipeLine(data, pipeLine=['filterCycleIndustry', 'filterFundamentals', 'filterBearCondition01'])
    print(1)
