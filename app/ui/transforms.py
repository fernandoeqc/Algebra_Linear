from tkinter import *
from tkinter import ttk
from app.algebra import *
from ..transformation import *
from .styles import font_field_config, font_label_config


def GenericOperation2D(root: Widget, handler):
    frame = ttk.Frame(root)

    row = ttk.Frame(frame)
    label = ttk.Label(row, text='Vetor', font=font_label_config)
    label.grid(row=0, column=0)

    first = DoubleVar(frame, 0)
    first_entry = ttk.Entry(row, textvariable=first, font=font_field_config, width=8)
    first_entry.grid(row=0, column=1, padx=10)

    second = DoubleVar(frame, 0)
    second_entry = ttk.Entry(row, textvariable=second, font=font_field_config, width=8)
    second_entry.grid(row=0, column=2, padx=10)

    row.pack()

    result_var = StringVar(frame)
    text_result = ttk.Label(frame, textvariable=result_var, font=font_label_config)

    def calculate():
        value = Vector(2, [first.get(), second.get()])
        result = handler(value)
        text = 'X={} Y={}'.format(result.get(1, 1), result.get(2, 1))
        result_var.set(text)

    button = ttk.Button(frame, text='Calcular', command=calculate)
    button.pack(pady=10)

    text_result.pack()

    return frame


def GenericOperation3D(root: Widget, handler):
    frame = ttk.Frame(root)

    row = ttk.Frame(frame)
    label = ttk.Label(row, text='Vetor', font=font_label_config)
    label.grid(row=0, column=0)

    first = DoubleVar(frame, 0)
    first_entry = ttk.Entry(row, textvariable=first, font=font_field_config, width=8)
    first_entry.grid(row=0, column=1, padx=10)

    second = DoubleVar(frame, 0)
    second_entry = ttk.Entry(row, textvariable=second, font=font_field_config, width=8)
    second_entry.grid(row=0, column=2, padx=10)

    third = DoubleVar(frame, 0)
    third_entry = ttk.Entry(row, textvariable=third, font=font_field_config, width=8)
    third_entry.grid(row=0, column=3, padx=10)

    row.pack()

    result_var = StringVar(frame)
    text_result = ttk.Label(frame, textvariable=result_var, font=font_label_config)

    def calculate():
        value = Vector(3, [first.get(), second.get(), third.get()])
        result = handler(value)
        text = 'X={} Y={} Z={}'.format(result.get(1, 1), result.get(2, 1), result.get(3, 1))
        result_var.set(text)

    button = ttk.Button(frame, text='Calcular', command=calculate)
    button.pack(pady=10)

    text_result.pack()

    return frame


def RotationOperation2D(root: Widget, handler):
    frame = ttk.Frame(root)

    row = ttk.Frame(frame)
    label = ttk.Label(row, text='Vetor', font=font_label_config)
    label.grid(row=0, column=0)

    first = DoubleVar(frame, 0)
    first_entry = ttk.Entry(row, textvariable=first, font=font_field_config, width=8)
    first_entry.grid(row=0, column=1, padx=10)

    second = DoubleVar(frame, 0)
    second_entry = ttk.Entry(row, textvariable=second, font=font_field_config, width=8)
    second_entry.grid(row=0, column=2, padx=10)

    row.pack()

    row_angle = ttk.Frame(frame)

    angle_label = ttk.Label(row_angle, text='Angulo º', font=font_label_config)
    angle_label.grid(row=0, column=0)

    angle = DoubleVar(frame, 0)
    angle_entry = ttk.Entry(row_angle, textvariable=angle, font=font_field_config)
    angle_entry.grid(row=0, column=1)

    row_angle.pack()

    result_var = StringVar(frame)
    text_result = ttk.Label(frame, textvariable=result_var, font=font_label_config)

    def calculate():
        value = Vector(2, [first.get(), second.get()])
        result = handler(value, angle.get())
        text = 'X={} Y={}'.format(result.get(1, 1), result.get(2, 1))
        result_var.set(text)

    button = ttk.Button(frame, text='Calcular', command=calculate)
    button.pack(pady=10)

    text_result.pack()

    return frame


