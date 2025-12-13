from queue import Queue
import random
import time

request_queue = Queue()

request_id = 1


def generate_request():
    global request_id
    request = {
        "id": request_id,
        "type": random.choice(["Техпідтримка", "Консультація", "Нове замовлення"])
    }
    request_queue.put(request)
    print(f"Згенеровано заявку №{request['id']} ({request['type']})")
    request_id += 1


def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється заявка №{request['id']} ({request['type']})")
    else:
        print("Черга порожня, немає заявок для обробки")


def main():
    print("Система обробки заявок запущена (Ctrl+C для виходу)\n")
    try:
        while True:
            generate_request()
            process_request()
            process_request()
            time.sleep(1)  
    except KeyboardInterrupt:
        print("\nРоботу програми завершено")


if __name__ == "__main__":
    main()
