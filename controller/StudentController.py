from model.Certification import Certification
from model.Student import Student
from model.StudentC import StudentC
from model.StudentD import StudentD
from validate.CertValidate import CertValidate
from validate.StudentValidate import StudentValidate


class StudentController:
    def __init__(self):
        self.__lstC = []
        self.__lstD = []

    def __addStudentC(self, student: Student):
        self.__lstC.append(student)
        
    def __addStudentD(self, student: Student):
        self.__lstD.append(student)

    def addStudent(self, student_type: int):
        while True:
            try: 
                si = int(input('Nhập số CCCD: '))
                StudentValidate.checkCitizenIdentity(si)
                break
            except ValueError:
                print('Số CCCD không hợp lệ, vui lòng nhập lại.')
                continue
        while True:
            try: 
                sn = int(input('Nhập SBD: '))
                StudentValidate.checkCandidateNumber(sn)
                break
            except ValueError:
                print('SBD không hợp lệ, vui lòng nhập lại.')
                continue
        while True:
            try:
                name = str(input('Nhập họ và tên: '))
                StudentValidate.checkName(name)
                break
            except ValueError:
                print('Họ và tên không hợp lệ, vui lòng nhập lại.')
                continue
        while True:
            try:
                address = str(input('Nhập địa chỉ: '))
                StudentValidate.checkAddress(address)
                break
            except ValueError:
                print('Địa chỉ không hợp lệ, vui lòng nhập lại.')
                continue
        cert = None
        has_cert = str(input('Có chứng chỉ tiếng Anh? (y/n): ').lower().strip())
        while True:
            try:                
                if has_cert == 'y':
                    while True:
                        try:
                            cert_type = CertValidate.parseCertType(str(input('Nhập loại chứng chỉ (toeic/ielts): ')))
                            CertValidate.checkCertType(cert_type)
                            break
                        except ValueError:
                            print('Loại chứng chỉ không hợp lệ, vui lòng nhập lại.')
                            continue
                    while True:
                        try:
                            cert_score = float(input('Nhập số điểm: '))
                            CertValidate.checkScore(cert_type, cert_score)
                            break
                        except ValueError:
                            print('Số điểm không hợp lệ, vui lòng nhập lại.')
                            continue
                    cert = Certification(cert_type, cert_score)
                    break
                elif has_cert == 'n':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Giá trị không hợp lệ, vui lòng nhập lại.')
                continue
        st = Student(si, sn, name, address, cert)
        if student_type == 1:
            st.__class__ = StudentC
        elif student_type == 2:
            st.__class__ = StudentD
        for i in range(3):
            while True:
                try:
                    score = float(input(f'Nhập số điểm {st.__class__.subDict[i]}: '))
                    StudentValidate.checkScore(score)
                    break
                except ValueError:
                    print('Số điểm không hợp lệ, vui lòng nhập lại.')
                    continue
                finally:
                    match student_type:
                        case 1:
                            match i:
                                case 0:
                                    st.setLiteratureScore(score)
                                case 1:
                                    st.setHistoryScore(score)
                                case 2:
                                    st.setGeographyScore(score)
                                    self.__addStudentC(st)
                        case 2:
                            match i:
                                case 0:
                                    st.setMathScore(score)
                                case 1:
                                    st.setLiteratureScore(score)
                                case 2:
                                    st.getEnglishScore(score)
                                    self.__addStudentD(st)
                                    
    def getStudentCAsList(self) -> list:
        return self.__lstC
    
    def getStudentDAsList(self) -> list:
        return self.__lstD
    
    def getAllStudentAsList(self) -> list:
        return self.__lstC + self.__lstD

    def findStudentByCandidateNumber(self, candidateNumber: int):
        StudentValidate.checkCandidateNumber(candidateNumber)
        for num in (self.__lstC + self.__lstD):
            if num.getCandidateNumber() == candidateNumber:
                print(num.__dict__)
                break
    def findStudentByCitizenIdentity(self, citizenIdentity: int):
        StudentValidate.checkCitizenIdentity(citizenIdentity)
        for num in (self.__lstC + self.__lstD):
            if num.getCitizenIdentity() == citizenIdentity:
                print(num.__dict__)
                break

    def checkStudentNotFall(self, lstStudentC: list, lstStudentD: list):
        for stdC in lstStudentC:
            if (stdC.getLitSrc() >= 2) & (stdC.getHistSrc() >= 2) & (stdC.getGeoSrc() >= 2):
                print(stdC.__dict__)
        for stdD in lstStudentD:
            if (stdD.getMathScore() >= 2) & (stdD.getLiteratureScore() >= 2) & (stdD.getEnglishScore() >= 2):
                print(stdD.__dict__)

    def listScholarship(self, lstStudentC: list, lstStudentD: list):
        listScore = []
        for stdt in lstStudentC:
            listScore.append({'CitizenIdentity': stdt.getCitizenIdentity,
                              'SATScore': stdt.getSATScore,
                              'LitScr': stdt.getLitScr(),
                              'B': stdt.getHistSrc, 'C': stdt.getGeoSrc()}
                             )
        for stdt in lstStudentD:
            listScore.append({'CitizenIdentity': stdt.getCitizenIdentity,
                              'SATScore': stdt.getSATScore,
                              'LitScr': stdt.getLiteratureScore(),
                              'B': stdt.getMathScore, 'C': stdt.getEnglishScore()}
                             )
        listScore.sort(reverse=True, key='SATScore')
        lScholarship = []
        for stdt in listScore:
            if (stdt['LitScr'] > 8.) & (stdt['B'] >= 5.) & (stdt['C'] >= 5.):
                lScholarship.append(stdt['CitizenIdentity'])
            if len(lScholarship) == 5:
                break
        for ci in lScholarship:
            print(self.findStudentByCitizenIdentity(ci))
