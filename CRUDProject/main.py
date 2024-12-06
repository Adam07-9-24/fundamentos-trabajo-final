from models.models import Receipt
from database.data import receipts
from utils.utils import validate_unique_id
from iu.menu import display_menu

def save_receipts_to_file(receipts):
    try:
        with open('receipts.txt', 'w') as file:
            file.write("="*42 + "\n")
            file.write("                Receipt\n")
            file.write("="*42 + "\n")
            
            for receipt in receipts:
                file.write(f"ID: {receipt.get('id', 'No ID')}\n")
                file.write(f"Customer: {receipt.get('customer_name', 'No customer')}\n")
                file.write(f"Pizza Type: {receipt.get('pizza_type', 'No pizza type')}\n")
                file.write(f"Pizza Size: {receipt.get('pizza_size', 'No pizza size')}\n")  
                file.write(f"Quantity: {receipt.get('quantity', 0)}\n")
                file.write(f"Total Price: ${receipt.get('total_price', 0.0):.2f}\n")
                file.write("-"*42 + "\n")
            
            file.write("="*42 + "\n")
            file.write("          Thank you for your purchase!\n")
            file.write("="*42 + "\n")
    except Exception as e:
        print(f"Error saving receipts to file: {e}")

def main():
    while True:
        try:
            option = display_menu()
            if option == 1:
                for receipt in receipts:
                    print(receipt)
            elif option == 2:
                receipt_id = int(input("Recibo ID: "))
                receipt = next((receipt for receipt in receipts if receipt["id"] == receipt_id), None)
                print(receipt if receipt else "Recibo no encontrado")
            elif option == 3:
                receipt_id = int(input("Recibo ID: "))
                if not validate_unique_id(receipts, receipt_id):
                    print("ID duplicado")
                    continue
                customer_name = input("Nombre del cliente: ")
                pizza_type = input("Tipo de pizza: ")
                pizza_size = input("Tamaño de pizza (Pequeña, Mediana, Grande): ")  
                quantity = int(input("Cantidad: "))
                price_per_pizza = float(input("Precio por pizza: "))
                total_price = price_per_pizza * quantity
                receipt = {
                    "id": receipt_id,
                    "customer_name": customer_name,
                    "pizza_type": pizza_type,
                    "pizza_size": pizza_size,  
                    "quantity": quantity,
                    "total_price": total_price
                }
                receipts.append(receipt)
                print("Recibo agregado")
                print(receipt) 
                save_receipts_to_file(receipts)
            elif option == 4:
                receipt_id = int(input("Recibo ID: "))
                receipt = next((receipt for receipt in receipts if receipt["id"] == receipt_id), None)
                if not receipt:
                    print("Recibo no encontrado")
                    continue
                receipt["customer_name"] = input(f"Cliente ({receipt['customer_name']}): ") or receipt["customer_name"]
                receipt["pizza_type"] = input(f"Tipo de pizza ({receipt['pizza_type']}): ") or receipt["pizza_type"]
                receipt["pizza_size"] = input(f"Tamaño de pizza ({receipt['pizza_size']}): ") or receipt["pizza_size"]
                price_per_pizza = float(input(f"Precio por pizza ({receipt.get('price_per_pizza', 'No especificado')}): ") or receipt.get('price_per_pizza', 0))
                quantity = int(input(f"Cantidad ({receipt['quantity']}): ") or receipt["quantity"])
                receipt["total_price"] = price_per_pizza * quantity
                receipt["quantity"] = quantity
                print("Recibo actualizado")
                save_receipts_to_file(receipts)
            elif option == 5:
                receipt_id = int(input("Recibo ID: "))
                receipts[:] = [receipt for receipt in receipts if receipt["id"] != receipt_id]
                print("Recibo eliminado")
                save_receipts_to_file(receipts)
            elif option == 6:
                break
        except ValueError as ve:
            print(f"Entrada no válida: {ve}. Por favor, ingresa el valor correcto.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
