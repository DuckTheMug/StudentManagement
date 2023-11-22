class StudentValidate:
    @staticmethod
    def checkCitizenIdentity(citizenIdentity: int):
        if (len(str(citizenIdentity)) > 12) | (len(str(citizenIdentity)) < 10):
            raise ValueError

    @staticmethod
    def checkCandidateNumber(candidateNumber: int):
        if (len(str(candidateNumber)) > 8) | (len(str(candidateNumber)) < 7):
            raise ValueError

    @staticmethod
    def checkName(name: str):
        if (len(name) < 5) | (len(name) > 255):
            raise ValueError
        namec = name.encode().decode().split(" ")
        for i in namec:
            if not i.isalpha():
                raise ValueError
        

    @staticmethod
    def checkAddress(address: str):
        if (len(address) < 12) | (len(address) > 2048) | (address.isnumeric()):
            raise ValueError

    @staticmethod
    def checkScore(score: float):
        if (score < 0.0) | (score > 10.0):
            raise ValueError

    @staticmethod
    def CalculatorSATScore(scoreA: float, scoreB: float, scoreC: float, certification: Certification) -> float:
        satScore = 1.5 * scoreA + scoreB + scoreC
        if certification.getCerType() is "ielts":
            satScore += 1.5
        elif certification.getCerType() is "toeic":
            satScore += 1.
        return satScore
