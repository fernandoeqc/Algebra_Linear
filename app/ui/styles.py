#import matplotlib
# from matplotlib import use
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# use('TkAgg')
font_label_config = ('Consolas', 22)
font_field_config = ('Consolas', 18)

def LatexComponent(master, text):
    fig = Figure(figsize=(5, 4), dpi=100)
    latex = "$" + text + "$"
    ax = fig.add_subplot()
    ax.clear()
    ax.text(0.2, 0.6, latex, fontsize=50)  
    canvas = FigureCanvasTkAgg(fig, master=master)
    return canvas

