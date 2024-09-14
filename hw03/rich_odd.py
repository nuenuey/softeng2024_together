from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

import tkinter as tk
from tkinter import simpledialog, messagebox

console = Console()

def is_even(n: int) -> bool:
    return n % 2 == 0

def main():

    window = tk.Tk()
    window.withdraw()
    n = simpledialog.askinteger("홀짝을 판별하는 프로그램", "숫자를 입력하시오:")

    if n is not None:
        if is_even(n):
            result = "짝수"
        else:
            result = "홀수"

    # Rich
    console.print(Panel("💡 [bold yellow]홀짝 판별 프로그램[/bold yellow] 💡", expand=False))

    if is_even(n):
        result = Text(f"{n}은 짝수입니다.", style="bold blue")
    else:
        result = Text(f"{n}은 홀수입니다.", style="bold magenta")

    console.print(result)

if __name__ == "__main__":
    main()
