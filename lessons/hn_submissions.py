from operator import itemgetter

import requests

#Создание вызова API и сохранение ответа 
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Обработка информации о каждой статье
submissions_ids = r.json()

submissions_dicts = []
for submission_id in submissions_ids[:5]:
    #Создание отдельного вызова API для каждой статьи
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    #Построение словаря для каждой статьи 
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants']
    }
    submissions_dicts.append(submission_dict)

submissions_dicts = sorted(submissions_dicts, key=itemgetter('comments'), 
                            reverse=True) #сортируем по кол-ву комментариев (key=itemgetter('comments'))
                            #чтобы статьи с наибольшим кол-м комментариев были в начале, то мы пишем
                            #reverse=True

for submission_dict in submissions_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")