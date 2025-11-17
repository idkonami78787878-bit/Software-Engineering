# chef.py
from data_store import orders

def chef_view_pending_dishes():
    print("\n----- MÓN CẦN NẤU -----")
    for o in orders:
        if o["status"] == "confirmed":
            print(f"Order {o['order_id']} cần nấu.")
    print("Hết.")


def chef_fix_dish(order_id: int):
    for o in orders:
        if o["order_id"] == order_id:
            o["status"] = "served"
            print("Đã nấu xong và phục vụ món ăn.")
            return
    print("Không tìm thấy order.")
