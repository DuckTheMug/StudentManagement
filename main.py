import os
from controller.StudentController import ManageStudent
from view import Menu


class Main:
    controller = ManageStudent()
    choice = controller.inputMenu()
    while choice != 0:
        match choice:
            case 1:
                while True:
                    try:
                        studentBlock = int(input("Nhập khối thí sinh dự thi (khối C:1, khối D:2): "))
                        if studentBlock != 1 and studentBlock != 2:
                            raise ValueError
                        else:
                            controller.addStudent(studentBlock)
                            print("Thêm thành công!")
                            controller.printStudent()
                        break
                    except ValueError:
                        print('Lựa chọn không hợp lệ, vui lòng nhập lại.')
                        continue

                choice = controller.inputMenu()
            case 2:
                while True:
                    try:
                        candidateNumber = int(input("Nhập SBD muốn tìm kiếm? "))
                        controller.findStudentByCandidateNumber(candidateNumber)
                        break
                    except ValueError:
                        print('SBD không hợp lệ, vui lòng nhập lại.')
                        continue
                choice = controller.inputMenu()
            case 3:
                while True:
                    try:
                        citizenIdentity = int(input("Nhập số CCCD muốn tìm kiếm?: "))
                        controller.findStudentByCitizenIdentity(citizenIdentity)
                        break
                    except ValueError:
                        print('Số CCCD không hợp lệ, vui lòng nhập lại.')
                        continue
                choice = controller.inputMenu()
            case 4:
                while True:
                    try:
                        citizenIdentity = int(input("Nhập số CCCD muốn sửa: "))
                        controller.updateStudent(citizenIdentity)
                        print(controller.findStudentByCitizenIdentity(citizenIdentity).__dict__)
                        break
                    except ValueError:
                        print('Số CCCD không hợp lệ, vui lòng nhập lại.')
                        continue
                choice = controller.inputMenu()
            case 5:
                while True:
                    try:
                        candidateNumber = int(input("Nhập số SBD thí sinh muốn xóa? "))
                        controller.deleteStudent(candidateNumber)
                        break
                    except ValueError:
                        print('Số CCCD không hợp lệ, vui lòng nhập lại.')
                        continue
                choice = controller.inputMenu()
            case 6:
                while True:
                    try:
                        studentBlock = int(input("Nhập khối thí sinh muốn sắp xếp (khối C:1, khối D:2): "))
                        if studentBlock != 1 and studentBlock != 2:
                            raise ValueError
                        else:
                            controller.sortStudentListAscending(studentBlock, controller.getListStudentC(),
                                                                controller.getListStudentD())
                            break
                    except ValueError:
                        print('Lựa chọn không hợp lệ, vui lòng nhập lại.')
                        continue
                os.system('pause' if os.name == 'nt' else "/bin/bash -c 'read -s -n 1 -p "
                                                          "\"Press any key to continue...\"'")
                choice = controller.inputMenu()
            case 7:
                while True:
                    try:
                        studentBlock = int(input("Nhập khối thí sinh muốn sắp xếp (khối C:1, khối D:2): "))
                        if studentBlock != 1 and studentBlock != 2:
                            raise ValueError
                        else:
                            controller.sortStudentListDescending(studentBlock, controller.getListStudentC(),
                                                                 controller.getListStudentD())
                            break
                    except ValueError:
                        print('Lựa chọn không hợp lệ, vui lòng nhập lại.')
                        continue
                os.system('pause' if os.name == 'nt' else "/bin/bash -c 'read -s -n 1 -p "
                                                          "\"Press any key to continue...\"'")
                choice = controller.inputMenu()
            case 8:
                controller.listScholarship(controller.getListStudentC(), controller.getListStudentD())
                os.system('pause' if os.name == 'nt' else "/bin/bash -c 'read -s -n 1 -p "
                                                          "\"Press any key to continue...\"'")
                choice = controller.inputMenu()
            case 9:
                controller.checkStudentNotFall(controller.getListStudentC(), controller.getListStudentD())
                os.system('pause' if os.name == 'nt' else "/bin/bash -c 'read -s -n 1 -p "
                                                          "\"Press any key to continue...\"'")
                choice = controller.inputMenu()
    print("____KẾT THÚC CHƯƠNG TRÌNH_____")
