# manager.py
from data_store import menu, staff, orders, invoices

def manager_view_revenue():
    print("\n----- DOANH THU -----")
    total = sum(inv["amount"] for inv in invoices)
    print("Tổng doanh thu:", total, "VND")


def manager_view_report():
    print("\n----- BÁO CÁO ORDER -----")
    for o in orders:
        print(o)


def manager_menu_management():
    print("\n----- QUẢN LÝ MENU (XEM) -----")
    for m in menu:
        print(m)


def manager_personnel_management():
    print("\n----- DANH SÁCH NHÂN SỰ -----")
    for s in staff:
        print(s)
