import json


def convert_orderdict_to_json(order_dict):
    data_str = json.dumps(order_dict)
    return json.loads(data_str)