def RotationOperation3D(root: Widget, handler):
    frame = ttk.Frame(root)

    row = ttk.Frame(frame)
    label = ttk.Label(row, text='Vetor', font=font_label_config)
    label.grid(row=0, column=0)

    first = DoubleVar(frame, 0)
    first_entry = ttk.Entry(row, textvariable=first, font=font_field_config, width=8)
    first_entry.grid(row=0, column=1, padx=10)

    second = DoubleVar(frame, 0)
    second_entry = ttk.Entry(row, textvariable=second, font=font_field_config, width=8)
    second_entry.grid(row=0, column=2, padx=10)

    third = DoubleVar(frame, 0)
    third_entry = ttk.Entry(row, textvariable=third, font=font_field_config, width=8)
    third_entry.grid(row=0, column=3, padx=10)

    row.pack()

    row_angle = ttk.Frame(frame)

    angle_label = ttk.Label(row_angle, text='Angulo º', font=font_label_config)
    angle_label.grid(row=0, column=0)

    angle = DoubleVar(frame, 0)
    angle_entry = ttk.Entry(row_angle, textvariable=angle, font=font_field_config)
    angle_entry.grid(row=0, column=1)

    row_angle.pack()

    result_var = StringVar(frame)
    text_result = ttk.Label(frame, textvariable=result_var, font=font_label_config)

    def calculate():
        value = Vector(3, [first.get(), second.get(), third.get()])
        result = handler(value, angle.get())
        text = 'X={} Y={} Z={}'.format(result.get(1, 1), result.get(2, 1), result.get(3, 1))
        result_var.set(text)

    button = ttk.Button(frame, text='Calcular', command=calculate)
    button.pack(pady=10)

    text_result.pack()

    return frame


def GenericOperationWithParameter2D(root: Widget, handler, parameter1_text, parameter2_text):
    frame = ttk.Frame(root)

    row = ttk.Frame(frame)
    label = ttk.Label(row, text='Vetor', font=font_label_config)
    label.grid(row=0, column=0)

    first = DoubleVar(frame, 0)
    first_entry = ttk.Entry(row, textvariable=first, font=font_field_config, width=8)
    first_entry.grid(row=0, column=1, padx=10)

    second = DoubleVar(frame, 0)
    second_entry = ttk.Entry(row, textvariable=second, font=font_field_config, width=8)
    second_entry.grid(row=0, column=2, padx=10)

    row.pack()

    row_parameters = ttk.Frame(frame)

    parameter1_label = ttk.Label(row_parameters, text=parameter1_text, font=font_label_config)
    parameter1_label.grid(row=0, column=0)

    parameter1 = DoubleVar(frame, 0)
    parameter1_entry = ttk.Entry(row_parameters, textvariable=parameter1, font=font_field_config, width=8)
    parameter1_entry.grid(row=0, column=1)

    parameter2_label = ttk.Label(row_parameters, text=parameter2_text, font=font_label_config)
    parameter2_label.grid(row=0, column=2)

    parameter2 = DoubleVar(frame, 0)
    parameter2_entry = ttk.Entry(row_parameters, textvariable=parameter2, font=font_field_config, width=8)
    parameter2_entry.grid(row=0, column=3)

    row_parameters.pack()

    result_var = StringVar(frame)
    text_result = ttk.Label(frame, textvariable=result_var, font=font_label_config)

    def calculate():
        value = Vector(2, [first.get(), second.get()])
        result = handler(value, parameter1.get(), parameter2.get())
        text = 'X={} Y={}'.format(result.get(1, 1), result.get(2, 1))
        result_var.set(text)

    button = ttk.Button(frame, text='Calcular', command=calculate)
    button.pack(pady=10)

    text_result.pack()

    return frame


