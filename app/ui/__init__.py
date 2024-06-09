from tkinter import *
from tkinter import ttk
from app.ui.page_rank import PageRankScreen
from app.ui.transforms import MainScreen as TransformScreen

def build_app():
    root = Tk()
    root.title('Algebra Linear')
    root.geometry('700x550')

    notebook = ttk.Notebook(root)
    notebook.add(PageRankScreen(notebook), text='Page rank')
    notebook.add(TransformScreen(notebook), text='Transformações')

    notebook.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    build_app()
