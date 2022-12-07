import requests
response = requests.get("http://pytalk.c1.biz/api/js/read_all.php?key=redmi123")

print(response.status_code)

if response.status_code == 200:
    print(response.text)