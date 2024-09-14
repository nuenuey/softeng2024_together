import tkinter as tk
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def show_result(message: str):
    console.print(Panel(":banana: [bold yellow]팩토리얼 구하는 프로그램[/bold yellow] :banana:",
                        border_style="yellow", expand=False))
    console.print(message, style="bold yellow")

def show():
    n = int(input_entry.get())
    if n >= 0:
        result = factorial(n)
        message = f"{n}의 팩토리얼은 {result}입니다."
        show_result(message)

    window.destroy()

def main():
    global window, input_entry
    
    window = tk.Tk()
    window.title("팩토리얼 계산기")
    window.geometry("300x100")
    
    tk.Label(window, text="숫자를 입력하세요:", padx=20, pady=10).pack()
    
    input_entry = tk.Entry(window)
    input_entry.pack(pady=(0, 10))
    
    tk.Button(window, text="결과 보기", command=show).pack()
    
    window.mainloop()

if __name__ == "__main__":
    main()
