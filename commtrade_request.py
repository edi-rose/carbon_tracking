import requests

h = {'authority': 'www.commtrade.co.nz',
'method': 'POST',
'path': '/Default.aspx/GetMarketData',
'scheme': 'https',
'accept': "'application/json', 'text/javascript'",
'accept-encoding': "'gzip', 'deflate', 'br'",
'accept-language': "'en-GB','en-US;' 'q=0.9','en;q=0.8'",
'content-length': '2',
'content-type': 'application/json; charset=UTF-8',
'cookie': 'ASP.NET_SessionId=lvwpnv2fb0cwnqpbnzcazx4l; __CSRFCOOKIE=cd39da08-e916-484c-a3ea-b20552e904ff; ARRAffinity=6bdb0544be6ad143689e1d8612e86f77d444130debf6ee7780bad2c8d637206b; ARRAffinitySameSite=6bdb0544be6ad143689e1d8612e86f77d444130debf6ee7780bad2c8d637206b; __utmc=107546256; __utma=107546256.77344338.1646293274.1646295846.1646299222.3; __utmz=107546256.1646299222.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
'origin': 'https://www.commtrade.co.nz',
'referer': 'https://www.commtrade.co.nz/',
'sec-ch-ua': "'Not;A Brand';v='99', 'Google Chrome';v='97', 'Chromium';v='97'",
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "macOS",
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
'x-requested-with': 'XMLHttpRequest' }

j= {
'authority': 'www.commtrade.co.nz',
'method': 'GET',
'path': '/',
'scheme': 'https',
'accept': "'text/html','application/xhtml+xml','application/xml;q=0.9','image/avif','image/webp','image/apng','*/*;q=0.8','application/signed-exchange;v=b3;q=0.9'",
'accept-encoding': "'gzip', 'deflate', 'br'",
'accept-language': "'en-GB','en-US;q=0.9','en;q=0.8'",
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
r = requests.post("https://www.commtrade.co.nz/", headers=h)

print(r.text)

