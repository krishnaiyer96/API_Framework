from random import random, randint


class CommonUtility:

    @staticmethod
    def get_custom_header():
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer 0347439ce5cbdcb0c794a63db16ab8f1d6b7b9d62db8385ed59f0785b11eda6d"}

        return header

    @staticmethod
    def get_unique_email():
        rand_no = randint(1000, 99999)
        email = f"test_automation{rand_no}@mail.com"
        return email
