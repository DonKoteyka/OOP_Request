import requests
from pprint import pprint
import datetime
def fun_unix_data(data):
    '''я честно разбирался 30 минут с юникс датой и психанул'''
    res = ((int(str(data).split('-')[2]))*57600)+1680307200

    return res

def get_title(json):
    res = [i.get('title') for i in json.get('items')]
    return res
def stackoverflow_qestion(unix_time1, unix_time2, theme='Python'):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate':unix_time1, 'todate':unix_time2, 'order':'desc', 'sort':'activity', 'site':'stackoverflow', 'tagged':theme}
    respond = requests.get(url, params=params).json()
    return (respond)

if __name__ == '__main__':
    presentDate = datetime.datetime.now().date()
    unix_time1 = fun_unix_data(presentDate)
    unix_time2 = unix_time1 + 259200
    pprint(get_title(stackoverflow_qestion(unix_time1, unix_time2)))









