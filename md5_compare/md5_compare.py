import sys
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

CHUNK_SIZE = 64 * 1024


def file_md5(filename):
    md5 = hashlib.md5()

    with open(filename, "rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            md5.update(chunk)

    return md5.hexdigest()

def get_app_dir():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent

class MD5App:
    def __init__(self, root):
        self.root = root
        self.root.title("MD5 文件校验")
        self.root.geometry("600x300")
        self.root.resizable(False, False)

        self.file1 = tk.StringVar()
        self.file2 = tk.StringVar()

        self.create_widgets()
         # 默认从程序所在目录打开
        self.last_dir = get_app_dir()

    def create_widgets(self):
        tk.Label(self.root, text="文件1").grid(row=0, column=0, padx=10, pady=15)

        tk.Entry(self.root, textvariable=self.file1, width=55).grid(
            row=0, column=1, padx=5
        )

        tk.Button(
            self.root,
            text="浏览",
            width=8,
            command=lambda: self.select_file(self.file1)
        ).grid(row=0, column=2, padx=10)

        tk.Label(self.root, text="文件2").grid(row=1, column=0, padx=10, pady=10)

        tk.Entry(self.root, textvariable=self.file2, width=55).grid(
            row=1, column=1, padx=5
        )

        tk.Button(
            self.root,
            text="浏览",
            width=8,
            command=lambda: self.select_file(self.file2)
        ).grid(row=1, column=2, padx=10)

        tk.Button(
            self.root,
            text="开始比较",
            width=15,
            height=2,
            command=self.compare
        ).grid(row=2, column=1, pady=20)

        self.result_label = tk.Label(
            self.root,
            text="请选择两个文件",
            font=("Microsoft YaHei", 12)
        )
        self.result_label.grid(row=3, column=0, columnspan=3, pady=5)

        self.md5_label = tk.Label(
            self.root,
            text="",
            justify=tk.LEFT,
            anchor="w"
        )
        self.md5_label.grid(row=4, column=0, columnspan=3, padx=20, sticky="w")

    def select_file(self, variable):
        initial_dir = Path(__file__).resolve().parent

        filename = filedialog.askopenfilename(
            initialdir=self.last_dir,
            title="选择文件"
        )

        if filename:
            variable.set(filename)
            self.last_dir = Path(filename).parent

    def compare(self):
        file1 = self.file1.get()
        file2 = self.file2.get()

        if not file1 or not file2:
            messagebox.showwarning("提示", "请选择两个文件")
            return

        if not Path(file1).is_file():
            messagebox.showerror("错误", f"文件不存在：\n{file1}")
            return

        if not Path(file2).is_file():
            messagebox.showerror("错误", f"文件不存在：\n{file2}")
            return

        try:
            self.result_label.config(text="正在计算 MD5...")
            self.root.update()

            md5_1 = file_md5(file1)
            md5_2 = file_md5(file2)

            self.md5_label.config(
                text=f"文件1 MD5：{md5_1}\n文件2 MD5：{md5_2}"
            )

            if md5_1 == md5_2:
                self.result_label.config(text="✓ 文件一致")
            else:
                self.result_label.config(text="✗ 文件不一致")

        except Exception as e:
            messagebox.showerror("错误", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = MD5App(root)
    root.mainloop()