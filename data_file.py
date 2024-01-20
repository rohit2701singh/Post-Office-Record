import requests
from datetime import datetime


class PostData:

    def __init__(self, auth_token, api_endpoint):

        self.__authorization_token = auth_token
        self.__sheety_api = api_endpoint
        self.__data = None

        self.__header_sheety = {
            "Authorization": self.__authorization_token,
            "Content-Type": "application/json"
        }

    def insert_data(self, data_to_post: list):
        """take data in list format and insert date automatically"""

        today = datetime.now().strftime("%d-%m-%Y")
        print(today)
        self.__data = data_to_post

        for item in self.__data:
            if len(item["name"]) != 0:
                data_entry = {
                    "information": {
                        "date": today,
                        "postName": item["name"],
                        "postFrom": item["post_from"],
                        "postTo": item["post_to"],
                        "phoneNumber": item["phone_number"]
                    }
                }

                requests.post(url=self.__sheety_api, json=data_entry, headers=self.__header_sheety)
            else:
                print("one input does not contain name, can't enter that data. continuing with others.")
        print("data inserted successfully")

    def get_sheet_data(self):
        """return all entries."""

        get_response = requests.get(url=self.__sheety_api, headers=self.__header_sheety)
        data = get_response.json()
        return data