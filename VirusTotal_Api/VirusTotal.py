from hashlib import md5
from virus_total_apis import PublicApi

API_KEY = '8760197ef2190aadbdf291059dd0a374397fbd6c9af460648395571dcb69ed9e'

api = PublicApi(API_KEY)

with open ("requerimientos.txt", "rb") as file:
    file_hash = md5(file.read()).hexdigest()
response = api.get_file_report(file_hash)

if response["response_code"] == 200:
    if response["results"]["positives"] > 0:
        print("Archivo malicioso detectado en más de " , response["results"]["positives"], " antivirus")
    else:
        print("Archivo seguro.", response["results"]["positives"])
else:
    print("No ha podido obtenerse el análisis del archivo.")
