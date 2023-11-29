from validate.CertValidate import CertValidate


class Certification:

    def __init__(self, certType: str, score: float):
        cert = CertValidate.parseCertType(certType)
        self.__certType = cert
        self.__score = score

    def setCerType(self, certType: str):
        cert = CertValidate.parseCertType(certType)
        self.__certType = cert

    def setScore(self, score: float):
        self.__score = score

    def getCerType(self) -> str:
        return self.__certType

    def getScore(self) -> float:
        return self.__score
    