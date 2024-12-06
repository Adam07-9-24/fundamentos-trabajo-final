from models.models import Receipt
from database.data import receipts
from utils.utils import validate_unique_id
from iu.menu import display_menu

def save_receipts_to_file(receipts):
    with open('receipts.txt', 'w') as file:
        file.write("="*42 + "\n")
        file.write("                Receipt\n")
        file.write("="*42 + "\n")
        
        for receipt in receipts:
            file.write(f"ID: {receipt['id']}\n")
            file.write(f"Customer: {receipt['customer_name']}\n")
            file.write(f"Pizza Type: {receipt['pizza_type']}\n")
            file.write(f"Quantity: {receipt['quantity']}\n")
            file.write(f"Total Price: ${receipt['total_price']:.2f}\n")
            file.write("-"*42 + "\n")
        
        file.write("="*42 + "\n")
        file.write("          Thank you for your purchase!\n")
        file.write("="*42 + "\n")

def main():
    while True:
        option = display_menu()
        if option == 1:
            for receipt in receipts:
                print(receipt)
        elif option == 2:
            receipt_id = int(input("ID del recibo: "))
            receipt = next((receipt for receipt in receipts if receipt["id"] == receipt_id), None)
            print(receipt if receipt else "Recibo no encontrado")
        elif option == 3:
            receipt_id = int(input("ID del recibo: "))
            if not validate_unique_id(receipts, receipt_id):
                print("ID duplicado")
                continue
            customer_name = input("Nombre del cliente: ")
            pizza_type = input("Tipo de pizza: ")
            quantity = int(input("Cantidad: "))
            total_price = float(input("Precio total: "))
            receipts.append({"id": receipt_id, "customer_name": customer_name, "pizza_type": pizza_type, "quantity": quantity, "total_price": total_price})
            print("Recibo agregado")
            save_receipts_to_file(receipts)
        elif option == 4:
            receipt_id = int(input("ID del recibo: "))
            receipt = next((receipt for receipt in receipts if receipt["id"] == receipt_id), None)
            if not receipt:
                print("Recibo no encontrado")
                continue
            receipt["customer_name"] = input(f"Cliente ({receipt['customer_name']}): ") or receipt["customer_name"]
            receipt["pizza_type"] = input(f"Tipo de pizza ({receipt['pizza_type']}): ") or receipt["pizza_type"]
            receipt["quantity"] = int(input(f"Cantidad ({receipt['quantity']}): ")) or receipt["quantity"]
            receipt["total_price"] = float(input(f"Precio ({receipt['total_price']}): ")) or receipt["total_price"]
            print("Recibo actualizado")
            save_receipts_to_file(receipts)
        elif option == 5:
            receipt_id = int(input("ID del recibo: "))
            receipts[:] = [receipt for receipt in receipts if receipt["id"] != receipt_id]
            print("Recibo eliminado")
            save_receipts_to_file(receipts)
        elif option == 6:
            break

if __name__ == "__main__":
    main()
