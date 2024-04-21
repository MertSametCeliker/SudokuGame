import tkinter as tk
from tkinter import messagebox
import random

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Oyunu")

        self.create_board()

    def create_board(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.cells = [[None for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell_entry = tk.Entry(self.board_frame, width=2, font=('Helvetica', 16, 'bold'), bd=1, relief='solid', justify="center")
                cell_entry.grid(row=i, column=j)
                self.cells[i][j] = cell_entry

        button_frame = tk.Frame(self.root)
        button_frame.pack()

        solve_button = tk.Button(button_frame, text="Çöz", command=self.solve)
        solve_button.pack(side="left", padx=5)

        check_button = tk.Button(button_frame, text="Kontrol Et", command=self.check)
        check_button.pack(side="left", padx=5)

    def solve(self):
        # Sudoku tahtasını oku
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                cell_value = self.cells[i][j].get()
                if cell_value.isdigit():
                    row.append(int(cell_value))
                else:
                    row.append(0)
            board.append(row)
        
        if self.solve_sudoku(board):
            # Çözümü güncelle
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].delete(0, tk.END)
                    self.cells[i][j].insert(0, str(board[i][j]))
        else:
            messagebox.showerror("Hata", "Bu Sudoku çözülemez.")

    def check(self):
        # Sudoku tahtasını kontrol et
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                cell_value = self.cells[i][j].get()
                if cell_value.isdigit():
                    row.append(int(cell_value))
                else:
                    row.append(0)
            board.append(row)
        
        if self.is_valid_solution(board):
            messagebox.showinfo("Bilgi", "Sudoku doğru bir şekilde çözülmüştür.")
        else:
            messagebox.showerror("Hata", "Sudoku yanlış bir şekilde çözülmüştür.")

    def solve_sudoku(self, board):
        # Sudoku çözme algoritması
        empty_loc = self.find_empty_location(board)
        if not empty_loc:
            return True
        
        row, col = empty_loc
        for num in range(1, 10):
            if self.is_safe(board, row, col, num):
                board[row][col] = num
                if self.solve_sudoku(board):
                    return True
                board[row][col] = 0
        return False

    def find_empty_location(self, board):
        # Boş bir konum bulma
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def is_safe(self, board, row, col, num):
        # Belirli bir sayının güvenli olup olmadığını kontrol etme
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    def is_valid_solution(self, board):
        # Çözümün doğru olup olmadığını kontrol etme
        for i in range(9):
            for j in range(9):
                if not self.is_safe(board, i, j, board[i][j]):
                    return False
        return True

root = tk.Tk()
app = SudokuGame(root)
root.mainloop()
