
import socket
import threading
import json
import os

HOST = "127.0.0.1"
PORT = 5000

orders = []
lock = threading.Lock()


# Load orders from the JSON file
def load_orders():
    global orders

    if os.path.exists("orders.json"):
        try:
            with open("orders.json", "r", encoding="utf-8") as file:
                orders = json.load(file)
        except:
            orders = []
    else:
        orders = []


# Save orders to the JSON file
def save_orders():
    with open("orders.json", "w", encoding="utf-8") as file:
        json.dump(orders, file, ensure_ascii=False, indent=4)


# Process a request from the client
def process_request(data):

    with lock:

        command = data.get("command")

        # Create a new order
        if command == "create":

            order_id = 1

            if len(orders) > 0:
                order_id = max(order["id"] for order in orders) + 1

            new_order = {
                "id": order_id,
                "name": data.get("name"),
                "contact": data.get("contact"),
                "address": data.get("address"),
                "products": data.get("products"),
                "status": "Принят"
            }

            orders.append(new_order)
            save_orders()

            return {
                "success": True,
                "message": "Заказ успешно создан!",
                "order": new_order
            }

        # Show all orders of a client
        elif command == "list":

            name = data.get("name")

            user_orders = []

            for order in orders:
                if order["name"] == name:
                    user_orders.append(order)

            return {
                "success": True,
                "orders": user_orders
            }

        # Check the order status
        elif command == "status":

            order_id = data.get("order_id")

            for order in orders:
                if order["id"] == order_id:
                    return {
                        "success": True,
                        "status": order["status"]
                    }

            return {
                "success": False,
                "message": "Заказ не найден!"
            }

        # Update the order status
        elif command == "update_status":

            order_id = data.get("order_id")
            new_status = data.get("status")

            statuses = [
                "Принят",
                "Готовится к отправке",
                "В пути",
                "Доставлен"
            ]

            if new_status not in statuses:
                return {
                    "success": False,
                    "message": "Неверный статус!"
                }

            for order in orders:
                if order["id"] == order_id:
                    order["status"] = new_status
                    save_orders()

                    return {
                        "success": True,
                        "message": "Статус заказа изменён!"
                    }

            return {
                "success": False,
                "message": "Заказ не найден!"
            }

        # Handle an unknown command
        else:
            return {
                "success": False,
                "message": "Неизвестная команда!"
            }


# Handle one connected client
def handle_client(conn, address):

    print("Connected client:", address)

    try:
        data = b""

        # Receive the complete client message
        while b"\n" not in data:
            part = conn.recv(4096)

            if not part:
                break

            data += part

        if not data:
            return

        try:
            request = json.loads(data.decode("utf-8").strip())

            if not isinstance(request, dict):
                raise ValueError("Invalid request")

            response = process_request(request)

        except (json.JSONDecodeError, ValueError):
            response = {
                "success": False,
                "message": "Некорректный запрос!"
            }

        # Send the response to the client
        message = json.dumps(response, ensure_ascii=False) + "\n"

        conn.sendall(message.encode("utf-8"))

    except (ConnectionError, OSError):
        print("Connection lost:", address)

    except Exception as error:
        print("Error:", error)

    finally:
        conn.close()
        print("Client disconnected:", address)


# Administrator panel for changing order status
def admin_panel():

    while True:
        try:
            print("\n--- Administrator Panel ---")
            order_id = input("Enter order number (0 - exit): ")

            if order_id == "0":
                break

            order_id = int(order_id)

            print("1 - Accepted")
            print("2 - Preparing for delivery")
            print("3 - On the way")
            print("4 - Delivered")

            choice = input("Choose new status: ")

            statuses = {
                "1": "Принят",
                "2": "Готовится к отправке",
                "3": "В пути",
                "4": "Доставлен"
            }

            if choice in statuses:
                result = process_request({
                    "command": "update_status",
                    "order_id": order_id,
                    "status": statuses[choice]
                })

                print(result["message"])
            else:
                print("Wrong choice!")

        except ValueError:
            print("Enter a correct number!")


# Start the server
def start_server():

    load_orders()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))
    server.listen(5)

    print("Delivery server started!")
    print("Waiting for connections...")
    print("Address:", HOST)
    print("Port:", PORT)

    # Start the administrator panel in a separate thread
    admin_thread = threading.Thread(
        target=admin_panel,
        daemon=True
    )
    admin_thread.start()

    # Accept connections from clients
    while True:
        try:
            conn, address = server.accept()

            # Create a separate thread for each client
            client_thread = threading.Thread(
                target=handle_client,
                args=(conn, address)
            )

            client_thread.start()

        except KeyboardInterrupt:
            print("Server stopped!")
            break

    server.close()


if __name__ == "__main__":
    start_server()
