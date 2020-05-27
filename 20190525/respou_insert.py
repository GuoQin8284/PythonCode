import requests

url=("http://127.0.0.1:8000/api/departments/")

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

respous1=requests.post(url,json=mydata)

print(respous1.json())