from vietnam_provinces import enums
from ctnx import remove_diacritics
from model.Certification import Certification


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
        addc = address.split(',')
        if len(addc) != 2:
            raise ValueError
        short_prov = ''.join(s[0] for s in addc[1].split())
        for i in range(2):
            addc[i] = remove_diacritics(addc[i].strip().replace(' ', '_')).upper()
            if i == 0:
                addc[i] = addc[i] + '_' + short_prov
        if addc[0] not in enums.districts.DistrictDEnum._member_names_:
            raise ValueError
        if addc[1] not in enums.districts.ProvinceDEnum._member_names_:
            raise ValueError

    @staticmethod
    def checkForUniqueID(lst: list, ele):
        for i in range(len(lst)):
            lst[i] = lst[i].getCitizenIdentity()
        if ele in lst:
            raise ValueError
    def checkForUniqueNumber(lst: list, ele):
        for i in range(len(lst)):
            lst[i] = lst[i].getCandidateNumber()
        if ele in lst:
            raise ValueError

    @staticmethod
    def checkScore(score: float):
        if (score < 0.0) | (score > 10.0):
            raise ValueError

    @staticmethod
    def CalculatorSATScore(scoreA: float, scoreB: float, scoreC: float, certification: Certification) -> float:
        satScore = 1.5 * scoreA + scoreB + scoreC
        if certification is None:
            pass
        elif certification.getCerType() == "ielts":
            satScore += 1.5
        elif certification.getCerType() == "toeic":
            satScore += 1.
        return satScore
