import json


def load_pool_data(filepath):
    try:
        return json.load(open(filepath))
    except Exception as e:
        return []


def save_pool_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)


def calculate_percentile(data, percentile):
    idx = (percentile/100) * (len(data) - 1)
    if idx.is_integer():
        percentile_value = data[int(idx)]
    else:
        lower_idx = int(idx)
        upper_idx = int(idx) + 1
        lower_value = data[lower_idx]
        upper_value = data[upper_idx]
        percentile_value = lower_value + (idx - lower_idx)*(upper_value - lower_value)
    return percentile_value
