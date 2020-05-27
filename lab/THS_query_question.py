import datetime
from lab.utils.common import getValueWithDefault


class TongHuaShunQuestionBuilder:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.tgtTimePoint = datetime.datetime(year=year, month=month, day=day)

    def ROEConditionBuild(self, method, **kwargs):
        buff = ''
        if method == 'Hukuba':
            minROE = getValueWithDefault(kwargs, 'minROE', 0.15)
            diffYear = getValueWithDefault(kwargs, 'diffYear', 7)
            if self.tgtTimePoint - datetime.datetime(year=self.year, month=4, day=30) >= datetime.timedelta(days=0):
                # build ROE ≥ 15%
                buff += '{}年到{}年ROE≥{}%，'.format(self.year - diffYear, self.year - 1, minROE * 100)

                # build current year ROE ≥ 3.75*Q %
                if self.tgtTimePoint <= datetime.datetime(year=self.year, month=8, day=30):
                    buff += '{}年3月31日ROE≥{}%，'.format(self.year, round(minROE * 100 / 4, 2))
                elif self.tgtTimePoint <= datetime.datetime(year=self.year, month=10, day=30):
                    buff += '{}年6月30日ROE≥{}%，'.format(self.year, round(minROE * 100 / 4 * 2, 2))
                else:
                    buff += '{}年9月30日ROE≥{}%，'.format(self.year, round(minROE * 100 / 4 * 3, 2))
            else:
                # build ROE ≥ 15%
                buff += '{}年到{}年ROE≥{}%，'.format(self.year - diffYear - 1, self.year - 2, minROE * 100)

                # build current year ROE ≥ 3.75*Q %
                buff += '{}年9月30日ROE≥{}，'.format(self.year - 1, round(minROE * 100 / 4 * 3, 2))
        return buff

    def IPOTimeBuild(self, method, **kwargs):
        buff = ''
        if method == 'Hukuba':
            diffYear = getValueWithDefault(kwargs, 'diffYear', 5)
            buff = '上市时间早于{}年{}月{}日，'.format(self.year - diffYear, self.month, self.day)
        return buff

    def industryBuild(self, method, **kwargs):
        buff = ''
        if method == 'Hukuba':
            buff = '行业，'
        return buff

    def revenueGrowthRateBuild(self, method, **kwargs):
        buff = ''
        if method == 'Hukuba':
            diffYear = getValueWithDefault(kwargs, 'diffYear', 1)
            if self.tgtTimePoint - datetime.datetime(year=self.year, month=4, day=30) >= datetime.timedelta(days=0):
                # last year revenue growth rate
                buff += '{}年营收增长率，'.format(self.year - diffYear)

                # last session revenue growth rate
                if self.tgtTimePoint <= datetime.datetime(year=self.year, month=8, day=30):
                    buff += '{}年3月31日营收增长率，'.format(self.year)
                elif self.tgtTimePoint <= datetime.datetime(year=self.year, month=10, day=30):
                    buff += '{}年6月30日营收增长率，'.format(self.year)
                else:
                    buff += '{}年9月30日营收增长率，'.format(self.year)
            else:
                # build ROE ≥ 15%
                buff += '{}年营收增长率，'.format(self.year - diffYear - 1)

                # build current year ROE ≥ 3.75*Q %
                buff += '{}年9月30日营收增长率，'.format(self.year - 1)

        return buff

    def netProfitGrowthRateBuild(self, method, **kwargs):
        buff = ''
        if method == 'Hukuba':
            diffYear = getValueWithDefault(kwargs, 'diffYear', 1)
            if self.tgtTimePoint - datetime.datetime(year=self.year, month=4, day=30) >= datetime.timedelta(days=0):
                # last year revenue growth rate
                buff += '{}年净利润增长率，'.format(self.year - diffYear)

                # last session revenue growth rate
                if self.tgtTimePoint <= datetime.datetime(year=self.year, month=8, day=30):
                    buff += '{}年3月31日净利润增长率，'.format(self.year)
                elif self.tgtTimePoint <= datetime.datetime(year=self.year, month=10, day=30):
                    buff += '{}年6月30日净利润增长率，'.format(self.year)
                else:
                    buff += '{}年9月30日净利润增长率，'.format(self.year)
            else:
                # build ROE ≥ 15%
                buff += '{}年净利润增长率，'.format(self.year - diffYear - 1)

                # build current year ROE ≥ 3.75*Q %
                buff += '{}年9月30日净利润增长率，'.format(self.year - 1)
        return buff

    def operatingIncomeBuild(self, method, **kwargs):
        buff = ''
        if method == 'Hukuba':
            diffYear = getValueWithDefault(kwargs, 'diffYear', 3)
            if self.tgtTimePoint - datetime.datetime(year=self.year, month=4, day=30) >= datetime.timedelta(days=0):
                buff += '{}年到{}年的营业收入，'.format(self.year - diffYear - 1, self.year - 1)

            else:
                buff += '{}年到{}年的营业收入，'.format(self.year - diffYear - 2, self.year - 2)
        return buff

    def accountsReceivableBuild(self, method, **kwargs):
        buff = ''
        if method == 'Hukuba':
            diffYear = getValueWithDefault(kwargs, 'diffYear', 3)
            if self.tgtTimePoint - datetime.datetime(year=self.year, month=4, day=30) >= datetime.timedelta(days=0):
                buff += '{}年到{}年的应收账款，'.format(self.year - diffYear - 1, self.year - 1)

            else:
                buff += '{}年到{}年的应收账款，'.format(self.year - diffYear - 2, self.year - 2)
        return buff

    def inventoryBuild(self, method, **kwargs):
        buff = ''
        if method == 'Hukuba':
            diffYear = getValueWithDefault(kwargs, 'diffYear', 3)
            if self.tgtTimePoint - datetime.datetime(year=self.year, month=4, day=30) >= datetime.timedelta(days=0):
                buff += '{}年到{}年的存货，'.format(self.year - diffYear - 1, self.year - 1)

            else:
                buff += '{}年到{}年的存货，'.format(self.year - diffYear - 2, self.year - 2)
        return buff

    def liquidityRatioBuild(self, method, **kwargs):
        buff = ''
        if method == 'Hukuba':
            diffYear = getValueWithDefault(kwargs, 'diffYear', 2)
            template = '{}年到{}年的流动比率，'
            if self.tgtTimePoint - datetime.datetime(year=self.year, month=4, day=30) >= datetime.timedelta(days=0):
                buff += template.format(self.year - diffYear - 1, self.year - 1)
            else:
                buff += template.format(self.year - diffYear - 2, self.year - 2)
        return buff

    def buildHukubaStockQuery(self):
        buff = ''
        method = 'Hukuba'
        buff += self.ROEConditionBuild(method)
        buff += self.IPOTimeBuild(method)
        buff += self.industryBuild(method)
        buff += self.revenueGrowthRateBuild(method)
        buff += self.netProfitGrowthRateBuild(method)
        buff += self.operatingIncomeBuild(method)
        buff += self.accountsReceivableBuild(method)
        buff += self.inventoryBuild(method)
        buff += self.liquidityRatioBuild(method)
        if buff[-1] == '，':
            buff = buff[:-1]
        return buff


if __name__ == '__main__':
    t = TongHuaShunQuestionBuilder(year=2020, month=3, day=25)
    question = t.buildHukubaStockQuery()
    print(question)