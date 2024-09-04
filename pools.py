import json
import os


class Pools:
    """A class to represent pools.

    Attributes:
        data_filepath (str): The path to the JSON file.
    Methods:
        load(): Loads a JSON file into a list from data_filepath.
        save(data): Saves data to a JSON file at data_filepath.
    """

    data_filepath = os.path.realpath(os.path.dirname(__file__)) + "/pool_data.json"

    @classmethod
    def load(cls) -> list:
        """Loads a JSON file into a list.

        Returns:
            list: The parsed JSON data.
            In case of an exception, an empty list is returned.
        """
        try:
            return json.load(open(cls.data_filepath))
        except Exception as e:
            return []

    @classmethod
    def save(cls, data: list) -> None:
        """Writes data to a JSON file.

        Parameters:
          data (list): The data to be written to the JSON file.
        """
        with open(cls.data_filepath, "w") as f:
            json.dump(data, f, indent=4)
