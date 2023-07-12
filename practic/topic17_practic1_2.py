from operator import itemgetter

from plotly.graph_objs import Bar
from plotly import offline

import requests

#Создание вызова API и сохранение ответа 
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Обработка информации о каждой статье
submissions_ids = r.json()

submissions_dicts = []

for submission_id in submissions_ids[:30]:
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
                            reverse=True) 

links, comments = [], []

for submission_dict in submissions_dicts:
    url = submission_dict['hn_link']
    name = submission_dict['title']
    link = f"<a href='{url}'>{name}</a>"
    links.append(link)

    comments.append(submission_dict['comments'])

data = [{
    'type': 'bar', 
    'x': links, 
    'y': comments,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6
}]

my_layout = {
    'title': 'Most-Comment articles on Hacker News', 
    'titlefont': {'size': 28},
    'xaxis': {'title': 'Name',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              }, 
    'yaxis': {'title': 'Comments',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
            }

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn.html')