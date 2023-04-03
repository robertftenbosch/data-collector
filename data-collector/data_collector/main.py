import json

import pandas
import requests


def get_ids():
    id_url = 'https://data.rcsb.org/rest/v1/holdings/current/entry_ids'
    response = requests.get(id_url)
    return response.json()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == '__main__':
    ids = get_ids()
    pd = pandas.DataFrame(ids)
    pd.to_csv('../data/rcsb_dataset.csv', index=True)

    print(ids)