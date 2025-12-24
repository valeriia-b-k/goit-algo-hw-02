import argparse
import shutil
from pathlib import Path


def copy_and_sort_files(src_dir: Path, dest_dir: Path) -> None:
    try:
        for item in src_dir.iterdir():
            try:
                if item.is_dir():
                    copy_and_sort_files(item, dest_dir)
                elif item.is_file():
                    ext = item.suffix.lower().lstrip(".")
                    if ext == "":
                        ext = "no_extension"

                    target_subdir = dest_dir / ext
                    target_subdir.mkdir(parents=True, exist_ok=True)

                    shutil.copy2(item, target_subdir / item.name)

            except PermissionError:
                print(f"Немає доступу до: {item}")
            except OSError as e:
                print(f"Помилка при обробці {item}: {e}")

    except FileNotFoundError:
        print(f"Директорію не знайдено: {src_dir}")
    except PermissionError:
        print(f"Немає доступу до директорії: {src_dir}")
    except OSError as e:
        print(f"Помилка при читанні директорії {src_dir}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Рекурсивно копіює файли з вихідної директорії та сортує їх за розширенням."
    )
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням: dist)"
    )

    args = parser.parse_args()

    src_dir = Path(args.source)
    dest_dir = Path(args.destination)

    if not src_dir.exists():
        print("Вихідна директорія не існує.")
        return
    if not src_dir.is_dir():
        print("Вказаний шлях джерела не є директорією.")
        return

    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Не вдалося створити директорію призначення {dest_dir}: {e}")
        return

    copy_and_sort_files(src_dir, dest_dir)
    print(f"✅ Готово! Файли скопійовано та відсортовано в: {dest_dir.resolve()}")


if __name__ == "__main__":
    main()
