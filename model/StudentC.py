from model.Student import Student
from model.Certification import Certification
from validate.StudentValidate import StudentValidate


class StudentC(Student):
    # constructor
    def __init__(self, citizenIdentity: int, candidateNumber: int, name: str, address: str,
                 literatureScore: float, historyScore: float, geographyScore: float, cert: Certification = None):
        StudentValidate.checkScore(literatureScore)
        StudentValidate.checkScore(historyScore)
        StudentValidate.checkScore(geographyScore)
        super().__init__(citizenIdentity, candidateNumber, name, address, cert)
        self.__literatureScore = literatureScore
        self.__historyScore = historyScore
        self.__geographyScore = geographyScore
        self.__satScore = StudentValidate.CalculatorSATScore(literatureScore, historyScore, geographyScore, cert)

    # getter & setter
    def setLiteratureScore(self, literatureScore: float):
        StudentValidate.checkScore(literatureScore)
        self.__literatureScore = literatureScore

    def setHistoryScore(self, historyScore: float):
        StudentValidate.checkScore(historyScore)
        self.__historyScore = historyScore

    def setGeographyScore(self, geographyScore: float):
        StudentValidate.checkScore(geographyScore)
        self.__geographyScore = geographyScore

    def getLitSrc(self) -> float:
        return self.__literatureScore

    def getHistSrc(self) -> float:
        return self.__historyScore

    def getGeoSrc(self) -> float:
        return self.__geographyScore
    
    #subject dictionary
    subDict = dict([(0, 'ngữ văn'), (1, 'lịch sử'), (2, 'địa lý')])
