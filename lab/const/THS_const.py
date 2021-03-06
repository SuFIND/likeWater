# i WenCai table map
tableHeadMap = {
    '股票代码': 'code',
    '股票简称': 'name',
    '最新价': 'last_price',
    '最新涨跌幅': 'last_change_percentage',
    '净资产收益率roe(加权,公布值)': 'ROE_weighted_published',
    '新股上市日期': 'IPO_time',
    '所属同花顺行业': 'industry',
    '营业收入': 'operating_income',
    '应收票据及应收账款': 'accounts_receivable',
    '存货': 'inventory',
    '流动比率': 'capital_flow_ratio',
    '营业收入(同比增长率)': 'operating_income(YoY GR)',
    '归属母公司股东的净利润(同比增长率)': 'net_profit_attributable_to_shareholders_of_parent_company(YoY GR)',
}

cycleIndustry = {'采掘-采掘服务-其他采掘服务', '采掘-采掘服务-油气钻采服务', '黑色金属-钢铁-普钢', '黑色金属-钢铁-特钢',
                 '化工-化工合成材料-氨纶', '化工-化工合成材料-涤纶', '化工-化工合成材料-改性塑料', '化工-化工合成材料-合成革',
                 '化工-化工合成材料-轮胎', '化工-化工合成材料-其他塑料制品', '化工-化工合成材料-其他纤维',
                 '化工-化工合成材料-其他橡胶制品', '化工-化工合成材料-炭黑', '化工-化工合成材料-维纶', '化工-化工合成材料-粘胶',
                 '化工-化工新材料-玻纤', '化工-化工新材料-聚氨酯', '采掘-石油矿业开采-其他采掘Ⅲ', '采掘-石油矿业开采-石油开采Ⅲ',
                 '有色金属-有色冶炼加工-黄金', '有色金属-有色冶炼加工-铝', '有色金属-有色冶炼加工-铅锌', '有色金属-有色冶炼加工-铜',
                 '有色金属-有色冶炼加工-小金属', '化工-化学制品-氮肥', '化工-化学制品-纺织化学用品', '化工-化学制品-氟化工及制冷剂',
                 '化工-化学制品-复合肥', '化工-化学制品-钾肥', '化工-化学制品-磷肥', '化工-化学制品-磷化工及磷酸盐',
                 '化工-化学制品-民爆用品', '化工-化学制品-农药', '化工-化学制品-其他化学制品', '化工-化学制品-日用化学产品',
                 '化工-化学制品-涂料油漆油墨制造', '交通运输-港口航运-港口Ⅲ', '交通运输-港口航运-航运Ⅲ', '交通运输-机场航运-航空运输Ⅲ',
                 '交通运输-机场航运-机场Ⅲ', '交运设备-交运设备服务-汽车服务', '国防军工-国防军工-船舶制造', '国防军工-国防军工-地面兵装',
                 '国防军工-国防军工-航空装备', '交运设备-汽车整车-乘用车', '交运设备-汽车整车-商用载货车', '交运设备-汽车整车-商用载客车',
                 '交运设备-汽车零部件-汽车零部件Ⅲ', '建筑材料-建筑材料-玻璃制造', '建筑材料-建筑材料-管材', '建筑材料-建筑材料-耐火材料',
                 '建筑材料-建筑材料-其他建材', '建筑材料-建筑材料-水泥制造', '建筑材料-建筑装饰-房屋建设', '建筑材料-建筑装饰-基础建设',
                 '建筑材料-建筑装饰-专业工程', '建筑材料-建筑装饰-装饰园林', '房地产-房地产开发-房地产开发Ⅲ', '房地产-园区开发-园区开发Ⅲ',
                 '金融服务-证券-证券Ⅲ', '金融服务-保险及其他-保险Ⅲ', '金融服务-保险及其他-多元金融'}
