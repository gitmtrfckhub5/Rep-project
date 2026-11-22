
import socket
import json
import threading

HOST = "127.0.0.1"
PORT = 5000


# Create a test order for one client
def test_client(number):

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.connect((HOST, PORT))

        data = {
            "command": "create",
            "name": "Client " + str(number),
            "contact": "099123456" + str(number),
            "address": "Test Street, house " + str(number),
            "products": ["Bread", "Milk", "Cheese"]
        }

        message = json.dumps(data, ensure_ascii=False) + "\n"

        client.sendall(message.encode("utf-8"))

        response = b""

        # Receive the server response
        while b"\n" not in response:
            part = client.recv(4096)

            if not part:
                break

            response += part

        if response:
            result = json.loads(response.decode("utf-8").strip())

            print("Client", number, "received response:")
            print(result)

        client.close()

    except Exception as error:
        print("Client error", number, ":", error)


# Create three client threads
threads = []

for i in range(1, 4):

    thread = threading.Thread(
        target=test_client,
        args=(i,)
    )

    threads.append(thread)


# Start all clients
for thread in threads:
    thread.start()


# Wait until all clients finish
for thread in threads:
    thread.join()


print("\nTesting completed!")
