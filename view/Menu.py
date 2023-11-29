import os


def menuChoice() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""Chức năng:
        1.Thêm mới thí sinh
        2.Tìm kiếm thí sinh theo SBD
        3.Tìm kiếm thí sinh theo CCCD
        4.Sửa thông tin thí sinh
        5.Xóa thí sinh
        6.Hiển thị danh sách thí sinh có điểm từ thấp đến cao
        7.Hiển thị danh sách thí sinh có điểm từ cao đến thấp
        8.Hiển thị danh sách thí sinh đạt học bổng
        9.Hiển thị danh sách thí sinh không liệt môn nào
        0. Thoát""")


def addStudentChoice():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
        1. Thí sinh khối C
        2. Thí sinh khối D
        0. Quay lại
        ''')


def updateStudentChoice():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
        Bạn muốn thay đổi ? (0-6): 
        1. CCCD
        2. SBD
        3. Họ và tên
        4. Địa chỉ
        5. Chứng chỉ
        6. Điểm
        0. Thoát
        ''')
