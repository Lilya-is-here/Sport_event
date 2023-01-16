import requests
from loguru import logger
import json
from datetime import datetime

logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', colorize=True)

def parse_1xstavka():
    url = 'https://1xstavka.ru/LiveFeed/Get1x2_VZip?count=50&mode=4&country=1&partner=51&getEmpty=true&mobi=true'
    try:
        result = requests.get(url)
        result.raise_for_status()
        data = result.json()
        games = []
        with open(f'1xstavka.json', 'w') as file:
            file.write(json.dumps(data, indent=4))
        for items in dict(data).get('Value'):
            match = {}
            first_team = items['O1']
            second_team = items['O2']
            score_first_team = items['SC']['FS'].get('S1')
            score_second_team = items['SC']['FS'].get('S2')
            match['category'] = items.get('L')
            match['teams'] = {'first': first_team, 'second': second_team}
            match['score'] = {'first': score_first_team, 'second': score_second_team}
            coefficients = []
            for coefficient in items.get('E'):
                coefficients.append(float(coefficient.get('C')))
            if len(coefficients) >= 3:
                match['coefficients'] = {
                    '1': coefficients[0],
                    'X': coefficients[1],
                    '2': coefficients[2]
                }
            else:
                match['coefficients'] = {
                    '1': None,
                    'X': None,
                    '2': None
                }
            games.append(match)
        file_name = f'1xstavka_{int(datetime.now().timestamp())}'
        # в файл данные записываем временно, потом их нужно будет записать в базу данных.
        with open(f'{file_name}.json', 'w') as file:
            file.write(json.dumps(games, indent=4))
    except (requests.RequestException, ValueError) as e:
        logger.error(e)


if __name__ == '__main__':
    parse_1xstavka()




