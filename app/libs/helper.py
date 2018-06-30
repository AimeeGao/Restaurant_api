"""
 Created by 七月 on 2018-1-31.
"""
import random
import requests
from collections import namedtuple

__author__ = '七月'

TAOBAO_IP_REQUEST_URL = 'http://ip.taobao.com/service/getIpInfo.php?ip={}'
Address = namedtuple('address', ['country', 'region', 'city', 'isp'])


def is_isbn_or_key(word):
    """
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key


def get_random_str(length):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(length):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt


# 根据ip获得ip区域
def get_ip_origin(ip):
    url = TAOBAO_IP_REQUEST_URL.format(ip)
    res = requests.get(url).json()
    if res.get('code') == 1:
        return None
    country = res.get('data').get('country')
    region = res.get('data').get('region')
    city = res.get('data').get('city')
    isp = res.get('data').get('isp')
    # data. country  region  city  isp
    address = Address(country=country, region=region, city=city, isp=isp)
    return address
