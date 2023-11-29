from model.Student import Student
from model.Certification import Certification
from validate.StudentValidate import StudentValidate
class StudentC(Student):
    # constructor
    def __init__(self, citizenIdentity: int, candidateNumber: int, name: str, address: str,
                 literatureScore: float, historyScore: float, geographyScore: float, cert: Certification = None):
        super().__init__(citizenIdentity, candidateNumber, name, address, cert)
        self.__literatureScore = literatureScore
        self.__historyScore = historyScore
        self.__geographyScore = geographyScore
    # getter & setter
    def setLiteratureScore(self, literatureScore: float):
        self.__literatureScore = literatureScore

    def setHistoryScore(self, historyScore: float):
        self.__historyScore = historyScore

    def setGeographyScore(self, geographyScore: float):
        self.__geographyScore = geographyScore

    def getLitSrc(self) -> float:
        return self.__literatureScore

    def getHistSrc(self) -> float:
        return self.__historyScore

    def getGeoSrc(self) -> float:
        return self.__geographyScore

    def getSATScore(self) -> float:
        return StudentValidate.CalculatorSATScore(self.getLitSrc(), self.getHistSrc(), self.getGeoSrc(), self.getCert())
    
    #subject dictionary
    subDict = dict([(0, 'ngữ văn'), (1, 'lịch sử'), (2, 'địa lý')])