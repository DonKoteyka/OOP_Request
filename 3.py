import requests
from pprint import pprint
import datetime

def get_title(json):
    res = [i.get('title') for i in json.get('items')]
    return res
def stackoverflow_qestion(unix_time1, unix_time2, theme='Python'):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate':unix_time1, 'todate':unix_time2, 'order':'desc', 'sort':'activity', 'site':'stackoverflow', 'tagged':theme}
    respond = requests.get(url, params=params).json()
    return (respond)

if __name__ == '__main__':
    now = int(datetime.datetime.now().timestamp())
    few_day_ago = int((datetime.datetime.now() - datetime.timedelta(days=3)).timestamp())
    pprint(get_title(stackoverflow_qestion(few_day_ago, now)))








