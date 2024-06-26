from tkinter import *
from tkinter import ttk
from app.algebra import Matrix
from app.page_rank import PageRank
from app.ui.styles import font_field_config, font_label_config


def InputShape(master, create_matrix, run_page_rank):
    frame = ttk.Frame(master)

    line_label = ttk.Label(frame, text='Linhas', font=font_label_config)
    line_label.grid(column=0, row=0)

    line_entry = ttk.Entry(frame, font=font_field_config, width=10)
    line_entry.grid(column=1, row=0)

    column_label = ttk.Label(frame, text='Colunas', font=font_label_config)
    column_label.grid(column=2, row=0)

    column_entry = ttk.Entry(frame, font=font_field_config, width=10)
    column_entry.grid(column=3, row=0)

    create_button = ttk.Button(frame, text='Criar', width=20, command=lambda : create_matrix(int(line_entry.get()), int(column_entry.get())))
    create_button.grid(column=1, row=1)

    run_button = ttk.Button(frame, text='Executar page rank', width=20, command=run_page_rank)
    run_button.grid(column=3, row=1)

    return frame


def PageRankScreen(master):
    frame = ttk.Frame(master)

    matrix_frame_input = ttk.Frame(frame)
    matrix_frame_input.grid(column=0, row=1)

    text_result = StringVar(frame, '')
    label_result = ttk.Label(frame, textvariable=text_result, font=font_label_config)
    label_result.grid(column=0, row=2)

    rows_value = IntVar(frame, 0)
    cols_value = IntVar(frame, 0)

    def create_matrix(rows, cols):
        text_result.set('')
        rows_value.set(rows)
        cols_value.set(cols)
        items = [item for _, item in matrix_frame_input.children.items()]
        for item in items:
            item.destroy()

        for i in range(rows):
            for j in range(cols):
                var = IntVar(matrix_frame_input, 0)
                entry = Entry(matrix_frame_input, textvariable=var, width=10, font=font_field_config)
                entry.grid(column=j, row=i)


    def run_page_rank():
        rows = rows_value.get()
        cols = cols_value.get()
        items = [int(item.get()) for _, item in matrix_frame_input.children.items()]
        matrix = Matrix(rows, cols, items)
        result = PageRank.run(matrix)
        items = [
            [f'Site {index}', result.get(index)]
            for index in range(1, result.dim + 1)
        ]
        items.sort(key=lambda x: x[1] * -1)
        text = '\n'.join([f'{label} = {value}' for label, value in items])
        text_result.set(text)

    input_shape_frame = InputShape(frame, create_matrix, run_page_rank)
    input_shape_frame.grid(column=0, row=0)

    frame.pack(fill='both', expand=True)
    return frame


def build_app():
    root = Tk()
    root.title('Algebra Linear')
    root.geometry('600x350')

    PageRankScreen(root)

    root.mainloop()


if __name__ == '__main__':
    build_app()
