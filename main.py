from pip._vendor import requests

print('hello world')

# mencoba fundamental python
try:
    r = requests.get('https://google.com')
    print(r.status_code)
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('404', e)