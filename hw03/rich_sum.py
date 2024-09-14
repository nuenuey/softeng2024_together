import tkinter as tk
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def is_even(n: int) -> bool:
    return n % 2 == 0

def calculate_even_sum() -> int:
    total = 0
    for i in range(1, 101):
        if is_even(i):
            total += i
    return total

def show_result(message: str):
    console.print(Panel(Text(message, style="bold green")))

def show():
    total = calculate_even_sum()
    result_text = f"1부터 100까지의 짝수 합은 {total}입니다."
    show_result(result_text)
    window.destroy()

def main():
    global window
    
    window = tk.Tk()
    window.title("짝수 합 계산기")
    window.geometry("300x100")
    
    tk.Label(window, text="1부터 100까지의 짝수 합을 계산합니다.", padx=20, pady=10).pack()
    tk.Button(window, text="결과", command=show).pack(pady=10)
    
    window.mainloop()

if __name__ == "__main__":
    main()
