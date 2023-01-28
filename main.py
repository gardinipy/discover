import requests


site = input('site: ')
wordlist = input('Wordlist: ')

arquivo = open(wordlist)

for d in arquivo.readlines():
    requisicao = requests.get(site+"/"+d.replace('\n',''))
    print(requisicao.url+" = "+str(requisicao.status_code))
