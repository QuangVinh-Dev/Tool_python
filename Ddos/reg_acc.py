import requests

url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSft2vX96LSJKvirHmWPVoAMLzXNAdZZZqlb_v1BUKYmL1NeiQ/formResponse',
data = {
    'entry.797325001':'Qvinh',
}
p = requests.post(url,data = data)