def GenericOperationWithParameter3D(root: Widget, handler):
    frame = ttk.Frame(root)

    row = ttk.Frame(frame)
    label = ttk.Label(row, text='Vetor', font=font_label_config)
    label.grid(row=0, column=0)

    first = DoubleVar(frame, 0)
    first_entry = ttk.Entry(row, textvariable=first, font=font_field_config, width=8)
    first_entry.grid(row=0, column=1, padx=10)

    second = DoubleVar(frame, 0)
    second_entry = ttk.Entry(row, textvariable=second, font=font_field_config, width=8)
    second_entry.grid(row=0, column=2, padx=10)

    third = DoubleVar(frame, 0)
    third_entry = ttk.Entry(row, textvariable=third, font=font_field_config, width=8)
    third_entry.grid(row=0, column=3, padx=10)

    row.pack()

    row_parameters = ttk.Frame(frame)

    parameter1_label = ttk.Label(row_parameters, text='dx', font=font_label_config)
    parameter1_label.grid(row=0, column=0)

    parameter1 = DoubleVar(frame, 0)
    parameter1_entry = ttk.Entry(row_parameters, textvariable=parameter1, font=font_field_config, width=8)
    parameter1_entry.grid(row=0, column=1)

    parameter2_label = ttk.Label(row_parameters, text='dy', font=font_label_config)
    parameter2_label.grid(row=0, column=2)

    parameter2 = DoubleVar(frame, 0)
    parameter2_entry = ttk.Entry(row_parameters, textvariable=parameter2, font=font_field_config, width=8)
    parameter2_entry.grid(row=0, column=3)

    parameter3_label = ttk.Label(row_parameters, text='dz', font=font_label_config)
    parameter3_label.grid(row=0, column=4)

    parameter3 = DoubleVar(frame, 0)
    parameter3_entry = ttk.Entry(row_parameters, textvariable=parameter3, font=font_field_config, width=8)
    parameter3_entry.grid(row=0, column=5)

    row_parameters.pack()

    result_var = StringVar(frame)
    text_result = ttk.Label(frame, textvariable=result_var, font=font_label_config)

    def calculate():
        value = Vector(3, [first.get(), second.get(), third.get()])
        result = handler(value, parameter1.get(), parameter2.get(), parameter3.get())
        text = 'X={} Y={} Z={}'.format(result.get(1, 1), result.get(2, 1), result.get(3, 1))
        result_var.set(text)

    button = ttk.Button(frame, text='Calcular', command=calculate)
    button.pack(pady=10)

    text_result.pack()

    return frame


def MainScreen(root):
    frame = ttk.Frame(root)

    operation = StringVar(frame, 'reflection2DX')
    operators = [
        'translate2D', 'translate3D', 'rotation2D', 'rotation3DX', 'rotation3DY',
        'rotation3DZ', 'reflection2DX', 'reflection2DY', 'reflection3DX', 'reflection3DY',
        'reflection3DZ', 'projection2DX', 'projection2DY', 'projection3DX', 'projection3DY',
        'projection3DZ', 'shearing'
    ]

    operation_frame = ttk.Frame(frame)

    pages = {
        'translate2D': GenericOperationWithParameter2D(operation_frame, Transformations.translate2D, 'dx', 'dy'),
        'translate3D': GenericOperationWithParameter3D(operation_frame, Transformations.translate3D),
        'rotation2D': RotationOperation2D(operation_frame, Transformations.rotation2D),
        'rotation3DX': RotationOperation3D(operation_frame, Transformations.rotation3DX),
        'rotation3DY': RotationOperation3D(operation_frame, Transformations.rotation3DY),
        'rotation3DZ': RotationOperation3D(operation_frame, Transformations.rotation3DZ),
        'reflection2DX': GenericOperation2D(operation_frame, Transformations.reflection2DX),
        'reflection2DY': GenericOperation2D(operation_frame, Transformations.reflection2DY),
        'reflection3DX': GenericOperation3D(operation_frame, Transformations.reflection3DX),
        'reflection3DY': GenericOperation3D(operation_frame, Transformations.reflection3DY),
        'reflection3DZ': GenericOperation3D(operation_frame, Transformations.reflection3DZ),
        'projection2DX': GenericOperation2D(operation_frame, Transformations.projection2DX),
        'projection2DY': GenericOperation2D(operation_frame, Transformations.projection2DY),
        'projection3DX': GenericOperation3D(operation_frame, Transformations.projection3DX),
        'projection3DY': GenericOperation3D(operation_frame, Transformations.projection3DY),
        'projection3DZ': GenericOperation3D(operation_frame, Transformations.projection3DZ),
        'shearing': GenericOperationWithParameter2D(operation_frame, Transformations.shearing, 'kx', 'ky'),
    }

    current = pages.get('reflection2DX')

    def change_operator(arg):
        for _, item in operation_frame.children.items():
            item.pack_forget()

        widget = pages.get(arg)
        widget.pack()


    option_menu = ttk.OptionMenu(frame, operation, 'reflection2DX', *operators, command=change_operator)
    option_menu.pack()

    operation_frame.pack()
    current.pack()

    frame.pack()
    return frame


def build_app():
    root = Tk()
    root.title('Algebra Linear')
    root.geometry('600x350')

    MainScreen(root)

    root.mainloop()


if __name__ == '__main__':
    build_app()
