from zeep import Client

client = Client('http://localhost:8000')
result = client.service.SumaDosNumeros(num1=5, num2=3)
print(result)
