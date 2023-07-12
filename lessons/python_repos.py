import requests

#Создание вызова API и сохранение ответа 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github+json'} #заголовок указывает на то, какую 
#информацию мы хотим получить с сервера и в каком формате
r = requests.get(url, headers=headers) 
print(f"Status code: {r.status_code}") #код 200 - признак успешного ответа

#Сохранение API в переменной
response_dict = r.json() #т.к. информация возвращается в формате json, 
#поэтому используется метод json, чтобы преобразовать информацию в словари
print(f"Total repositories: {response_dict['total_count']}")

#Анализ информации о репозиториях
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}") #сколько всего репозиториев
#найдено (ко скольким есть доступ)

print("\nSelected information about each repository:")
for repo_dict in repo_dicts: #информация о всех доступных репозиториях
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

#Анализ первого репозитория
#repo_dict = repo_dicts[0]
#print(f"\nKeys: {len(repo_dict)}")
#for key in sorted(repo_dict.keys()): #заголовки, по которым можно понять, какую 
    #информацию можно вытащить
    #print(key)