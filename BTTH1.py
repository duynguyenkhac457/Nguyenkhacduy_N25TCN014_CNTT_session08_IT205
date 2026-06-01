while True:
    print("========================================")
    print("HỆ THỐNG QUẢN LÍ NỘI DUNG TIKTOK")
    print("========================================")
    print("1. Nhập thông tin phân tích video")
    print("2. Chuẩn hóa tên tài khoản")
    print("3. Kiểm tra tính hợp lệ của hashtag")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả")
    print("5. Thoát chương trình")
    print("========================================")

    choice = input("Mời bạn chọn chức năng(1 > 5): ")

    match(choice):


    
        case "1":
            user_name = input("Nhập tên tài khoản: ")
            if user_name =="":
                print("Không được để trống!!!")
                continue
            title_video = input("Nhập tiêu đề video: ")
            decription = input("Nhập mô tả video: ")
            hashtag_list = input("Nhập danh sách hashtag(Cách nhau bởi dấu phẩy): ")

            print("===Đang xử lí dữ liệu===")
            print(f"Tên tài khoản: {user_name.strip()}")
            print(f"Tên tiêu đề: {title_video.strip().title()}")
            print(f"Mô tả: {decription.strip()}")
            print(f"Độ dài mô tả: {len(decription)}")
            count_space = decription.count(" ") + 1
            print(f"Số lượng từ trong mô tả: {count_space}")
            list_item = hashtag_list.split(",")
            new_list_hashtag = "".join(list_item)
            print(f"Danh sách hashtag: {new_list_hashtag}")
            count_hashtag = len(list_item)
            print(f"Số lượng hashtag: {count_hashtag}")
            print(f"Mô tả đã chuyển hóa thành thường: {decription.lower()}")
            print(f"Mô tả đã chuyển hóa thành Hoa: {decription.upper()}")


        case "2":
            print(f"Tên tài khoản ban đầu: {user_name}")
            print("Tên tài khoản khi chuẩn hóa: ","@"+ user_name.lower())
        
        case "3":
            hashtag = input("Nhập hashtag: ")
            if (hashtag == ""):
                print("Không được rỗng!!!")
                break
            elif (not hashtag.startswith("#")):
                print("Phải bắt đầu bằng #")
                break
            elif (" " in hashtag):
                print("Hashtag không được chứa khoản trắng!!!")
                break
            elif (len(hashtag) > 2):
                print("Phải chứa tối thiểu 2 kí tự")
                break
            else: 
                print("Hashtag hợp lệ")
                hashtag_list = hashtag_list + hashtag
                print(f"Danh sách hashtag mới: {hashtag_list}")
        
        case "4":
            find_word = input("Nhập từ khóa cần tìm: ")
            if(find_word in decription):
                decription = decription.replace(find_word, "Từ khóa mới")
                print(f"Mô tả sau khi thay thế: {decription}")
            else:
                print("Không hợp lệ!!!")
        case "5":
            print("Đã thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ!!!")