# ================== BIẾN TOÀN CỤC ==================
product_description = ""
discount_codes = []

# ================== CHƯƠNG TRÌNH ==================
while True:
    print("\n===== MENU CHƯƠNG TRÌNH =====")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo")
    print("2. Chuẩn hóa tên Shop")
    print("3. Kiểm tra mã giảm giá")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát chương trình")

    choice = input("Chọn chức năng: ")

    # ===== BẪY 4: không phải số =====
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5")
        continue

    choice = int(choice)

    # ===== BẪY 3: ngoài phạm vi =====
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5")
        continue

    match choice:

        
        case 1:
            shop_name = input("Nhập tên shop: ").strip()
            if not shop_name:
                print("Tên shop không được bỏ trống")
                continue

            product_name = input("Nhập tên sản phẩm: ").strip().title()

            product_description = input("Nhập mô tả sản phẩm: ").strip()
            if not product_description:
                print("Mô tả sản phẩm không được rỗng")
                continue

            category = " ".join(input("Nhập danh mục: ").split()).lower()

            keywords_input = input("Nhập từ khóa (phân cách bằng dấu phẩy): ")
            keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]

            print("\n--- BÁO CÁO SẢN PHẨM ---")
            print("Tên shop:", shop_name)
            print("Tên sản phẩm:", product_name)
            print("Mô tả:", product_description)
            print("Độ dài mô tả:", len(product_description))
            print("Danh mục:", category)
            print("Danh sách từ khóa:", keywords)
            print("Số lượng từ khóa:", len(keywords))
            print("Mô tả chữ thường:", product_description.lower())
            print("Mô tả chữ hoa:", product_description.upper())


        case 2:
            shop_name = input("Nhập tên shop: ").strip()

            if not shop_name:
                print("Tên shop không được bỏ trống")
                continue

            shop_name = shop_name.lower()
            shop_name = "-".join(shop_name.split())

            if not shop_name.startswith("shop-"):
                shop_name = "shop-" + shop_name

            print("Tên shop sau chuẩn hóa:", shop_name)

        
        case 3:
            code = input("Nhập mã giảm giá: ")

            if not code:
                print("Mã giảm giá không được rỗng")
            elif " " in code:
                print("Mã giảm giá không được chứa khoảng trắng")
            elif not (6 <= len(code) <= 12):
                print("Mã giảm giá phải từ 6 đến 12 ký tự")
            elif not code.isupper():
                print("Mã giảm giá phải viết hoa toàn bộ")
            elif not code.isalnum():
                print("Mã giảm giá chỉ được chứa chữ và số")
            elif not code.startswith("SALE"):
                print("Mã giảm giá phải bắt đầu bằng SALE")
            else:
                discount_codes.append(code)
                print("Mã giảm giá hợp lệ")
                print("Danh sách mã hiện tại:", discount_codes)

        
        case 4:
            if not product_description:
                print("Chưa có mô tả sản phẩm để xử lý")
                continue

            find_word = input("Từ khóa cần tìm: ")
            replace_word = input("Từ khóa thay thế: ")

            count = product_description.count(find_word)

            if count == 0:
                print("Không tìm thấy từ khóa trong mô tả")
            else:
                product_description = product_description.replace(find_word, replace_word)
                print("Số lần xuất hiện:", count)
                print("Mô tả sau khi thay thế:")
                print(product_description)

        
        case 5:
            print("Thoát chương trình")
            break