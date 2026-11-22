

import socket
import json

HOST = "127.0.0.1"
PORT = 5000


# Send a request to the server
def send_request(data):

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(5)

        client.connect((HOST, PORT))

        message = json.dumps(data, ensure_ascii=False) + "\n"

        client.sendall(message.encode("utf-8"))

        response = b""

        # Receive the server response
        while b"\n" not in response:
            part = client.recv(4096)

            if not part:
                break

            response += part

        client.close()

        if not response:
            print("The server did not send a response!")
            return None

        return json.loads(response.decode("utf-8").strip())

    except ConnectionRefusedError:
        print("Cannot connect to the server!")
        return None

    except socket.timeout:
        print("Connection timeout!")
        return None

    except ConnectionError:
        print("Connection lost!")
        return None

    except Exception as error:
        print("Error:", error)
        return None


# Create a new order
def create_order():

    print("\n--- Create Order ---")

    name = input("Enter your name: ")
    contact = input("Enter your phone number: ")
    address = input("Enter delivery address: ")

    products = []

    print("Enter products.")
    print("Enter 0 to finish.")

    # Add products to the list
    while True:

        product = input("Product name: ")

        if product == "0":
            break

        if product.strip() != "":
            products.append(product)

    if not name.strip() or not contact.strip() or not address.strip():
        print("Please fill in all required fields!")
        return

    if len(products) == 0:
        print("Please add at least one product!")
        return

    data = {
        "command": "create",
        "name": name,
        "contact": contact,
        "address": address,
        "products": products
    }

    result = send_request(data)

    if result is not None:

        if result["success"]:
            print("\n", result["message"])
            print("Your order number:", result["order"]["id"])
        else:
            print(result["message"])


# Show all client orders
def show_orders():

    print("\n--- My Orders ---")

    name = input("Enter your name: ")

    result = send_request({
        "command": "list",
        "name": name
    })

    if result is not None:

        if len(result["orders"]) == 0:
            print("No orders found!")

        else:

            for order in result["orders"]:

                print("\nOrder number:", order["id"])
                print("Name:", order["name"])
                print("Phone:", order["contact"])
                print("Address:", order["address"])
                print("Products:", ", ".join(order["products"]))
                print("Status:", order["status"])


# Check delivery status
def check_status():

    print("\n--- Check Delivery Status ---")

    try:
        order_id = int(input("Enter order number: "))

        result = send_request({
            "command": "status",
            "order_id": order_id
        })

        if result is not None:

            if result["success"]:
                print("Delivery status:", result["status"])
            else:
                print(result["message"])

    except ValueError:
        print("Please enter a number!")


# Main program menu
def main():

    while True:

        print("\n==============================")
        print("       DELIVERY SERVICE")
        print("==============================")
        print("1. Create order")
        print("2. Show my orders")
        print("3. Check delivery status")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_order()

        elif choice == "2":
            show_orders()

        elif choice == "3":
            check_status()

        elif choice == "0":
            print("Thank you for using our program!")
            break

        else:
            print("Wrong menu option!")


if __name__ == "__main__":
    main()

