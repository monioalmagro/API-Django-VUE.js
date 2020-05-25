import requests
#url="https://www.satan.lt/WebServices/Time.asmx"
url = "http://www.subirporno.com/"
#?WSDL
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetRemoteTime xmlns="http://tempuri.org/" />
  </soap:Body>
</soap:Envelope>"""

response = requests.get(url,data=body,headers=headers)
print(response.status_code)
print response.content

cabeza=response.headers#['content-type']
#print(cabeza)
tex=response.text
#print(tex)
#galletas=response.cookies['example_cookie_name']
#print(galletas)