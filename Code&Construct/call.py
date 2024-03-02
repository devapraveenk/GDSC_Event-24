import requests

url = 'http://localhost:5000/dev'
data = {'num1':90, 'num2':10}
response = requests.get(url, json=data)

if response.status_code == 200:
    result = response.json()['result']
    print("Result of multiplication:", result)
else:
    print("Error:", response.json())
    # exit()