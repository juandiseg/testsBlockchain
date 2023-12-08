import requests
import json
from dataParsers import *

class retriever:

    @staticmethod
    def sendGetRequest(baseURL:str, surgery:bool=False, userAccess:bool=False, injury:bool=False, incident:bool=False, drug:bool=False, appointment:bool=False, allergy:bool=False):
        try:
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            filters = {"surgery" : surgery,"userHasAccess": userAccess,"injury" : injury,"incident" : incident,"drug" : drug,"appointment" : appointment,"allergy" : allergy}
            url = baseURL + "data/-1"
            return requests.get(url, headers=headers,data=json.dumps(filters))
        except:
            return False

    @staticmethod
    def checkSurgery(baseURL:str):
        x = retriever.sendGetRequest(baseURL, surgery=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkUserHasAccess(baseURL:str):
        x = retriever.sendGetRequest(baseURL, userAccess=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkInjury(baseURL:str):
        x = retriever.sendGetRequest(baseURL, injury=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkIncident(baseURL:str):
        x = retriever.sendGetRequest(baseURL, incident=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkDrug(baseURL:str):
        x = retriever.sendGetRequest(baseURL, drug=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkAppointment(baseURL:str):
        x = retriever.sendGetRequest(baseURL, appointment=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkAllergy(baseURL:str):
        x = retriever.sendGetRequest(baseURL, allergy=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def failed(skk="FAILED"): print("\033[91m {}\033[00m" .format(skk))
    
    @staticmethod
    def passed(skk="PASSED"): print("\033[92m {}\033[00m" .format(skk))


    @staticmethod
    def checkResponse(x):
        if isinstance (x, bool):
            return False
        if len(x.json()) != 0:
            return True
        return False

    @staticmethod
    def result(result:bool):
        if result:
            retriever.passed()
            return
        retriever.failed()

    @staticmethod
    def test(baseURL:str):
        print("\n2 | RETRIEVING DATA:")
        print("  2.1 | Retrieve surgery\t", end="")
        retriever.result(retriever.checkSurgery(baseURL))
        print("  2.2 | Retrieve user access\t", end="")
        retriever.result(retriever.checkUserHasAccess(baseURL))
        print("  2.3 | Retrieve injury\t\t", end="")
        retriever.result(retriever.checkInjury(baseURL))
        print("  2.4 | Retrieve incident\t", end="")
        retriever.result(retriever.checkIncident(baseURL))
        print("  2.5 | Retrieve drug\t\t", end="")
        retriever.result(retriever.checkDrug(baseURL))
        print("  2.6 | Retrieve appointment\t", end="")
        retriever.result(retriever.checkAppointment(baseURL))
        print("  2.7 | Retrieve allergy\t", end="")
        retriever.result(retriever.checkAllergy(baseURL))