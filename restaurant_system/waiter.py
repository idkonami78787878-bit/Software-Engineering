# waiter.py
from data_store import orders, invoices

def waiter_view_orders():
    print("\n----- DANH SÁCH ORDER -----")
    for o in orders:
        print(f"Order {o['order_id']} - Trạng thái: {o['status']}")


def waiter_send_to_kitchen(order_id: int):
    for o in orders:
        if o["order_id"] == order_id:
            o["status"] = "confirmed"
            print("Đã gửi order vào bếp.")
            return
    print("Không tìm thấy order.")


def waiter_update_order(order_id: int, new_status: str):
    for o in orders:
        if o["order_id"] == order_id:
            o["status"] = new_status
            print("Đã cập nhật trạng thái order.")
            return
    print("Không tìm thấy order.")


def waiter_create_invoice(order_id: int):
    for o in orders:
        if o["order_id"] == order_id:
            amount = sum(item["price"] for item in o["items"])
            invoice = {
                "invoice_id": len(invoices) + 1,
                "order_id": order_id,
                "amount": amount,
                "method": "none",
            }
            invoices.append(invoice)
            print("Đã tạo hóa đơn (chưa thanh toán).")
            return
    print("Không tìm thấy order.")
