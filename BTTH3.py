# ================== BIẾN TOÀN CỤC ==================
delivery_note = ""

# ================== CHƯƠNG TRÌNH ==================
while True:
    print("\n=== HỆ THỐNG QUẢN LÝ ĐƠN GIAO HÀNG GRAB EXPRESS ===")
    print("1. Nhập dữ liệu đơn hàng và xem báo cáo")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại khách hàng")
    print("4. Tìm kiếm và thay thế từ khóa trong ghi chú")
    print("5. Thoát chương trình")

    choice = input("Nhập chức năng: ")

    # ===== BẪY 6 =====
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5")
        continue

    # ===== BẪY 5 =====
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5")
        continue

    match choice:


        case "1":
            sender_name = input("Tên người gửi: ").strip()
            if sender_name == "":
                print("Tên người gửi không được bỏ trống")
                continue

            sender_phone = input("SĐT người gửi: ").strip()
            if sender_phone == "":
                print("Số điện thoại người gửi không được bỏ trống")
                continue

            pickup_address = input("Địa chỉ lấy hàng: ").strip()
            if pickup_address == "":
                print("Địa chỉ lấy hàng không được bỏ trống")
                continue

            receiver_name = input("Tên người nhận: ").strip()
            if receiver_name == "":
                print("Tên người nhận không được bỏ trống")
                continue

            receiver_phone = input("SĐT người nhận: ").strip()
            if receiver_phone == "":
                print("Số điện thoại người nhận không được bỏ trống")
                continue

            delivery_address = input("Địa chỉ giao hàng: ").strip()
            if delivery_address == "":
                print("Địa chỉ giao hàng không được bỏ trống")
                continue

            delivery_note = input("Ghi chú giao hàng: ").strip()
            if delivery_note == "":
                print("Ghi chú giao hàng không được bỏ trống")
                continue

            print("\n--- BÁO CÁO ĐƠN HÀNG ---")
            print("Người gửi:", sender_name.title())
            print("Người nhận:", receiver_name.title())
            print("Địa chỉ lấy hàng:", " ".join(pickup_address.split()))
            print("Địa chỉ giao hàng:", " ".join(delivery_address.split()))
            print("Ghi chú:", delivery_note)
            print("Độ dài ghi chú:", len(delivery_note))
            print("Số từ trong ghi chú:", len(delivery_note.split()))
            print("Ghi chú chữ thường:", delivery_note.lower())
            print("Ghi chú chữ hoa:", delivery_note.upper())

    
        case "2":
            order_code = input("Nhập mã đơn hàng: ").strip().upper()
            order_code = "-".join(order_code.split())

            if not order_code.startswith("GRAB-"):
                order_code = "GRAB-" + order_code

            print("Mã đơn sau chuẩn hóa:", order_code)

        
        case "3":
            sender_phone = input("SĐT người gửi: ").strip()
            receiver_phone = input("SĐT người nhận: ").strip()

            if not sender_phone.isdigit():
                print("Số điện thoại người gửi không hợp lệ")
                continue
            if len(sender_phone) != 10:
                print("Số điện thoại người gửi phải có đúng 10 ký tự")
                continue

            if not receiver_phone.isdigit():
                print("Số điện thoại người nhận không hợp lệ")
                continue
            if len(receiver_phone) != 10:
                print("Số điện thoại người nhận phải có đúng 10 ký tự")
                continue

            hidden_sender = sender_phone[:3] + "*****" + sender_phone[-2:]
            hidden_receiver = receiver_phone[:3] + "*****" + receiver_phone[-2:]

            print("SĐT người gửi:", hidden_sender)
            print("SĐT người nhận:", hidden_receiver)

        
        case "4":
            if delivery_note == "":
                print("Chưa có ghi chú giao hàng để tìm kiếm")
                continue

            find_word = input("Từ khóa cần tìm: ")
            replace_word = input("Từ khóa thay thế: ")

            count = delivery_note.count(find_word)

            if count == 0:
                print("Không tìm thấy từ khóa trong ghi chú")
            else:
                delivery_note = delivery_note.replace(find_word, replace_word)
                print("Số lần xuất hiện:", count)
                print("Ghi chú sau thay thế:")
                print(delivery_note)

        
        case "5":
            print("Thoát chương trình")
            break