# ==========================
# DỮ LIỆU MẪU
# ==========================
menu = {
    "M01": {"ten": "Phở bò", "gia": 45000, "trang_thai": "Đang bán"},
    "M02": {"ten": "Cơm gà", "gia": 50000, "trang_thai": "Đang bán"},
    "M03": {"ten": "Bún chả", "gia": 40000, "trang_thai": "Tạm ngưng"},
}

# ==========================
# HÀM HIỂN THỊ DANH SÁCH MÓN
# ==========================
def hien_thi_menu(menu_dict):
    print("\n=== DANH SÁCH MÓN ĂN ===")
    if not menu_dict:
        print("Menu đang trống.")
        return
    print(f"{'Mã':<5} {'Tên món':<20} {'Giá':<10} {'Trạng thái':<15}")
    for ma, mon in menu_dict.items():
        print(f"{ma:<5} {mon['ten']:<20} {mon['gia']:<10} {mon['trang_thai']:<15}")
    print("========================\n")

# ==========================
# HÀM SỬA MÓN ĂN (QUẢN LÝ)
# ==========================
def sua_mon_an(menu_dict):
    hien_thi_menu(menu_dict)

    ma_mon = input("Nhập mã món cần sửa (vd: M01): ").strip().upper()

    if ma_mon not in menu_dict:
        print("❌ Không tìm thấy món ăn với mã này.")
        return

    mon_cu = menu_dict[ma_mon]
    print("\n--- Thông tin hiện tại ---")
    print(f"Mã món     : {ma_mon}")
    print(f"Tên món    : {mon_cu['ten']}")
    print(f"Giá        : {mon_cu['gia']}")
    print(f"Trạng thái : {mon_cu['trang_thai']}")
    print("--------------------------\n")

    # Nhập thông tin mới (Enter để giữ nguyên)
    ten_moi = input("Tên món mới (Enter để giữ nguyên): ").strip()
    gia_moi = input("Giá mới (Enter để giữ nguyên): ").strip()
    trang_thai_moi = input("Trạng thái mới (Enter để giữ nguyên): ").strip()

    # Cập nhật nếu có nhập
    if ten_moi != "":
        menu_dict[ma_mon]["ten"] = ten_moi

    if gia_moi != "":
        try:
            gia_moi_int = int(gia_moi)
            if gia_moi_int > 0:
                menu_dict[ma_mon]["gia"] = gia_moi_int
            else:
                print("⚠ Giá phải > 0. Giữ nguyên giá cũ.")
        except ValueError:
            print("⚠ Giá không hợp lệ. Giữ nguyên giá cũ.")

  
