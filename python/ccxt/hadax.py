# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.huobipro import huobipro


class hadax (huobipro):

    def describe(self):
        return self.deep_extend(super(hadax, self).describe(), {
            'id': 'hadax',
            'name': 'HADAX',
            'countries': 'CN',
            'hostname': 'api.hadax.com',
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/38059952-4756c49e-32f1-11e8-90b9-45c1eccba9cd.jpg',
                'api': 'https://api.hadax.com',
                'www': 'https://www.hadax.com',
                'doc': 'https://github.com/huobiapi/API_Docs/wiki',
            },
            'api': {
                'public': {
                    'get': [
                        'hadax/common/symbols',  # 查询系统支持的所有交易对
                        'hadax/common/currencys',  # 查询系统支持的所有币种
                        'common/timestamp',  # 查询系统当前时间
                    ],
                },
            },
        })

    def fetch_markets(self):
        response = self.publicGetHadaxCommonSymbols()
        return self.parseMarkets(response['data'])
