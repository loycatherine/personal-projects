import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'volatile acidity':0.27, 'citric acid':0.13, 'sulphates':0.67, 'alcohol':11.9})

print(r.json())