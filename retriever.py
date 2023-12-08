import requests
import json
from dataParsers import *

class retriever:

    @staticmethod
    def sendGetRequest(surgery:bool=False, userAccess:bool=False, injury:bool=False, incident:bool=False, drug:bool=False, appointment:bool=False, allergy:bool=False):
        try:
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            filters = {"surgery" : surgery,"userHasAccess": userAccess,"injury" : injury,"incident" : incident,"drug" : drug,"appointment" : appointment,"allergy" : allergy}
            url = "http://127.0.0.1:5000/data/-1"
            return requests.get(url, headers=headers,data=json.dumps(filters))
        except:
            return False

    @staticmethod
    def checkSurgery():
        x = retriever.sendGetRequest(surgery=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkUserHasAccess():
        x = retriever.sendGetRequest(userAccess=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkInjury():
        x = retriever.sendGetRequest(injury=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkIncident():
        x = retriever.sendGetRequest(incident=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkDrug():
        x = retriever.sendGetRequest(drug=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkAppointment():
        x = retriever.sendGetRequest(appointment=True)
        return retriever.checkResponse(x)
    
    @staticmethod
    def checkAllergy():
        x = retriever.sendGetRequest(allergy=True)
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
    def test():
        print("\n2 | RETRIEVING DATA:")
        print("  2.1 | Retrieve surgery\t", end="")
        retriever.result(retriever.checkSurgery())
        print("  2.2 | Retrieve user access\t", end="")
        retriever.result(retriever.checkUserHasAccess())
        print("  2.3 | Retrieve injury\t\t", end="")
        retriever.result(retriever.checkInjury())
        print("  2.4 | Retrieve incident\t", end="")
        retriever.result(retriever.checkIncident())
        print("  2.5 | Retrieve drug\t\t", end="")
        retriever.result(retriever.checkDrug())
        print("  2.6 | Retrieve appointment\t", end="")
        retriever.result(retriever.checkAppointment())
        print("  2.7 | Retrieve allergy\t", end="")
        retriever.result(retriever.checkAllergy())