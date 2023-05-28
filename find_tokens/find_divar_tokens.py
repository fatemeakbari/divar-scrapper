import requests
import datetime
from json.decoder import JSONDecodeError
import pandas as pd

LIMIT_FOR_EACH_VACANCY = 1000
URL = 'https://api.divar.ir/v8/search/1/apartment-sell'
HEADERS = {
    "Content-Type": "application/json"
}
NUM_OF_SCRAPPING_VACANCIES = 10
current_date = datetime.datetime.now()
last_post_date_ = int(current_date.strftime("%Y%m%d%H%M%S") + '00')

print(f'scrapping post has published before {current_date}')
json = {"json_schema": {"category": {"value": "apartment-sell"}},
        "last-post-date": last_post_date_}

res = requests.post(URL, json=json, headers=HEADERS)
data = res.json()

vacancies = data['input_suggestion']['json_schema']['properties']['districts']['properties']['vacancies']['items']
vacancies_id = vacancies['enum'][:NUM_OF_SCRAPPING_VACANCIES]
vacancies_name = vacancies['enumNames'][:NUM_OF_SCRAPPING_VACANCIES]
list_of_tokens = []

json = {
    "json_schema":
        {
            "category": {"value": "apartment-sell"},
            "districts": {"vacancies": []},
            "sort": {"value": "sort_date"},
            "cities": ["1"]
        },
    "last-post-date": ""}

for idx, name in zip(vacancies_id, vacancies_name):

    print(f'start scraping for vacancy = {idx}')


    json['json_schema']['districts']['vacancies'] = [f"{idx}"]
    json['last-post-date'] = last_post_date_
    count = 0

    try:
        while count < LIMIT_FOR_EACH_VACANCY:

            res = requests.post(URL, json=json, headers=HEADERS)
            data = res.json()

            if data['last_post_date'] == -1:
                print('Divar has limited our access to the older items')
                break

            for widget in data['web_widgets']['post_list']:
                token = widget['data']['token']
                list_of_tokens.append([idx, name, token])
                count += 1

                if count % 100 == 0:
                    print(f'count = {count}')

            json['last-post-date'] = data['last_post_date']


    except JSONDecodeError as e:
        print('occurs an error ', e)
    except:
        print('occurs an unknown problem')

df = pd.DataFrame(list_of_tokens, columns=['vacancy_id', 'vacancy_name', 'token'])
df.to_csv('tokens.csv', index=False)
