#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json
import sys
import os
import pandas as pd


def drop_na(d):
    for key, value in list(d.items()):
        if pd.isna(value):
            del d[key]
        elif isinstance(value, dict):
            drop_na(value)
    return d


def chara():
    cdata = pd.read_json(os.path.join(KF3DB_PATH, 'mst', 'CHARA_DATA.json'))
    cdata = cdata.set_index(cdata['id']).sort_index()

    cdata_en = cdata[['nameEn']]
    cdata = cdata[[
        'name', 'nickname', 'eponymName', 'flavorText', 'animalFlavorText'
    ]]

    pdata = pd.read_json(os.path.join(KF3DB_PATH, 'parameter.json'),
                         orient='index')
    pdata.drop(['id', 'arts_plus'], axis=1, inplace=True)
    pdata.columns = [
        'art', 'art_desc', 'special', 'special_desc', 'wait', 'wait_desc',
        'ability', 'ability_desc', 'kiseki', 'kiseki_desc'
    ]
    data = cdata.join(pdata)

    # old = pd.read_json(os.path.join('ja_jp', 'chara.json'), orient='index')
    # diff = data[~(data == old)].dropna(how='all').dropna(axis=1, how='all')

    with open(os.path.join('ja_jp', 'chara.json'), 'w', encoding='utf-8') as f:
        json.dump(data.to_dict(orient='index'),
                  f,
                  indent=2,
                  ensure_ascii=False)

    cdata_en.columns = ['name', 'nickname', 'eponymName', 'flavorText', 'animalFlavorText']
    if os.path.exists(os.path.join('en_us', 'chara.json')):
        old_en = pd.read_json(os.path.join('en_us', 'chara.json'),
                              orient='index')
        old_en.drop('name', axis=1, inplace=True)
        cdata_en = pd.concat([cdata_en, old_en], axis=1)

    with open(os.path.join('en_us', 'chara.json'), 'w', encoding='utf-8') as f:
        json.dump(drop_na(cdata_en.to_dict(orient='index')),
                  f,
                  indent=2,
                  ensure_ascii=False)


if __name__ == '__main__':
    KF3DB_PATH = sys.argv[1]
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    chara()
