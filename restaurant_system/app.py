# app.py
from customer import (
    customer_view_menu,
    customer_order,
    customer_cancel_order,
    customer_pay,
)
from waiter import (
    waiter_view_orders,
    waiter_send_to_kitchen,
    waiter_update_order,
)
from chef import (
    chef_view_pending_dishes,
    chef_fix_dish,
)
from cashier import cashier_print_invoice
from manager import (
    manager_view_report,
    manager_view_revenue,
)

def main():
    print("==== SIMPLE RESTAURANT SYSTEM ====")

    while True:
        print("\nChọn actor:")
        print("1. Customer")
        print("2. Waiter")
        print("3. Chef")
        print("4. Cashier")
        print("5. Manager")
        print("0. Thoát")
        a = input("Chọn: ")

        # CUSTOMER
        if a == "1":
            print("\n--- CUSTOMER MENU ---")
            print("1. Xem menu")
            print("2. Đặt món")
            print("3. Hủy order")
            print("4. Thanh toán")
            c = input("Chọn: ")

            if c == "1":
                customer_view_menu()
            elif c == "2":
                customer_order()
            elif c == "3":
                oid = int(input("Nhập Order ID: "))
                customer_cancel_order(oid)
            elif c == "4":
                oid = int(input("Nhập Order ID: "))
                customer_pay(oid)

        # WAITER
        elif a == "2":
            print("\n--- WAITER ---")
            print("1. Xem tất cả order")
            print("2. Gửi order vào bếp")
            print("3. Cập nhật trạng thái order")
            w = input("Chọn: ")

            if w == "1":
                waiter_view_orders()
            elif w == "2":
                oid = int(input("Order ID: "))
                waiter_send_to_kitchen(oid)
            elif w == "3":
                oid = int(input("Order ID: "))
                st = input("Trạng thái mới: ")
                waiter_update_order(oid, st)

        # CHEF
        elif a == "3":
            print("\n--- CHEF ---")
            print("1. Xem món cần nấu")
            print("2. Đánh dấu đã nấu xong")
            ch = input("Chọn: ")

            if ch == "1":
                chef_view_pending_dishes()
            elif ch == "2":
                oid = int(input("Order ID: "))
                chef_fix_dish(oid)

        # CASHIER
        elif a == "4":
            print("\n--- CASHIER ---")
            print("1. In hóa đơn")
            ca = input("Chọn: ")

            if ca == "1":
                iid = int(input("Invoice ID: "))
                cashier_print_invoice(iid)

        # MANAGER
        elif a == "5":
            print("\n--- MANAGER ---")
            print("1. Xem báo cáo order")
            print("2. Xem doanh thu")
            m = input("Chọn: ")

            if m == "1":
                manager_view_report()
            elif m == "2":
                manager_view_revenue()

        elif a == "0":
            print("Tạm biệt!")
            break


if __name__ == "__main__":
    main()
