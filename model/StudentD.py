from model.Student import Student
from Certification import Certification
from validate.StudentValidate import StudentValidate


class StudentD(Student):
    # constructor
    def __init__(self, citizenIdentity: int, candidateNumber: int, name: str, address: str, mathScore: float,
                 literatureScore: float, englishScore: float, cert: Certification = None):
        StudentValidate.checkScore(mathScore)
        StudentValidate.checkScore(literatureScore)
        StudentValidate.checkScore(englishScore)
        super().__init__(citizenIdentity, candidateNumber, name, address, cert)
        self.__mathScore = mathScore
        self.__literatureScore = literatureScore
        self.__englishScore = englishScore

    # getter & setter
    def setMathScore(self, mathScore: float):
        StudentValidate.checkScore(mathScore)
        self.__mathScore = mathScore

    def setLiteratureScore(self, literatureScore: float):
        StudentValidate.checkScore(literatureScore)
        self.__literatureScore = literatureScore

    def setEnglishScore(self, englishScore: float):
        StudentValidate.checkScore(englishScore)
        self.__englishScore = englishScore

    def getMathScore(self) -> float:
        return self.__mathScore

    def getLiteratureScore(self) -> float:
        return self.__literatureScore

    def getEnglishScore(self) -> float:
        return self.__englishScore