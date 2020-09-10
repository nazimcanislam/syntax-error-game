import os
import sys


class App:

    @staticmethod
    def get_total_data() -> dict:
        """
        Ana dizindeki 'app.py' dosyasının ve util/ klasörünün altındaki
        ilk .py uzantılı dosyaların satır sayısılarını toplayıp geri döndürür.
        """

        total_line: int = 0
        total_bytes: int = 0

        with open("main.py", "r", encoding="utf-8") as f:
            total_line += len(f.readlines())
            total_bytes += os.path.getsize("main.py")

        for filename in os.listdir("util"):
            filename: str = filename

            total_bytes += os.path.getsize(f"util/{filename}")

            if filename.endswith(".py"):
                with open(f"util/{filename}", "r", encoding="utf-8") as f:
                    total_line += len(f.readlines())

        return {
            "line": total_line,
            "bytes": total_bytes
        }

    @staticmethod
    def main(*args: list, **kwargs: dict) -> None:
        data: dict = App.get_total_data()

        print(f"{os.path.basename(os.getcwd())} için...\n")
        print(f"Toplam satır: {data.get('line')}")
        print(f"Toplam byte: {data.get('bytes')}")

        input("\nYa, Python harika değil mi işte?\n\n")


if __name__ == "__main__":
    App.main(sys.argv)
