import requests
from bs4 import BeautifulSoup

url = "https://mangalib.me/fire-punch/v6/c59?bid=7617&ui=6484159"
payload = {}
headers = {
  'sec-ch-ua-platform': '"Windows"',
  'Referer': 'https://mangalib.me/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
  'sec-ch-ua-mobile': '?0'
}

response = requests.request("GET", url, headers=headers, data=payload)

html_content = response.text

#with open("text.txt", "a", encoding='utf-8') as file:
soup = BeautifulSoup(html_content, 'html.parser')
#file.write(soup.prettify())
print(soup.prettify())

# payload = "{\"memory\":{\"totalJSHeapSize\":40553750,\"usedJSHeapSize\":25056494,\"jsHeapSizeLimit\":4294705152},\"resources\":[],\"referrer\":\"https://mangalib.me/?section=home-updates-6484159\",\"eventType\":1,\"firstPaint\":1055.9000000357628,\"firstContentfulPaint\":1055.9000000357628,\"startTime\":1729894003094.2,\"versions\":{\"fl\":\"2024.10.4\",\"js\":\"2024.6.1\",\"timings\":2},\"pageloadId\":\"10a11ea7-eff7-44dc-a953-51eb60901927\",\"location\":\"https://mangalib.me/salangbadneun-magnaeneun-cheoeum-ila/v1/c44\",\"nt\":\"reload\",\"serverTimings\":[{\"name\":\"cfCacheStatus\",\"dur\":0,\"desc\":\"DYNAMIC\"}],\"timingsV2\":{\"unloadEventStart\":934.6000000238419,\"unloadEventEnd\":934.6000000238419,\"domInteractive\":1123.9000000357628,\"domContentLoadedEventStart\":1126.2000000476837,\"domContentLoadedEventEnd\":1126.7000000476837,\"domComplete\":3183.900000035763,\"loadEventStart\":3184,\"loadEventEnd\":3184.800000011921,\"type\":\"reload\",\"redirectCount\":0,\"criticalCHRestart\":0,\"activationStart\":0,\"initiatorType\":\"navigation\",\"nextHopProtocol\":\"h2\",\"deliveryType\":\"\",\"workerStart\":1.100000023841858,\"redirectStart\":0,\"redirectEnd\":0,\"fetchStart\":1.300000011920929,\"domainLookupStart\":2.600000023841858,\"domainLookupEnd\":77.10000002384186,\"connectStart\":77.10000002384186,\"connectEnd\":739.7000000476837,\"secureConnectionStart\":621.4000000357628,\"requestStart\":739.7000000476837,\"responseStart\":924.3000000119209,\"responseEnd\":995.1000000238419,\"transferSize\":11225,\"encodedBodySize\":10925,\"decodedBodySize\":50113,\"responseStatus\":200,\"firstInterimResponseStart\":0,\"renderBlockingStatus\":\"non-blocking\",\"name\":\"https://mangalib.me/salangbadneun-magnaeneun-cheoeum-ila/v1/c44?ui=6484159\",\"entryType\":\"navigation\",\"startTime\":0,\"duration\":3184.800000011921},\"dt\":\"\",\"siteToken\":\"fa664a6268b54b7f88d83c9349c63781\",\"st\":2}"
# headers = {
#   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#   'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#   'cache-control': 'max-age=0',
#   'cookie': '_ym_uid=1728641114256590319; _ym_d=1728641114; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6Ik02QzVFS05nQUN0ODBMZzNpeG94WGc9PSIsInZhbHVlIjoielljNHFmeitFS3htWkE0aUhlTWJ1b0dld0xEVmFGVGJwSngzaDl2MXBLNURXL2lSaEJFUHZZb1JxRSsxYXBDL0t3UnlhQ1Y2RklSaU9ES0h4cEJVa3djZFdPK3pUQVd5UzZlUzlUajI1b1BmRkwvRmNJVmpjMk01WmpKZGowVmtqcmFUL0ZadDhLNFc0NkxlQkhvRTFuOFlMRUlKb2E0MEVoWkZna05MTzcrTHVIcTlKTEYwR1NLNnJJWU9NOVJReWdJMXQ1R3pNbnFKQXI3dlRMZnkzbmhvNncrYUlnZkNERzBDN2hGQ0lEcz0iLCJtYWMiOiIwYjJhOGUzNTY2N2I3OWUyMDNkZWRhY2JkMmMwOTAyZjc4ZWIyOTA1NjQ5ZTgzZWQ3NmFlZmZkMmQ5ODliZTQzIiwidGFnIjoiIn0%3D; _gid=GA1.2.449861603.1729850873; _ym_isad=2; _ym_visorc=b; _ga_SF8S8RTHBE=GS1.1.1729892552.9.1.1729893364.58.0.0; _ga=GA1.1.1051355117.1728641114; cf_clearance=xZDz.zhnWdmvWJJuobTUq21tgRXS_6UP4CURo3iyDrg-1729893368-1.2.1.1-ip42LKlK7Ns79jThMOb43jMTEgSa38lRmMrmG2T_XLwdPB4L4TzRmS_ALVCVrmOHw_vw4ArKyYaMPPqDIxaW3Nlzu2Lrem8drBVkqmTNs09NXcWCGhNhp7mqEJf9FGzmgofYf6KZG1IMS.wFOJoG6K2IU2SX3PRI.pzYG8Xb2jKtxXohmx_IEGeisGFRKNrz4vw6qMIpxaVwAThW3Wzhwf0UAQaoDJT.IJr_PkQo2oHI0AaP84g93wrOm0q72nCiKwqkayZpC.OXmxU9u7hGzdlqtE5Uh6UD1E_q28EUfaE_XMciZIQtsfqWkKuav8HtkSO1VkoerWOZ7UX_cjbBLWR6.D0wr1OecE6su3Xi3tzHwnSFa.kh5oLZ_Qf208j0; XSRF-TOKEN=eyJpdiI6Ik9ZOXRiL0xTK0c0RXFDQ080UEREanc9PSIsInZhbHVlIjoidHRlUUhHQzJZWkE4Nit6cVRrdnRrL0Qyc3I5WUhYNlNNSGs3RE5VbFBMM3V4RXJOMjBOOURsSlNaUnoyTUg4czZOUTd2cDRzNjFzRHR6RENQVVY1MHYvYm9uVk9LZjd2c1F6ZHllYUtpelFRaXNJMWhmVWRIVU0rdDhkbW1GNHYiLCJtYWMiOiI3MDRiYzAzMDcwNmM5YTRjNDMzMGY3YTljNWI3MWQ1ZGFmZmVkYmU0YWY1ODAzODc4ZGIwZTkwMTAzNmI0NDVmIiwidGFnIjoiIn0%3D; mangalib_session=eyJpdiI6IkVRdGoreE4vb0VOM2RsWEtveHlTOHc9PSIsInZhbHVlIjoicG1XNGcvTHRaVkg2eFhzdHFlSTcxRFcrVU43anNBdjc0TEd2VHpBOFZUdVZPZkdDVzJ2cnVDL1FLaHRIT1VnUm1aTE5CZVRxVmFOUHducnZWemFmcm5jaGo1UmVrSTNidUxBZ1NkT05zT2ZrYk1xNktYMVBmcVJNeElkdEc2dGQiLCJtYWMiOiJmODE4ZGU1ZmMyZjU0YTc5NTUzMmM1OTc4ZmMyODViZDZhMzRmYTI3ZjMyMzVhZjY1NmY0ZmJhZWZiNjlkYzYxIiwidGFnIjoiIn0%3D',
#   'priority': 'u=0, i',
#   'referer': 'https://mangalib.me/?section=home-updates-6484159',
#   'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'document',
#   'sec-fetch-mode': 'navigate',
#   'sec-fetch-site': 'same-origin',
#   'sec-fetch-user': '?1',
#   'upgrade-insecure-requests': '1',
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
#   'Referer': 'https://mangalib.me/',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
#   'x-client-data': 'CKO1yQEIh7bJAQiltskBCKmdygEI0OfKAQiVocsBCPaiywEI9JjNAQiFoM0BCJPGzgEI08fOAQinyM4BCIjJzgEImMrOAQ==',
#   'Origin': 'https://mangalib.me',
#   'origin': 'https://mangalib.me',
#   'Upgrade-Insecure-Requests': '1',
#   'x-browser-channel': 'stable',
#   'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
#   'x-browser-validation': 'QTcFh+5ZedCCidQkKanqiUwPHQo=',
#   'x-browser-year': '2024',
#   'content-length': '0',
#   'content-type': 'text/plain'
# }