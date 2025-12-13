from collections import deque

def is_palindrome(text: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in text if not ch.isspace())
    d = deque(cleaned)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True

def main():
    print("Перевірка рядка на паліндром")
    print("Введіть рядок або 'q' для виходу\n")

    while True:
        user_input = input("Рядок: ")

        if user_input.lower() == "q":
            print("Роботу завершено")
            break

        if is_palindrome(user_input):
            print("✅ Це паліндром\n")
        else:
            print("❌ Це НЕ паліндром\n")


if __name__ == "__main__":
    main()