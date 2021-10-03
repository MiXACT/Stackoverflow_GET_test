from pprint import pprint
import requests
import time


def time_count(t):
    """Ф-ия принимает на вход числовое значение, обозначающее кол-во дней.
    Ф-ия возвращает момент времени (Unix time) после вычета принятого на вход значения.
    Возвращаемое значение момента времени округлено и приведено к int."""
    time_minus_t = int(round(time.time() - t * 24 * 3600, 0))
    return time_minus_t


URL = "https://api.stackexchange.com/2.3/questions"

params = {'order': 'desc',
          'sort': 'activity',
          'fromdate': time_count(2),
          'todate': time_count(0),
          'tagged': 'python',
          'site': 'stackoverflow'
          }
r = requests.get(URL, params=params)
pprint(r.json()['items'])
