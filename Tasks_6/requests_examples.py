import requests


 
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)
 
# просмотр нового массива `text-matches` с предоставленными данными
# о поиске в пределах результатов
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')