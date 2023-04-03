import json

import requests

id_url = 'https://data.rcsb.org/rest/v1/holdings/current/entry_ids'


def print_hi(name):
    query = '''{
  entries(entry_ids: ["AF_AFP68871F1"]) {
    rcsb_ma_qa_metric_global {
      ma_qa_metric_global {
        type
        value
      }
    }
  }
}'''
    query2 = '''
    {
        "type": "group",
        "nodes": [
            {
                "type": "group",
                "nodes": [
                    {
                        "type": "terminal",
                        "service": "text",
                        "parameters": {
                            "attribute": "struct_keywords.pdbx_keywords",
                            "negation": false,
                            "operator": "contains_phrase",
                            "value": "PHOTOSYNTHESIS"
                        }
                    }
                ],
                "logical_operator": "and",
                "label": "text"
            }
        ],
        "logical_operator": "and"
    },
    "return_type": "entry",
    "request_options": {
        "paginate": {
            "start": 0,
            "rows": 25
        },
        "results_content_type": [
            "experimental"
        ],
        "sort": [
            {
                "sort_by": "score",
                "direction": "desc"
            }
        ],
        "scoring_strategy": "combined"
    }



    '''
    payload = json.dumps({'query': query})
    payload2 = json.dumps({'query': query2})
    headers = {
        'Content-Type': 'application/json',
    }
    response2 = requests.post('https://data.rcsb.org/graphql', headers=headers, data=payload)
    response = requests.post('https://data.rcsb.org/graphql', headers=headers, data=payload2)
    print(response.json())
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
