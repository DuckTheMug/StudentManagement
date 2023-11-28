import os
from controller.StudentController import ManageStudent
from view import Menu


class Main:
    Menu.menuChoice()
    controller = ManageStudent()
    choice = int(input("Nhập lựa chọn của bạn: "))
    while choice != 0:
        match choice:
            case 1:
                studentBlock = int(input("Nhập khối thí sinh dự thi (khối C:1, khối D:2): "))
                controller.addStudent(studentBlock)
                print("Thêm thành công!")
                for student in controller.getListStudent():
                    print("{:<8} {:<18} "
                          .format(student.getCitizenIdentity(), student.getName()))
                Menu.menuChoice()
                choice = int(input("Nhập lựa chọn của bạn: "))
            case 2:
                candidateNumber = int(input("Nhập SBD muốn tìm kiếm? "))
                controller.findStudentByCandidateNumber(candidateNumber)
                Menu.menuChoice()
                choice = int(input("Nhập lựa chọn của bạn: "))
            case 3:
                citizenIdentity = int(input("Nhập CCCD muốn tìm kiếm? "))
                print(controller.findStudentByCitizenIdentity(citizenIdentity).__dict__)
                Menu.menuChoice()
                choice = int(input("Nhập lựa chọn của bạn: "))
            case 4:
                citizenIdentity = int(input("Nhập CCCD thí sinh: "))
                controller.updateStudent(citizenIdentity)
                print(controller.findStudentByCitizenIdentity(citizenIdentity).__dict__)
                Menu.menuChoice()
                choice = int(input("Nhập lựa chọn của bạn: "))
            case 5:
                citizenIdentity = int(input("Nhập SBD thí sinh: "))
                controller.deleteStudent(citizenIdentity)
                os.system('pause' if os.name == 'nt' else "/bin/bash -c 'read -s -n 1 -p \"Press any key to continue...\"'")
                # print(controller.findStudentByCitizenIdentity(citizenIdentity).__dict__)
                Menu.menuChoice()
                choice = int(input("Nhập lựa chọn của bạn: "))
            case 8:
                controller.listScholarship(controller.getListStudentC(),controller.getListStudentD())
                os.system('pause' if os.name == 'nt' else "/bin/bash -c 'read -s -n 1 -p \"Press any key to continue...\"'")
                Menu.menuChoice()
                choice = int(input("Nhập lựa chọn của bạn: "))
