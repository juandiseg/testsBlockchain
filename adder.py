import requests
from dataParsers import *
import jsonpickle

class adder:

    @staticmethod
    def sendPostRequest(baseURL:str, name:str,data):
        try:
            url = baseURL + "data/" + name
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            return requests.post(url, headers=headers, data=jsonpickle.encode(data, unpicklable=False))
        except:
            return False

    @staticmethod
    def addSurgery(baseURL:str):
        response = adder.sendPostRequest(baseURL, "surgery", surgery(-1, -2, [-4,-5,-6], "foo", "foo", "foo"))
        return adder.checkResponse(response)

    @staticmethod
    def addUserAccess(baseURL:str):
        response = adder.sendPostRequest(baseURL, "userAccess", userHasAccess(-1, -2, "foo"))
        return adder.checkResponse(response)

    @staticmethod
    def addInjury(baseURL:str):
        response = adder.sendPostRequest(baseURL, "injury", injury(-1, [-4,-5,-6], "foo", "foo", "foo"))
        return adder.checkResponse(response)

    @staticmethod
    def addIncident(baseURL:str):
        response = adder.sendPostRequest(baseURL, "incident", incident(-1, [-4,-5,-6], "foo", "foo", "foo"))
        return adder.checkResponse(response)

    @staticmethod
    def addDrug(baseURL:str):
        response = adder.sendPostRequest(baseURL, "drug", drug(-1, -2, "foo", "foo", "foo", "foo"))
        return adder.checkResponse(response)
    
    @staticmethod
    def addAppointment(baseURL:str):
        response = adder.sendPostRequest(baseURL, "appointment", appointment(-1, -2, -7, "foo", "foo", "foo"))
        return adder.checkResponse(response)
    
    @staticmethod
    def addAllergy(baseURL:str):
        response = adder.sendPostRequest(baseURL, "allergy", allergy(-1, "foo", "foo", "foo"))
        return adder.checkResponse(response)

    @staticmethod
    def checkResponse(response):
        if isinstance (response, bool):
            return False
        if response.status_code == 200:
            return True
        return False
    
    @staticmethod
    def failed(skk="FAILED"): print("\033[91m {}\033[00m" .format(skk))
    
    @staticmethod
    def passed(skk="PASSED"): print("\033[92m {}\033[00m" .format(skk))

    @staticmethod
    def result(result:bool):
        if result:
            adder.passed()
            return
        adder.failed()

    @staticmethod
    def test(baseURL:str):
        print("1 | UPLOADING DATA:")
        print("  1.1 | Add surgery\t\t", end="")
        adder.result(adder.addSurgery(baseURL))
        print("  1.2 | Add user access\t\t", end="")
        adder.result(adder.addUserAccess(baseURL))
        print("  1.3 | Add injury\t\t", end="")
        adder.result(adder.addInjury(baseURL))
        print("  1.4 | Add incident\t\t", end="")
        adder.result(adder.addIncident(baseURL))
        print("  1.5 | Add drug\t\t", end="")
        adder.result(adder.addDrug(baseURL))
        print("  1.6 | Add appointment\t\t", end="")
        adder.result(adder.addAppointment(baseURL))
        print("  1.7 | Add allergy\t\t", end="")
        adder.result(adder.addAllergy(baseURL))
