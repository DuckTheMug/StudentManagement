from model.Certification import Certification
from model.Student import Student
from model.StudentC import StudentC
from model.StudentD import StudentD
from validate.CertValidate import CertValidate
from validate.StudentValidate import StudentValidate
from view import Menu


class ManageStudent:
    def __init__(self):
        self.__lstC = []
        self.__lstD = []

    def getListStudent(self):
        return self.__lstC + self.__lstD

    def getListStudentC(self):
        return self.__lstC

    def getListStudentD(self):
        return self.__lstD

    def __addStudentC(self, student: Student):
        self.__lstC.append(student)

    def __addStudentD(self, student: Student):
        self.__lstD.append(student)

    def addStudent(self, student_type: int):
        while True:
            try:
                si = int(input('Nhập số CCCD (12 ký tự): '))
                StudentValidate.checkCitizenIdentity(si)
                StudentValidate.checkForUniqueID(self.__lstC + self.__lstD, si)
                break
            except ValueError:
                print('Số CCCD không hợp lệ, vui lòng nhập lại.')
                continue
        while True:
            try:
                sn = int(input('Nhập SBD (8 ký tự): '))
                StudentValidate.checkCandidateNumber(sn)
                StudentValidate.checkForUniqueNumber(self.__lstC + self.__lstD, sn)
                break
            except ValueError:
                print('SBD không hợp lệ, vui lòng nhập lại.')
                continue
        while True:
            try:
                name = str(input('Nhập họ và tên (5-255 ký tự): '))
                StudentValidate.checkName(name)
                break
            except ValueError:
                print('Họ và tên không hợp lệ, vui lòng nhập lại.')
                continue
        while True:
            try:
                address = str(input('Nhập địa chỉ (Theo form sau: [Tên quận/huyện], [Tên tỉnh/thành phố]): '))
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
                                    st.setEnglishScore(score)
                                    self.__addStudentD(st)

    @staticmethod
    def inputMenu():
        check = False
        while not check:
            try:
                Menu.menuChoice()
                choice = int(input("Nhập vào lựa chọn: "))
                if 0 <= choice <= 9:
                    check = True
                    return choice
                else:
                    check = False
                    raise ValueError

            except ValueError:
                print('Lựa chọn không hợp lệ, vui lòng nhập lại.')
                continue

    @staticmethod
    def inputUpdate():
        check = False
        while not check:
            try:
                Menu.updateStudentChoice()
                choice = int(input("Nhập vào lựa chọn: "))
                if 0 <= choice <= 6:
                    check = True
                    return choice
                else:
                    check = False
                    raise ValueError
            except ValueError:
                print('Lựa chọn không hợp lệ, vui lòng nhập lại.')
                continue

    def updateStudent(self, citizenIdentity: int):
        StudentValidate.checkCitizenIdentity(citizenIdentity)
        student: Student = self.findStudentByCitizenIdentity(citizenIdentity)
        choice = self.inputUpdate()
        while choice != 0:
            match choice:
                case 1:
                    while True:
                        try:
                            citizenIdentity = int(input("Nhập số CCCD muốn sửa: "))
                            StudentValidate.checkCitizenIdentity(citizenIdentity)
                            StudentValidate.checkForUniqueID(self.__lstC, citizenIdentity)
                            student.setCitizenIdentity(citizenIdentity)
                            break
                        except ValueError:
                            print('Số CCCD không hợp lệ, vui lòng nhập lại.')
                            continue
                    choice = self.inputUpdate()
                case 2:
                    while True:
                        try:
                            candidateNumber = int(input("Nhập SBD muốn sửa: "))
                            StudentValidate.checkCandidateNumber(candidateNumber)
                            StudentValidate.checkForUniqueNumber(self.__lstC, candidateNumber)
                            student.setCandidateNumber(candidateNumber)
                            break
                        except ValueError:
                            print('SBD không hợp lệ, vui lòng nhập lại.')
                            continue
                    choice = self.inputUpdate()
                case 3:
                    while True:
                        try:
                            name = str(input('Nhập họ và tên: '))
                            StudentValidate.checkName(name)
                            student.setName(name)
                            break
                        except ValueError:
                            print('Họ và tên không hợp lệ, vui lòng nhập lại.')
                            continue
                    choice = self.inputUpdate()
                case 4:
                    while True:
                        try:
                            address = str(
                                input('Nhập địa chỉ (Theo form sau: [Tên quận/huyện], [Tên tỉnh/thành phố]): '))
                            StudentValidate.checkAddress(address)
                            student.setAddress(address)
                            break
                        except ValueError:
                            print('Địa chỉ không hợp lệ, vui lòng nhập lại.')
                            continue
                    choice = self.inputUpdate()
                case 5:
                    cert = student.getCert()
                    if cert is not None:
                        has_cert = str(input('Có chứng chỉ tiếng Anh? (y/n): ').lower().strip())
                    else:
                        continue
                    while True:
                        try:
                            if has_cert == 'y':
                                while True:
                                    try:
                                        cert_type = CertValidate.parseCertType(
                                            str(input('Nhập loại chứng chỉ (toeic/ielts): ')))
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
                                cert.setCerType(cert_type)
                                cert.setScore(cert_score)
                                student.setCert(cert)
                                break
                            elif has_cert == 'n':
                                cert = None
                                student.setCert(cert)
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print('Giá trị không hợp lệ, vui lòng nhập lại.')
                            continue
                    choice = self.inputUpdate()
                case 6:
                    check = False
                    for num in self.__lstC:
                        if num.getCitizenIdentity() == citizenIdentity:
                            studentC: StudentC = self.findStudentCByCitizenIdentity(citizenIdentity)
                            while not check:
                                try:
                                    choice = int(input("""Nhập vào lựa chọn: 
                                    1. Điểm Văn
                                    2. Điểm Sử
                                    3. Điểm Địa
                                    0. Thoát"""))
                                    if 0 <= choice <= 3:
                                        check = True
                                    else:
                                        check = False
                                        raise ValueError
                                    break
                                except ValueError:
                                    print('Lựa chọn không hợp lệ, vui lòng nhập lại.')
                                    continue
                            while choice != 0:
                                match choice:
                                    case 1:
                                        literatureScore = float(input("Nhập vào điểm môn Văn muốn sửa: "))
                                        studentC.setLiteratureScore(literatureScore)
                                    case 2:
                                        historyScore = float(input("Nhập vào điểm môn Sử muốn sửa: "))
                                        studentC.setHistoryScore(historyScore)
                                    case 3:
                                        geographyScore = float(input("Nhập vào điểm môn Địa lý muốn sửa: "))
                                        studentC.setGeographyScore(geographyScore)
                                check = False
                                while not check:
                                    try:
                                        choice = int(input("""Nhập vào lựa chọn: 
                                        1. Điểm Văn
                                        2. Điểm Sử
                                        3. Điểm Địa
                                        0. Thoát"""))
                                        if 0 <= choice <= 3:
                                            check = True
                                        else:
                                            check = False
                                            raise ValueError
                                        break
                                    except ValueError:
                                        print('Lựa chọn không hợp lệ, vui lòng nhập lại.')
                                        continue
                    for num in self.__lstD:
                        if num.getCitizenIdentity() == citizenIdentity:
                            studentD: StudentD = self.findStudentDByCitizenIdentity(citizenIdentity)
                            while not check:
                                try:
                                    choice = int(input("""Nhập vào lựa chọn: 
                                        1. Điểm Toán
                                        2. Điểm Văn
                                        3. Điểm Anh
                                        0. Thoát"""))
                                    if 0 <= choice <= 3:
                                        check = True
                                    else:
                                        check = False
                                        raise ValueError
                                    break
                                except ValueError:
                                    print('Lựa chọn không hợp lệ, vui lòng nhập lại.')
                                    continue
                            while choice != 0:
                                match choice:
                                    case 1:
                                        mathScore = float(input("Nhập vào điểm môn Toán muốn sửa: "))
                                        studentD.setMathScore(mathScore)
                                    case 2:
                                        literatureScore = float(input("Nhập vào điểm môn Văn muốn sửa: "))
                                        studentD.setLiteratureScore(literatureScore)
                                    case 3:
                                        englishScore = float(input("Nhập vào điểm môn Tiếng Anh muốn sửa: "))
                                        studentD.setEnglishScore(englishScore)
                                while not check:
                                    try:
                                        choice = int(input("""Nhập vào lựa chọn: 
                                            1. Điểm Toán
                                            2. Điểm Văn
                                            3. Điểm Anh
                                            0. Thoát"""))
                                        if 0 <= choice <= 3:
                                            check = True
                                        else:
                                            check = False
                                            raise ValueError
                                        break
                                    except ValueError:
                                        print('Lựa chọn không hợp lệ, vui lòng nhập lại.')
                                        continue
                case 0:
                    choice = self.inputUpdate()

    def printStudent(self):
        print("{:<14} {:<18} {:<18} {:<18} "
              .format("CCCD", "SBD", "Họ và tên", "Địa chỉ"))
        for student in self.getListStudent():
            print("{:<14} {:<18} {:<12} {:<12}"
                  .format(student.getCitizenIdentity(), student.getCandidateNumber(),
                          student.getName(), student.getAddress()))

    def calculateAverageScore(self, citizenIdentity: int):
        StudentValidate.checkCitizenIdentity(citizenIdentity)
        for student in self.getListStudentC():
            if student.getCitizenIdentity() == citizenIdentity:
                studentC: StudentC = self.findStudentCByCitizenIdentity(citizenIdentity)
                sum = studentC.getLitSrc() + studentC.getHistSrc() + studentC.getGeoSrc()
                print(sum / 3)
            else:
                print("Không tìm thấy thí sinh!")

    def findStudentByCandidateNumber(self, candidateNumber: int):
        StudentValidate.checkCandidateNumber(candidateNumber)
        for student in self.getListStudent():
            if student.getCandidateNumber() == candidateNumber:
                print("{:<14} {:<14} {:<18} {:<18} "
                      .format("CCCD", "SBD", "Họ và tên", "Địa chỉ"))
                print("{:<14} {:<14} {:<18} {:<12}".format(student.getCitizenIdentity(),
                                                           student.getCandidateNumber(),
                                                           student.getName(), student.getAddress()))
                return student
            elif len(self.getListStudent()) > 0:
                continue
            elif len(self.getListStudent()) <= 0:
                print("Không tìm thấy thí sinh!")
                break
            else:
                print("Không tìm thấy thí sinh!")
                break

    def findStudentByCitizenIdentity(self, citizenIdentity: int):
        StudentValidate.checkCitizenIdentity(citizenIdentity)
        for student in self.getListStudent():
            if student.getCitizenIdentity() == citizenIdentity:
                print("{:<14} {:<14} {:<18} {:<18} "
                      .format("CCCD", "SBD", "Họ và tên", "Địa chỉ"))
                print("{:<14} {:<14} {:<18} {:<12}".format(student.getCitizenIdentity(),
                                                           student.getCandidateNumber(),
                                                           student.getName(), student.getAddress()))
                return student
            elif len(self.getListStudent()) > 0:
                continue
            elif len(self.getListStudent()) <= 0:
                print("Không tìm thấy thí sinh!")
                break
            else:
                print("Không tìm thấy thí sinh!")
                break

    def findStudentCByCitizenIdentity(self, citizenIdentity: int):
        StudentValidate.checkCitizenIdentity(citizenIdentity)
        for num in self.getListStudentC():
            if num.getCitizenIdentity() == citizenIdentity:
                return num
            elif len(self.getListStudent()) > 0:
                continue
            else:
                print("Không tìm thấy thí sinh!")
                break

    def findStudentDByCitizenIdentity(self, citizenIdentity: int):
        StudentValidate.checkCitizenIdentity(citizenIdentity)
        for num in self.getListStudentD():
            if num.getCitizenIdentity() == citizenIdentity:
                return num
            elif len(self.getListStudent()) > 0:
                continue
            else:
                print("Không tìm thấy thí sinh!")
                break

    def sortStudentListAscending(self, typeStudent: int, listStudentC: list, listStudentD: list):
        list1 = []
        if typeStudent == 1:
            for stdC in listStudentC:
                list1.append(
                    [stdC.getCitizenIdentity(), stdC.getSATScore(), stdC.getLitSrc(), stdC.getHistSrc(),
                     stdC.getGeoSrc()])
            list1.sort(key=lambda x: x[1], reverse=False)

            liststdt = self.getListStudentC()

            for ci in list1:
                for student in liststdt:
                    if ci[0] == student.getCitizenIdentity() and typeStudent == 1:
                        print(f"Tổng số điểm cả 3 môn: {round(student.getSATScore(), 2)}\n\t"
                              f"Số báo danh: {student.getCandidateNumber()}\n\t"
                              f"Họ và tên: {student.getName()}\n\t"
                              f"Căn cước công dân: {student.getCitizenIdentity()}\n\t"
                              f"Địa chỉ: {student.getAddress()}\n")
        elif typeStudent == 2:
            for stdD in listStudentD:
                list1.append(
                    [stdD.getCitizenIdentity(), stdD.getSATScore(), stdD.getLiteratureScore,
                     stdD.getMathScore, stdD.getEnglishScore])
            list1.sort(key=lambda x: x[1], reverse=False)

            liststdt = self.getListStudentD()

            for ci in list1:
                for student in liststdt:
                    if ci[0] == student.getCitizenIdentity() and typeStudent == 2:
                        print(f"Tổng số điểm cả 3 môn: {round(student.getSATScore(), 2)}\n\t"
                              f"Số báo danh: {student.getCandidateNumber()}\n\t"
                              f"Họ và tên: {student.getName()}\n\t"
                              f"Căn cước công dân: {student.getCitizenIdentity()}\n\t"
                              f"Địa chỉ: {student.getAddress()}\n")

    def sortStudentListDescending(self, typeStudent: int, listStudentC: list, listStudentD: list):
        list1 = []
        if typeStudent == 1:
            for stdC in listStudentC:
                list1.append(
                    [stdC.getCitizenIdentity(), stdC.getSATScore(), stdC.getLitSrc(), stdC.getHistSrc(),
                     stdC.getGeoSrc()])
            list1.sort(key=lambda x: x[1], reverse=True)

            liststdt = self.getListStudentC()

            for ci in list1:
                for student in liststdt:
                    if ci[0] == student.getCitizenIdentity() and typeStudent == 1:
                        print(f"Tổng số điểm cả 3 môn: {round(student.getSATScore(), 2)}\n\t"
                              f"Số báo danh: {student.getCandidateNumber()}\n\t"
                              f"Họ và tên: {student.getName()}\n\t"
                              f"Căn cước công dân: {student.getCitizenIdentity()}\n\t"
                              f"Địa chỉ: {student.getAddress()}\n")
        elif typeStudent == 2:
            for stdD in listStudentD:
                list1.append(
                    [stdD.getCitizenIdentity(), stdD.getSATScore(), stdD.getLiteratureScore,
                     stdD.getMathScore, stdD.getEnglishScore])
            list1.sort(key=lambda x: x[1], reverse=True)

            liststdt = self.getListStudentD()

            for ci in list1:
                for student in liststdt:
                    if ci[0] == student.getCitizenIdentity() and typeStudent == 2:
                        print(f"Tổng số điểm cả 3 môn: {round(student.getSATScore(), 2)}\n\t"
                              f"Số báo danh: {student.getCandidateNumber()}\n\t"
                              f"Họ và tên: {student.getName()}\n\t"
                              f"Căn cước công dân: {student.getCitizenIdentity()}\n\t"
                              f"Địa chỉ: {student.getAddress()}\n")

    def deleteStudent(self, cn: int):
        StudentValidate.checkCandidateNumber(cn)
        student = self.findStudentByCandidateNumber(cn)
        if student is not None:
            print("Thông tin thí sinh cần xoá:")
            print(f"Tổng số điểm cả 3 môn: {round(student.getSATScore(), 2)}\n\t"
                  f"Số báo danh: {student.getCandidateNumber()}\n\t"
                  f"Họ và tên: {student.getName()}\n\t"
                  f"Căn cước công dân: {student.getCitizenIdentity()}\n\t"
                  f"Địa chỉ: {student.getAddress()}\n")
            while True:
                confirm = str(input("Bạn có chắc chắn muốn xoá thí sinh này? (y/n): ")).lower().strip()
                try:
                    if confirm == 'y':
                        if student.__class__ == StudentC:
                            self.__lstC.remove(student)
                        else:
                            self.__lstD.remove(student)
                        print("Đã xoá thí sinh .")
                        break
                    elif confirm == 'n':
                        print("Hủy xoá thí sinh.")
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print('Giá trị không hợp lệ, vui lòng nhập lại.')
                    continue
        else:
            print("Không tìm thấy thí sinh với SBD: ", cn)

    @staticmethod
    def checkStudentNotFall(lstStudentC: list, lstStudentD: list):
        for stdC in lstStudentC:
            if (stdC.getLitSrc() >= 2) & (stdC.getHistSrc() >= 2) & (stdC.getGeoSrc() >= 2):
                print(stdC.__dict__)
        for stdD in lstStudentD:
            if (stdD.getMathScore() >= 2) & (stdD.getLiteratureScore() >= 2) & (stdD.getEnglishScore() >= 2):
                print(stdD.__dict__)

    def listScholarship(self, lstStudentC: list, lstStudentD: list):
        list1 = []
        list2 = []

        for stdC in lstStudentC:
            list1.append(
                [stdC.getCitizenIdentity(), stdC.getSATScore(), stdC.getLitSrc(), stdC.getHistSrc(), stdC.getGeoSrc()])
        for stdD in lstStudentD:
            list1.append([stdD.getCitizenIdentity(), stdD.getSATScore(), stdD.getLiteratureScore(), stdD.getMathScore(),
                          stdD.getEnglishScore()])

        list1.sort(key=lambda x: x[1], reverse=True)

        # list2 là danh sách CCCD của tối đa 5 sinh viên có học bổng
        for stdt in list1:
            if (stdt[1] > 8.) & (stdt[2] >= 5.) & (stdt[3] >= 5.):
                list2.append(stdt[0])
            if len(list2) == 5:
                break

        liststdt = self.getListStudent()

        # Sắp xếp theo thứ tự từ điểm cao đến thấp
        i = 0
        for ci in list2:
            for stdt in liststdt:
                if ci == stdt.getCitizenIdentity():
                    i += 1
                    print(f"Thí sinh đạt học bổng thứ {i}:\n\t"
                          f"Tổng số điểm cả 3 môn: {round(stdt.getSATScore(), 2)}\n\t"
                          f"Số báo danh: {stdt.getCandidateNumber()}\n\t"
                          f"Họ và tên: {stdt.getName()}\n\t"
                          f"Căn cước công dân: {stdt.getCitizenIdentity()}\n\t"
                          f"Địa chỉ: {stdt.getAddress()}\n")