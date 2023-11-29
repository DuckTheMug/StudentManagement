from model.Certification import Certification


class Student:

    def __init__(self, citizenIdentity: int, candidateNumber: int, name: str, address: str,
                 cert: Certification = None):
        self.__citizenIdentity = citizenIdentity
        self.__candidateNumber = candidateNumber
        self.__name = name
        self.__address = address
        self.__cert = cert

    def setCitizenIdentity(self, citizenIdentity: int):
        self.__citizenIdentity = citizenIdentity

    def setCandidateNumber(self, candidateNumber: int):
        self.__candidateNumber = candidateNumber

    def setName(self, name: str):
        self.__name = name

    def setAddress(self, address: str):
        self.__address = address

    def setCert(self, cert: Certification | None):
        self.__cert = cert

    def getCitizenIdentity(self) -> int:
        return self.__citizenIdentity

    def getCandidateNumber(self) -> int:
        return self.__candidateNumber

    def getName(self) -> str:
        return self.__name

    def getAddress(self) -> str:
        return self.__address

    def getCert(self) -> Certification | None:
        return self.__cert
