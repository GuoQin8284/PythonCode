import requests

url=("http://127.0.0.1:8000/api/departments/T2016N/")

mydata={
		"data": [
				{
					"dep_id":"T01",
					"dep_name":"Test学院",
					"master_name":"Test-Master",
					"slogan":"Here is Slogan"
				}
			]
		}

respous=requests.put(url,json=mydata)

print(respous.json())