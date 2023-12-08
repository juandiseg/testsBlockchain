import requests
from dataParsers import *

class validator:

    @staticmethod
    def failed(skk="FAILED"): print("\t\033[91m {}\033[00m" .format(skk))
    @staticmethod
    def passed(skk="PASSED"): print("\t\033[92m {}\033[00m" .format(skk))
    
    @staticmethod
    def result(result:bool):
        if result:
            validator.passed()
            return
        validator.failed()

    @staticmethod
    def sendGetValidation(baseURL:str):
        try:
            url = baseURL + "data/validate"
            return requests.get(url).content.decode("utf-8")
        except:
            return "FAILED"
    
    @staticmethod
    def checkResponse(response):
        if response == "PASSED":
            validator.passed()
            return
        validator.failed()

    @staticmethod
    def test(baseURL:str):
        print("\n3 | BLOCKCHAIN VALID: \t", end="")
        result = validator.sendGetValidation(baseURL)
        validator.checkResponse(result)