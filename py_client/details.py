import requests



endpoint="http://127.0.0.1:8000/products/7/"
#for get
#get_response = requests.get(endpoint, json={"product_id": 123}) #Http get requests #API--application programming Interface
get_response = requests.get(endpoint, json={"title": "hello_world"})
#print(get_response.text)
#print(get_response.status_code) 
print(get_response.json())