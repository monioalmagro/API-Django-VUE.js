""" from suds.client import Client
client = Client("http://www.w3schools.com/xml/tempconvert.asmx?WSDL")
print client """

from suds.client import Client
client = Client("http://www.w3schools.com/xml/tempconvert.asmx?WSDL")
 
#far_value = event.source.parent.getComponent('Numeric Text Field').floatValue


cels_value = client.service.FahrenheitToCelsius("5")
 
#print (cels_value)