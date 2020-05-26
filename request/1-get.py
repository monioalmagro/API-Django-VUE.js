import requests

""" url = 'http://localhost:8000/api/v1.0/books/'
"""
#url = 'https://www.satan.lt/WebServices/Time.asmx'
#url = "http://www.cfdiauribox.com/PruebasCFDI33/services/ServicioTimbrado1?wsdl"
#url = 'http://www.explorecalifornia.org/pox/tours.php'
#url = 'http://services.explorecalifornia.org/pox/tours.php?packgeid=1'
#url = 'http://www.webservicex.net/'

#url = 'http://www.webservicex.net/globalweather.asmx?WSDL'
#url = 'http://webservice11.somee.com/WebService1.asmx?WSDL'
url = 'https://www.w3schools.com/xml/tempconvert.asmx?WSDL'
res = requests.get(url)
#print(res)
#print(res.content)
cabeza=res.headers
#print(cabeza)
tex=res.text
print(tex)

