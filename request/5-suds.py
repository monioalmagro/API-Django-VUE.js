
#Import the SUDS Client object
from suds.client import Client
  
#Instantiate a new Client Object
client = Client("https://cvnet.cpd.ua.es/servicioweb/publicos/pub_gestdocente.asmx?wsdl")
print client
#Call the desired method using the service instance variable
#client.service.MyMethod(myArgument)