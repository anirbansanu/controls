import requests

def fetch(key):
    response = requests.get("http://pytalk.c1.biz/api/js/read_all.php?key="+key)

    print(response.status_code)

    if response.status_code == 200:
        print(int(response.text.replace('"','')))

def update(key,text):
    response = requests.get("http://pytalk.c1.biz/api/js/update.php?key="+key+"&text="+text)

    print(response.status_code)

    if response.status_code == 200:
        print(response.text)

fetch("redmi123")
update("redmi123","1")
fetch("redmi123")