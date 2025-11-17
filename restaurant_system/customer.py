# customer.py
from data_store import menu, orders, invoices

def customer_view_menu():
    print("\n----- MENU -----")
    for item in menu:
        print(f"{item['id']}. {item['name']} - {item['price']} VND")


def customer_order():
    customer_view_menu()
    items = input("Nhập ID món (vd: 1,2): ").split(",")

    order_items = []
    total = 0

    for i in items:
        i = int(i.strip())
        for item in menu:
            if item["id"] == i:
                order_items.append(item)
                total += item["price"]

    order = {
        "order_id": len(orders) + 1,
        "items": order_items,
        "status": "pending",
    }
    orders.append(order)

    print("\nTạo order thành công!")
    print("Order ID:", order["order_id"])
    print("Tổng tiền:", total, "VND")
    return order["order_id"]


def customer_cancel_order(order_id: int):
    for o in orders:
        if o["order_id"] == order_id:
            if o["status"] == "pending":
                o["status"] = "cancelled"
                print("\nĐã hủy order.")
            else:
                print("\nKhông thể hủy order này (đã xử lý).")
            return
    print("\nKhông tìm thấy order.")


def customer_pay(order_id: int):
    for o in orders:
        if o["order_id"] == order_id:
            if o["status"] == "cancelled":
                print("Order đã bị hủy, không thể thanh toán.")
                return

            print("\nChọn phương thức thanh toán:")
            print("1. Tiền mặt")
            print("2. Thẻ")
            choice = input("Chọn: ")

            method = "cash" if choice == "1" else "card"

            amount = sum(item["price"] for item in o["items"])
            invoice = {
                "invoice_id": len(invoices) + 1,
                "order_id": order_id,
                "amount": amount,
                "method": method,
            }
            invoices.append(invoice)
            o["status"] = "paid"

            print("\nThanh toán thành công!")
            print("Invoice ID:", invoice["invoice_id"])
            print("Số tiền:", invoice["amount"])
            print("Hình thức:", invoice["method"])
            return

    print("Không tìm thấy order.")
