import tkinter as tk
from tkinter import simpledialog, messagebox


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    window = tk.Tk()
    window.withdraw()


    n = simpledialog.askinteger("소수 판별 프로그램", "숫자를 입력하시오:")

    if n is not None:
        if is_prime(n):
            result = "소수"
        else:
            result = "소수가 아님"

        messagebox.showinfo("결과", f"{n}은 {result}입니다.")

if __name__ == "__main__":
    main()