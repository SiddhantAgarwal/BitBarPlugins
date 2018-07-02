#!/usr/bin/python
import requests
try:
    url = 'https://koinex.in/api/ticker'
    response = requests.get(url)
    json_response = response.json()
    print("KOINEX:BCH:%s|size=12" % json_response['prices']['BCH'])
    print("KOINEX:BTC:%s|size=12" % json_response['prices']['BTC'])
    print("KOINEX:ETH:%s|size=12" % json_response['prices']['ETH'])
    print("KOINEX:XRP:%s|size=12" % json_response['prices']['XRP'])
    print("KOINEX:LTC:%s|size=12" % json_response['prices']['LTC'])
except:
    print("")
def bittrex_processor(pair):
    bittrex_url = 'https://bittrex.com/api/v1.1/public/getticker?market=%s' % (pair)
    obj = requests.get(bittrex_url).json()
    print("BITTREX:%s:%s|size=12" % (pair, obj["result"]["Last"]))
bittrex_processor("BTC-LSK")