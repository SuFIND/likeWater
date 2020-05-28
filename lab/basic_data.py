#!/usr/bin/python
# -- coding: utf-8 --**
import re
import requests
from lab.utils.common import getValueWithDefault
from lab.utils.type_trans import transStr, transNumber, transDatetime
from lab.const.THS_const import tableHeadMap


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
        self.form = {
            'question': '',
            'secondary_intent': 'stock',
            'condition_id': None,
            'perpage': 50,
        }

    def columnNameParse(self, columnName):
        reRst = re.match(r'(?P<column>.*)\[(?P<date>.*)\]', columnName)
        column = columnName
        if reRst:
            column = reRst.group('column')
        column = getValueWithDefault(tableHeadMap, column, '')
        if reRst and column != '':
            dateStr = reRst.group('date')
            column += '[{}]'.format(dateStr)
        return column

    def buildStockRequest(self, **kwargs):
        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        r = requests.post(self.url, data=self.form, headers=headers)
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
                newK = self.columnNameParse(k)
                if newK == '':
                    continue
                columnCfg = getValueWithDefault(configurationData, k, {})
                dataType = getValueWithDefault(columnCfg, 'type', 'STR')
                newV = self.transMap[dataType](v)
                buff.update({newK: newV})
            tgt.append(buff)
        return tgt

    def buildForm(self, question: str, maxCnt: int):
        self.form['question'] = question
        self.form['maxCnt'] = maxCnt
