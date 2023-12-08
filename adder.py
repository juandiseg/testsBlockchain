import requests
from dataParsers import *
import jsonpickle

class adder:

    @staticmethod
    def sendPostRequest(name:str,data):
        try:
            url = "http://127.0.0.1:5000/data/" + name
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            return requests.post(url, headers=headers, data=jsonpickle.encode(data, unpicklable=False))
        except:
            return False

    @staticmethod
    def addSurgery():
        response = adder.sendPostRequest("surgery", surgery(-1, -2, [-4,-5,-6], "foo", "foo", "foo"))
        return adder.checkResponse(response)

    @staticmethod
    def addUserAccess():
        response = adder.sendPostRequest("userAccess", userHasAccess(-1, -2, "foo"))
        return adder.checkResponse(response)

    @staticmethod
    def addInjury():
        response = adder.sendPostRequest("injury", injury(-1, [-4,-5,-6], "foo", "foo", "foo"))
        return adder.checkResponse(response)

    @staticmethod
    def addIncident():
        response = adder.sendPostRequest("incident", incident(-1, [-4,-5,-6], "foo", "foo", "foo"))
        return adder.checkResponse(response)

    @staticmethod
    def addDrug():
        response = adder.sendPostRequest("drug", drug(-1, -2, "foo", "foo", "foo", "foo"))
        return adder.checkResponse(response)
    
    @staticmethod
    def addAppointment():
        response = adder.sendPostRequest("appointment", appointment(-1, -2, -7, "foo", "foo", "foo"))
        return adder.checkResponse(response)
    
    @staticmethod
    def addAllergy():
        response = adder.sendPostRequest("allergy", allergy(-1, "foo", "foo", "foo"))
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
    def test():
        print("1 | UPLOADING DATA:")
        print("  1.1 | Add surgery\t\t", end="")
        adder.result(adder.addSurgery())
        print("  1.2 | Add user access\t\t", end="")
        adder.result(adder.addUserAccess())
        print("  1.3 | Add injury\t\t", end="")
        adder.result(adder.addInjury())
        print("  1.4 | Add incident\t\t", end="")
        adder.result(adder.addIncident())
        print("  1.5 | Add drug\t\t", end="")
        adder.result(adder.addDrug())
        print("  1.6 | Add appointment\t\t", end="")
        adder.result(adder.addAppointment())
        print("  1.7 | Add allergy\t\t", end="")
        adder.result(adder.addAllergy())
