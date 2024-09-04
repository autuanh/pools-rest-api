def calculate_percentile(data, percentile, n=2) -> float:
    """Calculates the percentile value of a given data set for a specified percentile, rounded to n decimal places.

    Parameters:
        data (list): The input data.
        percentile (float): The desired percentile (between 0 and 100).
        n (int): The desired rounded places, by default 2.

    Returns:
        float: The calculated percentile value, rounded to 2 decimal places.
    """
    data = sorted(data)

    # Calculate the index of the percentile
    idx = (percentile / 100) * (len(data) - 1)

    # Return the percentile value
    if idx.is_integer():
        percentile_value = data[int(idx)]
    else:
        lower_idx = int(idx)
        upper_idx = int(idx) + 1
        lower_value = data[lower_idx]
        upper_value = data[upper_idx]
        percentile_value = lower_value + (idx - lower_idx) * (upper_value - lower_value)
    return round(percentile_value, n)
