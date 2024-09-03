import json


def load_pool_data(filepath):
    """Loads a JSON file into a Python object.

    Parameters:
        filepath (str): The path to the JSON file.

    Returns:
        dict or list: The parsed JSON data.
    """
    try:
        return json.load(open(filepath))
    except Exception as e:
        return []


def save_pool_data(filepath, data):
    """Writes data to a JSON file.

    Parameters:
      filepath (str): The path of the JSON file.
      data (dict): The data to be written to the JSON file.
    """
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)


def calculate_quantile(data, percentile):
    """Calculates the quantile value of a given data set for a specified percentile.

    Parameters:
        data (list): The input data.
        percentile (float): The desired percentile (between 0 and 100).

    Returns:
        float: The calculated quantile value.
    """
    # Calculate the index of the percentile
    idx = (percentile/100) * (len(data) - 1)

    # Return the percentile value
    if idx.is_integer():
        quantile_value = data[int(idx)]
    else:
        lower_idx = int(idx)
        upper_idx = int(idx) + 1
        lower_value = data[lower_idx]
        upper_value = data[upper_idx]
        quantile_value = lower_value + (idx - lower_idx) * (upper_value - lower_value)
    return quantile_value
