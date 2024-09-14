import tkinter as tk
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def show_result(message: str):
    console.print(Panel(":grape: [bold magenta]소수 판별 프로그램[/bold magenta] :grape:",
                        border_style='magenta', expand=False))
    console.print(message, style="bold magenta")

def show():
    n = int(input_entry.get())
    if n >= 0:
        if is_prime(n):
            result_text = f"{n}은 소수입니다."
        else:
            result_text = f"{n}은 소수가 아닙니다."
        show_result(result_text)
        window.destroy()

def main():
    global input_entry, window
    
    window = tk.Tk()
    window.title("소수 판별기")
    window.geometry("300x100")
    
    tk.Label(window, text="숫자를 입력하세요:", padx=20, pady=10).pack()
    
    input_entry = tk.Entry(window)
    input_entry.pack(pady=(0, 10))
    
    tk.Button(window, text="결과 보기", command=show).pack()
    
    window.mainloop()

if __name__ == "__main__":
    main()
