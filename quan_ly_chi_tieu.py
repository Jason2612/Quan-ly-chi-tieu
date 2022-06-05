
expenses = []


def add_item(myTempList, item):
    myTempList.append(item)

def find_index_item(myTempList, item_name):
    result = -1
    length = len(myTempList)
    for i in range(length):
        if myTempList[i]["Tên"] == item_name:
            result = i
    return result

def remove_item(myTempList, item_name):
    if find_index_item(myTempList, item_name) > -1:
        del myTempList[find_index_item(myTempList, item_name)]
    else:
        print(item_name + " không có trong danh sách")

def optional():
    return int(input("Vui lòng chọn chức năng 1 hoặc 2: "))

def input_name():
    return input("Tên khoản chi tiêu: ")


while True:
    print("Chọn chức năng bạn muốn? -\n"\
                    "1. Thêm mục\n" \
                    "2. Xóa mục\n" \
                    "0. Thoát chương trình")
    option = optional()

    if option == 1:
        item_input = input_name()
        cost_input = int(input("Gia tri chi cua khoan chi moi: "))
        date_input = input("Ngay chi cua khoan chi moi: ")
        item = {
            "Tên":item_input,
            "Chi phí":cost_input,
            "Ngày":date_input,
        }
        add_item(expenses, item)
        print("Khoản chi tiêu của bạn: ", expenses)
    elif option == 2:
        item_input = input_name()
        remove_item(expenses, item_input)
        print("Khoản chi tiêu của bạn: ", expenses)
    elif option == 0:
        print("Exit the program")
        break
    else:
        print("Chức năng không hợp lệ")
    
