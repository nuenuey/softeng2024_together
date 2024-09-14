import tkinter as tk
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def is_even(n: int) -> bool:
    return n % 2 == 0


def show_result(message: str):
    console.print(Panel(':melon: [bold green]홀짝 판별 프로그램[/bold green] :melon:', border_style="green", expand=False))
    console.print(message, style="bold green")

def show():
    try:
        n = int(input_entry.get())
        if is_even(n):
            result = "짝수"
        else:
            result = "홀수"
        message = f"{n}은 {result}입니다."
        show_result(message)
    except ValueError:
        show_result("올바른 숫자를 입력하세요.")

    window.destroy()


def main():
    global window, input_entry

    window = tk.Tk()
    window.title("홀짝 판별 프로그램")
    window.geometry("300x100")

    tk.Label(window, text="숫자를 입력하세요:", padx=20, pady=10).pack()

    input_entry = tk.Entry(window)
    input_entry.pack(pady=(0, 10))

    tk.Button(window, text="결과 보기", command=show).pack()

    window.mainloop()


if __name__ == "__main__":
    main()