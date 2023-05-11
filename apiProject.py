import requests
import xmltodict
from urllib.parse import urlparse,parse_qs,urlencode

url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=DRr3Z3dZJqdLd1GnvsPNnStHUzR8%2Bh0eouQ%2Fkdw8IZJaS8cBCDYdPHNKPkFPTN%2F2Zrkr71sWx2WEP3nf3myURA%3D%3D&arsId=03567"
print(parse_qs(urlparse(url).query))

url2 = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?"
params = {'serviceKey': ['DRr3Z3dZJqdLd1GnvsPNnStHUzR8+h0eouQ/kdw8IZJaS8cBCDYdPHNKPkFPTN/2Zrkr71sWx2WEP3nf3myURA=='],
          'arsId': ['03567']}

resURL = url2+urlencode(params)
print(resURL )
# response = requests.get(url)
#
# result = xmltodict.parse(response.text)
# item = result['ServiceResult']['msgBody']['itemList']
#
# arrMsg1 = item['arrmsg1']
# arrMsg2 = item['arrmsg2']
# print(arrMsg1,'/',arrMsg2)

