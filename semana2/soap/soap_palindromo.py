from zeep import Client
client = Client('http://localhost:8000')
result = Client.service.CadenaPalindromo("ana")
print(result)