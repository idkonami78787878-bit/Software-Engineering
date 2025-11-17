# cashier.py
from data_store import invoices

def cashier_print_invoice(invoice_id: int):
    for inv in invoices:
        if inv["invoice_id"] == invoice_id:
            print("\n----- HÓA ĐƠN -----")
            print(f"Invoice ID: {inv['invoice_id']}")
            print(f"Order ID  : {inv['order_id']}")
            print(f"Số tiền   : {inv['amount']} VND")
            print(f"Hình thức : {inv['method']}")
            return
    print("Không tìm thấy hóa đơn.")
