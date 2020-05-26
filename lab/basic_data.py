#!/usr/bin/python
# -- coding: utf-8 --**

import requests
from lab.utils.common import getValueWithDefault
from lab.utils.type_trans import transStr, transNumber, transDatetime

# 同花顺i问财股票查询api
url_01 = 'http://search.10jqka.com.cn/unifiedwap/unified-wap/result/get-stock-pick'


class TongHuaShunService(object):
    def __init__(self, url):
        self.url = url
        self.transMap = {
            'STR': transStr,
            'DOUBLE': transNumber,
            'DATE': transDatetime
        }

    def buildStockRequest(self, form: dict, **kwargs):
        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        r = requests.post(self.url, data=form, headers=headers)
        response = r.json()
        if 'status_msg' not in response or response['status_msg'] != 'ok':
            msg = 'TongHuaShun Stock Data Get Error!'
            raise Exception(msg)
        tgt = self.parseStockResponse(response)
        return tgt

    def parseStockResponse(self, response):
        tgt = []
        data = getValueWithDefault(response, 'data', {})
        config = getValueWithDefault(data, 'config', {})
        configurationData = getValueWithDefault(config, 'configuration_data', {})
        items = getValueWithDefault(data, 'data', [])
        for itemIdx, item in enumerate(items):
            buff = {}
            for k, v in item.items():
                columnCfg = getValueWithDefault(configurationData, k, {})
                dataType = getValueWithDefault(columnCfg, 'type', 'STR')
                newV = self.transMap[dataType](v)
                buff.update({k: newV})
            tgt.append(buff)
        return tgt

form = {
    'question': '2013年到2019年ROE≥15%，2020年3月31日ROE≥3.75%，上市时间早于2015年5月25日，行业，2020年3月31日营收增长率，2020年3月31日净利润增长率，2019年营收增长率，2019年净利润增长率，2016年到2019年的营业收入，2016年到2019年的应收账款，2016年到2019年的存货，2017年到2019年的流动比率',
    'secondary_intent': 'stock',
    'condition_id': None,
    'perpage': 50,
}

if __name__ == '__main__':
    r = TongHuaShunService(url_01)
    rst = r.buildStockRequest(form)
    print(1)
