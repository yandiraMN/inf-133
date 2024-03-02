from zeep import Client
#saludo
client = Client('http://localhost:8000')
result = client.service.Saludar(nombre="Yandi")
print(result)
#dolar
client = Client('https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL')
resultd = client.service.NumberToDollars(7777)
print(resultd)
#palindromo
client = Client('http://localhost:8000')
resultpalindromo = Client.service.CadenaPalindromo("ana")
print(resultpalindromo)
#suma
client = Client('http://localhost:8000')
resultsuma = client.service.SumaDosNumeros(num1=5, num2=3)
print(resultsuma)