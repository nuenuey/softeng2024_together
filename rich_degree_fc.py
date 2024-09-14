import tkinter as tk
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def f2c(temp_f: float) -> float:
    return (temp_f - 32) * 5 / 9


def show_result(message: str):
    console.print(Panel(':pineapple: [bold yellow]화씨-섭씨 변환 프로그램 [/bold yellow] :pineapple:', border_style="yellow", expand=False))
    console.print(message, style="bold yellow")
    

def show():
    try:
        temp_f = float(input_entry.get())
        temp_c = f2c(temp_f)
        message = f"화씨 {temp_f}F는 섭씨 {temp_c:.1f}C입니다."
        show_result(message)
    except ValueError:
        show_result("올바른 숫자를 입력하세요.")

    window.destroy()


def main():
    global window, input_entry

    window = tk.Tk()
    window.title("화씨 => 섭씨 계산기")
    window.geometry("300x100")

    tk.Label(window, text="화씨 온도를 입력하세요:", padx=20, pady=10).pack()

    input_entry = tk.Entry(window)
    input_entry.pack(pady=(0, 10))

    tk.Button(window, text="결과 보기", command=show).pack()

    window.mainloop()


if __name__ == "__main__":
    main()