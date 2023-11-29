class CertValidate:
    @staticmethod
    def checkCertType(certType: str):
        if (certType != 'toeic') & (certType != 'ielts'):
            raise ValueError

    @staticmethod
    def checkScore(certType: str, score: float):
        if ((certType == 'ielts') & ((score < 0.0) | (score > 9.0))) | (
                (certType == 'toeic') & ((score < 0.0) | (score > 990.0) | (score % 5 != 0))):
            raise ValueError

    @staticmethod
    def parseCertType(certType: str) -> str:
        return certType.strip().lower()
