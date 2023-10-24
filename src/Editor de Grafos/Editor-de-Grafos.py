
from sage.all import *
from sage.graphs.graph_plot import GraphPlot

import tkinter as tk
from tkinter import font
import tkinter.simpledialog
from tkinter import colorchooser

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

import os
class Palette:
    def __init__(self, gui):
        self.gui = gui
        self.canvas = self.gui.canvas
        self.top = tk.Toplevel(self.canvas)
        self.top.title('Color Palette')

        self.colores = []
        # /* Red */
        self.colores.append(
            ['#ffebee', '#ffcdd2', '#ef9a9a', '#e57373', '#ef5350', '#f44336', '#e53935', '#d32f2f',
             '#c62828', '#b71c1c', '#f44336'])
        # /* Pink */
        self.colores.append(
            ['#fce4ec', '#f8bbd0', '#f48fb1', '#f06292', '#ec407a', '#e91e63', '#d81b60', '#c2185b',
             '#ad1457', '#880e4f', '#e91e63'])
        # /* Purple */
        self.colores.append(
            ['#f3e5f5', '#e1bee7', '#ce93d8', '#ba68c8', '#ab47bc', '#9c27b0', '#8e24aa', '#7b1fa2',
             '#6a1b9a', '#4a148c', '#9c27b0'])
        # /* Deep Purple */
        self.colores.append(
            ['#ede7f6', '#d1c4e9', '#b39ddb', '#9575cd', '#7e57c2', '#673ab7', '#5e35b1', '#512da8',
             '#4527a0', '#311b92', '#673ab7'])
        # /* Indigo */
        self.colores.append(
            ['#e8eaf6', '#c5cae9', '#9fa8da', '#7986cb', '#5c6bc0', '#3f51b5', '#3949ab', '#303f9f',
             '#283593', '#1a237e', '#3f51b5'])
        # /* Blue */
        self.colores.append(
            ['#e3f2fd', '#bbdefb', '#90caf9', '#64b5f6', '#42a5f5', '#2196f3', '#1e88e5', '#1976d2',
             '#1565c0', '#0d47a1', '#2196f3'])
        # /* Light Blue */
        self.colores.append(
            ['#e1f5fe', '#b3e5fc', '#81d4fa', '#4fc3f7', '#29b6f6', '#03a9f4', '#039be5', '#0288d1',
             '#0277bd', '#01579b', '#03a9f4'])
        # /* Cyan */
        self.colores.append(
            ['#e0f7fa', '#b2ebf2', '#80deea', '#4dd0e1', '#26c6da', '#00bcd4', '#00acc1', '#0097a7',
             '#00838f', '#006064', '#00bcd4'])
        # /* Teal */
        self.colores.append(
            ['#e0f2f1', '#b2dfdb', '#80cbc4', '#4db6ac', '#26a69a', '#009688', '#00897b', '#00796b',
             '#00695c', '#004d40', '#009688'])
        # /* Green */
        self.colores.append(
            ['#e8f5e9', '#c8e6c9', '#a5d6a7', '#81c784', '#66bb6a', '#4caf50', '#43a047', '#388e3c',
             '#2e7d32', '#1b5e20', '#4caf50'])
        # /* Light Green */
        self.colores.append(
            ['#f1f8e9', '#dcedc8', '#c5e1a5', '#aed581', '#9ccc65', '#8bc34a', '#7cb342', '#689f38',
             '#558b2f', '#33691e', '#8bc34a'])
        # /* Lime */
        self.colores.append(
            ['#f9fbe7', '#f0f4c3', '#e6ee9c', '#dce775', '#d4e157', '#cddc39', '#c0ca33', '#afb42b',
             '#9e9d24', '#827717', '#cddc39'])
        # /* Yellow */
        self.colores.append(
            ['#fffde7', '#fff9c4', '#fff59d', '#fff176', '#ffee58', '#ffeb3b', '#fdd835', '#fbc02d',
             '#f9a825', '#f57f17', '#ffeb3b'])
        # /* Amber */
        self.colores.append(
            ['#fff8e1', '#ffecb3', '#ffe082', '#ffd54f', '#ffca28', '#ffc107', '#ffb300', '#ffa000',
             '#ff8f00', '#ff6f00', '#ffc107'])
        # /* Orange */
        self.colores.append(
            ['#fff3e0', '#ffe0b2', '#ffcc80', '#ffb74d', '#ffa726', '#ff9800', '#fb8c00', '#f57c00',
             '#ef6c00', '#e65100', '#ff9800'])
        # /* Deep Orange */
        self.colores.append(
            ['#fbe9e7', '#ffccbc', '#ffab91', '#ff8a65', '#ff7043', '#ff5722', '#f4511e', '#e64a19',
             '#d84315', '#bf360c', '#ff5722'])
        # /* Brown */
        self.colores.append(
            ['#efebe9', '#d7ccc8', '#bcaaa4', '#a1887f', '#8d6e63', '#795548', '#6d4c41', '#5d4037',
             '#4e342e', '#3e2723', '#795548'])
        # /* Grey */
        self.colores.append(
            ['#fafafa', '#f5f5f5', '#eeeeee', '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161',
             '#424242', '#212121', '#9e9e9e'])
        # /* Blue Grey */
        self.colores.append(
            ['#eceff1', '#cfd8dc', '#b0bec5', '#90a4ae', '#78909c', '#607d8b', '#546e7a', '#455a64',
             '#37474f', '#263238', '#607d8b'])
        # /* White / Black */
        self.colores.append(['#ffffff', '#000000'])

        for j, columna in enumerate(self.colores):
            for i, color in enumerate(reversed(columna)):
                button = tk.Button(self.top, bg=color, width=3, height=3)
                button.bind('<Button-1>', lambda event, color=color: self.button_press(event, self.top, color))
                button.grid(row=i, column=j)

    def button_press(self, event, top, color):
        event.widget.config(relief=tk.SUNKEN)
        if color is not None:
            self.gui.color = color
        else:
            self.gui.color = ""
        top.destroy()

class Titulo:
    def __init__(self,gui):
        self.gui = gui
        self.canvas = self.gui.canvas

        self.title = str(tkinter.simpledialog.askstring("Titluo del grafo", "Titulo del grafo"))
        if self.title is None:
            self.title = ""
        self.id = tk.Label(self.canvas, text=self.title, font=("Arial", 24))

        self.id.bind("<Button-1>", self.edit_title)
        # Set the position of the label on the canvas to center it relative to the canvas size
        self.id.place(relx=0.5, rely=0.1, anchor="center")

        self.x, self.y = self.id.winfo_x(), self.id.winfo_y()

    def get_title_text(self):
        return self.title

    def edit_title(self,event):
        x,y = self.x,self.y
        if self.gui.modo == "configurar":
            old_label = self.title
            self.id.destroy()

            entry = tk.Entry(self.canvas, width=20)
            entry.place(relx=0.5, rely=0.1, anchor="center")

            # focus the entry widget
            entry.focus_set()

            def save_label(event):
                new_label = entry.get()
                self.title = new_label
                self.id = tk.Label(self.canvas, text=self.title, font=("Arial", 24))
                self.id.bind("<Button-1>", self.edit_title)
                self.id.place(relx=0.5, rely=0.1, anchor="center")

                entry.destroy()


            # bind the Return key to the entry widget to save the new label and remove the entry widget
            entry.bind("<Return>", save_label)

            def escape_label(event):
                self.title = old_label
                self.id = tk.Label(self.canvas, text=self.title, font=("Arial", 24))
                self.id.bind("<Button-1>", self.edit_title)
                self.id.place(relx=0.5, rely=0.1, anchor="center")

                entry.destroy()

                self.gui.canvas.focus()

            entry.bind("<Escape>", escape_label)
            entry.bind("<FocusOut>", escape_label)
class Impresion:
    def __init__(self,gui):
        self.path = None
        self.num_dibujo = None
        self.Dibujo_path = None

        self.gui = gui
        self.canvas = self.gui.canvas
        self.figsize = self.gui.figsize

        self.dashed_edges = []
        self.dotted_edges = []
        self.dashdot_edges = []
        self.solid_edges = []



        if self.gui.agregar_flechas_bool.get() == True:
            self.G = DiGraph({node.index : [] for node in self.gui.nodes}, loops=True, multiedges=self.gui.has_multiedges())
            self.crear_edges(self.G)

            if self.gui.layout_option.get() != "none":
                self.options = {
                    'title': self.gui.title.get_title_text(),
                    'vertex_size': 350,
                    'vertex_labels': self.vertex_label_dict(),
                    'vertex_color': '#dce775',
                    'vertex_colors': self.vertex_colors_dict(),
                    'layout': self.gui.layout_option.get(),
                    'edge_color': 'black',
                    'edge_labels': True,
                    'edge_thickness': 2,
                    'iterations': 100000,
                    'tree_orientation': 'down',
                    'heights': None,
                    'graph_border': False,
                    'talk': False,
                    'color_by_label': False,
                    'partition': None,
                    'edge_labels_background': 'transparent' if self.gui.has_multiedges() else 'white',  # 'transparent' o color 'white'
                    'save_pos': True,
                    'pos': self.pos_dict()}
            else:
                self.options = {
                    'title': self.gui.title.get_title_text(),
                    'vertex_size': 350,
                    'vertex_labels': self.vertex_label_dict(),
                    'vertex_color': '#dce775',
                    'vertex_colors': self.vertex_colors_dict(),
                    'edge_color': 'black',
                    'edge_labels': True,
                    'edge_thickness': 2,
                    'iterations': 100000,
                    'tree_orientation': 'down',
                    'heights': None,
                    'graph_border': False,
                    'talk': False,
                    'color_by_label': False,
                    'partition': None,
                    'edge_labels_background': 'transparent' if self.gui.has_multiedges() else 'white',  # 'transparent' o color 'white'
                    'save_pos': True,
                    'pos': self.pos_dict()}

            """
            self.options = {
                'title': self.gui.title.get_title_text(),
                'vertex_size': 200+ round(130*(len(self.gui.nodes) // 6 )), # *(len(self.gui.nodes) // 5 + 1) es un factor de crecimiento lineal segun la cantidad de nodos en el grafo
                'vertex_labels': self.vertex_label_dict(),
                'vertex_color': '#dce775',
                'vertex_colors': self.vertex_colors_dict(),
                'layout': self.gui.layout_option.get(),
                'edge_style': 'solid', #“solid”, “dashed”, “dotted”, dashdot”, or “-”, “–”, “:”, “-.”
                'edge_color': 'black',
                'edge_colors': self.edge_colors_dict(),
                'edge_labels': True,
                'edge_thickness': 1 + 5 // (len(self.gui.edges) ),
                'iterations': 250,
                'tree_orientation': 'down',
                'heights': None,
                'graph_border': False,
                'talk': False,
                'color_by_label': False,
                'partition': None,
                'dist': .150,
                'max_dist': 3,
                'loop_size': 0.300,
                'edge_labels_background': 'transparent', #    'transparent' o color 'white'
                'figsize': ((len(self.gui.nodes) + math.floor(sqrt(len(self.gui.edges)))) // 4 + 2, (len(self.gui.nodes) + math.floor(sqrt(len(self.gui.edges))) ) // 4 + 2),
                'save_pos': True,
                'pos': self.pos_dict()}
            """

            self.P = self.G.plot(**self.options)
            self.positions = self.G.get_pos()

            def options(edges_list_unformated):
                options = {
                    'title': self.gui.title.get_title_text(),
                    'vertex_size': 350,
                    'vertex_labels': self.vertex_label_dict(),
                    'vertex_color': '#dce775',
                    'vertex_colors': self.vertex_colors_dict(),
                    'edge_color': 'black',
                    'edge_colors': self.edge_colors_dict(edges_list_unformated),
                    'edge_labels': True,
                    'edge_thickness': 2,
                    'graph_border': False,
                    'talk': False,
                    'color_by_label': False,
                    'partition': None,
                    'edge_labels_background': 'transparent' if self.gui.has_multiedges() else 'white'}  # 'transparent' o color 'white'
                return options

            self.P = DiGraph(self.dashed_edges, loops=True, multiedges=self.gui.has_multiedges()).plot(
                pos=self.positions, edge_style="dashed", **options(self.dashed_edges)) \
                     + DiGraph(self.dotted_edges, loops=True, multiedges=self.gui.has_multiedges()).plot(
                pos=self.positions, edge_style="dotted", **options(self.dotted_edges)) \
                     + DiGraph(self.dashdot_edges, loops=True, multiedges=self.gui.has_multiedges()).plot(
                pos=self.positions, edge_style="dashdot", **options(self.dashdot_edges)) \
                     + DiGraph(self.solid_edges, loops=True, multiedges=self.gui.has_multiedges()).plot(
                pos=self.positions, edge_style="solid", axes=False, **options(self.solid_edges))
        else:
            self.G = Graph({node.index : [] for node in self.gui.nodes}, loops = True, multiedges = self.gui.has_multiedges())
            self.crear_edges(self.G)

            self.all_edge_types = self.solid_edges + self.dashed_edges + self.dotted_edges + self.dashdot_edges
            if self.gui.layout_option.get() != "none":
                self.options = {
                    'title': self.gui.title.get_title_text(),
                    'vertex_size': 350,
                    'vertex_labels': self.vertex_label_dict(),
                    'vertex_color': '#dce775',
                    'vertex_colors': self.vertex_colors_dict(),
                    'layout': self.gui.layout_option.get(),
                    'edge_color': 'black',
                    'edge_labels': True,
                    'edge_thickness': 2,
                    'iterations': 100000,
                    'tree_orientation': 'down',
                    'heights': None,
                    'graph_border': False,
                    'talk': False,
                    'color_by_label': False,
                    'partition': None,
                    'edge_labels_background': 'transparent' if self.gui.has_multiedges() else 'white',  # 'transparent' o color 'white'
                    'save_pos': True,
                    'pos': self.pos_dict()}
            else:
                self.options = {
                    'title': self.gui.title.get_title_text(),
                    'vertex_size': 350,
                    'vertex_labels': self.vertex_label_dict(),
                    'vertex_color': '#dce775',
                    'vertex_colors': self.vertex_colors_dict(),
                    'edge_color': 'black',
                    'edge_labels': True,
                    'edge_thickness': 2,
                    'iterations': 100000,
                    'tree_orientation': 'down',
                    'heights': None,
                    'graph_border': False,
                    'talk': False,
                    'color_by_label': False,
                    'partition': None,
                    'edge_labels_background': 'transparent' if self.gui.has_multiedges() else 'white',  # 'transparent' o color 'white'
                    'save_pos': True,
                    'pos': self.pos_dict()}

            """
            self.options = {
                'title': self.gui.title.get_title_text(),
                'vertex_size': 200+ round(130*(len(self.gui.nodes) // 6 )), # *(len(self.gui.nodes) // 5 + 1) es un factor de crecimiento lineal segun la cantidad de nodos en el grafo
                'vertex_labels': self.vertex_label_dict(),
                'vertex_color': '#dce775',
                'vertex_colors': self.vertex_colors_dict(),
                'layout': self.gui.layout_option.get(),
                'edge_style': 'solid', #“solid”, “dashed”, “dotted”, dashdot”, or “-”, “–”, “:”, “-.”
                'edge_color': 'black',
                'edge_colors': self.edge_colors_dict(),
                'edge_labels': True,
                'edge_thickness': 1 + 5 // (len(self.gui.edges) ),
                'iterations': 250,
                'tree_orientation': 'down',
                'heights': None,
                'graph_border': False,
                'talk': False,
                'color_by_label': False,
                'partition': None,
                'dist': .150,
                'max_dist': 3,
                'loop_size': 0.300,
                'edge_labels_background': 'transparent', #    'transparent' o color 'white'
                'figsize': ((len(self.gui.nodes) + math.floor(sqrt(len(self.gui.edges)))) // 4 + 2, (len(self.gui.nodes) + math.floor(sqrt(len(self.gui.edges))) ) // 4 + 2),
                'save_pos': True,
                'pos': self.pos_dict()}
            """

            self.P = self.G.plot(**self.options)
            self.positions = self.G.get_pos()

            def options(edges_list_unformated):
                options = {
                    'title': self.gui.title.get_title_text(),
                    'vertex_size': 350,
                    'vertex_labels': self.vertex_label_dict(),
                    'vertex_color': '#dce775',
                    'vertex_colors': self.vertex_colors_dict(),
                    'edge_color': 'black',
                    'edge_colors': self.edge_colors_dict(edges_list_unformated),
                    'edge_labels': True,
                    'edge_thickness': 2,
                    'graph_border': False,
                    'talk': False,
                    'color_by_label': False,
                    'partition': None,
                    'edge_labels_background': 'transparent' if self.gui.has_multiedges() else 'white'}  # 'transparent' o color 'white'
                return options

            self.P = Graph(self.dashed_edges, loops=True, multiedges=self.gui.has_multiedges()).plot(
                pos=self.positions, edge_style="dashed", **options(self.dashed_edges)) \
                     + Graph(self.dotted_edges, loops=True, multiedges=self.gui.has_multiedges()).plot(
                pos=self.positions, edge_style="dotted", **options(self.dotted_edges)) \
                     + Graph(self.dashdot_edges, loops=True, multiedges=self.gui.has_multiedges()).plot(
                pos=self.positions, edge_style="dashdot", **options(self.dashdot_edges)) \
                     + Graph(self.solid_edges, loops=True, multiedges=self.gui.has_multiedges()).plot(
                pos=self.positions, edge_style="solid", axes=False, **options(self.solid_edges))


    def descargar(self):
        __clase = self.gui.num_clase.get()
        __path = os.path.join("Figuras", str(__clase))

        # este bloque encuentra cual es el primer nombre "Clase x" disponible
        __x = 1
        __Dibujo_path = os.path.join(__path, "Dibujo " + str(__x) + ".pdf")
        while os.path.exists(__Dibujo_path):
            __x = __x + 1
            __Dibujo_path = os.path.join(__path, "Dibujo " + str(__x) + ".pdf")

        # plot = G.plot() de mas arriba del jupyter
        self.path = __path
        self.num_dibujo = __x
        self.Dibujo_path = __Dibujo_path

        self.P.save(self.Dibujo_path)
        print(self.Dibujo_path)

    def latex(self):
        __clase = self.gui.num_clase.get()
        __path = os.path.join("Figuras", str(__clase))

        if None in [self.path, self.num_dibujo, self.Dibujo_path]:
            __x = 1
            __Dibujo_path = os.path.join(__path, "Latex " + str(__x) + ".txt")
            while os.path.exists(__Dibujo_path):
                __x = __x + 1
                __Dibujo_path = os.path.join(__path, "Latex " + str(__x) + ".txt")
        else:
            __Dibujo_path = os.path.join(self.path, "Dibujo " + str(self.num_dibujo) + " - Latex" + ".txt")

        latex_code = latex(self.G)
        latex_by_line = []
        line = []
        for w in latex_code:
            if w != '\n':
                line.append(w)
            else:
                latex_by_line.append("".join(line))
                line = []
        latex_by_line.append("".join(line))
        line = []

        with open(__Dibujo_path, "w") as file:
            for line in latex_by_line:
                file.write(line + "\n")

        print(__Dibujo_path)

    def pos_dict(self):
        return {node.index : [node.x,node.y] for node in self.gui.nodes}

    def vertex_colors_dict(self):
        lista_colores = ['#ffebee', '#ffcdd2', '#ef9a9a', '#e57373', '#ef5350', '#f44336', '#e53935', '#d32f2f', '#c62828', '#b71c1c',
         '#f44336', '#fce4ec', '#f8bbd0', '#f48fb1', '#f06292', '#ec407a', '#e91e63', '#d81b60', '#c2185b', '#ad1457',
         '#880e4f', '#e91e63', '#f3e5f5', '#e1bee7', '#ce93d8', '#ba68c8', '#ab47bc', '#9c27b0', '#8e24aa', '#7b1fa2',
         '#6a1b9a', '#4a148c', '#9c27b0', '#ede7f6', '#d1c4e9', '#b39ddb', '#9575cd', '#7e57c2', '#673ab7', '#5e35b1',
         '#512da8', '#4527a0', '#311b92', '#673ab7', '#e8eaf6', '#c5cae9', '#9fa8da', '#7986cb', '#5c6bc0', '#3f51b5',
         '#3949ab', '#303f9f', '#283593', '#1a237e', '#3f51b5', '#e3f2fd', '#bbdefb', '#90caf9', '#64b5f6', '#42a5f5',
         '#2196f3', '#1e88e5', '#1976d2', '#1565c0', '#0d47a1', '#2196f3', '#e1f5fe', '#b3e5fc', '#81d4fa', '#4fc3f7',
         '#29b6f6', '#03a9f4', '#039be5', '#0288d1', '#0277bd', '#01579b', '#03a9f4', '#e0f7fa', '#b2ebf2', '#80deea',
         '#4dd0e1', '#26c6da', '#00bcd4', '#00acc1', '#0097a7', '#00838f', '#006064', '#00bcd4', '#e0f2f1', '#b2dfdb',
         '#80cbc4', '#4db6ac', '#26a69a', '#009688', '#00897b', '#00796b', '#00695c', '#004d40', '#009688', '#e8f5e9',
         '#c8e6c9', '#a5d6a7', '#81c784', '#66bb6a', '#4caf50', '#43a047', '#388e3c', '#2e7d32', '#1b5e20', '#4caf50',
         '#f1f8e9', '#dcedc8', '#c5e1a5', '#aed581', '#9ccc65', '#8bc34a', '#7cb342', '#689f38', '#558b2f', '#33691e',
         '#8bc34a', '#f9fbe7', '#f0f4c3', '#e6ee9c', '#dce775', '#d4e157', '#cddc39', '#c0ca33', '#afb42b', '#9e9d24',
         '#827717', '#cddc39', '#fffde7', '#fff9c4', '#fff59d', '#fff176', '#ffee58', '#ffeb3b', '#fdd835', '#fbc02d',
         '#f9a825', '#f57f17', '#ffeb3b', '#fff8e1', '#ffecb3', '#ffe082', '#ffd54f', '#ffca28', '#ffc107', '#ffb300',
         '#ffa000', '#ff8f00', '#ff6f00', '#ffc107', '#fff3e0', '#ffe0b2', '#ffcc80', '#ffb74d', '#ffa726', '#ff9800',
         '#fb8c00', '#f57c00', '#ef6c00', '#e65100', '#ff9800', '#fbe9e7', '#ffccbc', '#ffab91', '#ff8a65', '#ff7043',
         '#ff5722', '#f4511e', '#e64a19', '#d84315', '#bf360c', '#ff5722', '#efebe9', '#d7ccc8', '#bcaaa4', '#a1887f',
         '#8d6e63', '#795548', '#6d4c41', '#5d4037', '#4e342e', '#3e2723', '#795548', '#fafafa', '#f5f5f5', '#eeeeee',
         '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161', '#424242', '#212121', '#9e9e9e', '#eceff1', '#cfd8dc',
         '#b0bec5', '#90a4ae', '#78909c', '#607d8b', '#546e7a', '#455a64', '#37474f', '#263238', '#607d8b', '#ffffff',
         '#000000']

        return {color: [node.index for node in self.gui.nodes if node.color == color] for color in lista_colores}

    def edge_colors_dict(self, list_edges_unformated):
        def transform_to_EdgeObject(e):
            for edge in self.gui.edges:
                if edge.node1.index == e[0] and edge.node2.index == e[1]:
                    return edge
        list_edges = list(map(transform_to_EdgeObject,list_edges_unformated))
        lista_colores = ['#ffebee', '#ffcdd2', '#ef9a9a', '#e57373', '#ef5350', '#f44336', '#e53935', '#d32f2f',
                         '#c62828', '#b71c1c',
                         '#f44336', '#fce4ec', '#f8bbd0', '#f48fb1', '#f06292', '#ec407a', '#e91e63', '#d81b60',
                         '#c2185b', '#ad1457',
                         '#880e4f', '#e91e63', '#f3e5f5', '#e1bee7', '#ce93d8', '#ba68c8', '#ab47bc', '#9c27b0',
                         '#8e24aa', '#7b1fa2',
                         '#6a1b9a', '#4a148c', '#9c27b0', '#ede7f6', '#d1c4e9', '#b39ddb', '#9575cd', '#7e57c2',
                         '#673ab7', '#5e35b1',
                         '#512da8', '#4527a0', '#311b92', '#673ab7', '#e8eaf6', '#c5cae9', '#9fa8da', '#7986cb',
                         '#5c6bc0', '#3f51b5',
                         '#3949ab', '#303f9f', '#283593', '#1a237e', '#3f51b5', '#e3f2fd', '#bbdefb', '#90caf9',
                         '#64b5f6', '#42a5f5',
                         '#2196f3', '#1e88e5', '#1976d2', '#1565c0', '#0d47a1', '#2196f3', '#e1f5fe', '#b3e5fc',
                         '#81d4fa', '#4fc3f7',
                         '#29b6f6', '#03a9f4', '#039be5', '#0288d1', '#0277bd', '#01579b', '#03a9f4', '#e0f7fa',
                         '#b2ebf2', '#80deea',
                         '#4dd0e1', '#26c6da', '#00bcd4', '#00acc1', '#0097a7', '#00838f', '#006064', '#00bcd4',
                         '#e0f2f1', '#b2dfdb',
                         '#80cbc4', '#4db6ac', '#26a69a', '#009688', '#00897b', '#00796b', '#00695c', '#004d40',
                         '#009688', '#e8f5e9',
                         '#c8e6c9', '#a5d6a7', '#81c784', '#66bb6a', '#4caf50', '#43a047', '#388e3c', '#2e7d32',
                         '#1b5e20', '#4caf50',
                         '#f1f8e9', '#dcedc8', '#c5e1a5', '#aed581', '#9ccc65', '#8bc34a', '#7cb342', '#689f38',
                         '#558b2f', '#33691e',
                         '#8bc34a', '#f9fbe7', '#f0f4c3', '#e6ee9c', '#dce775', '#d4e157', '#cddc39', '#c0ca33',
                         '#afb42b', '#9e9d24',
                         '#827717', '#cddc39', '#fffde7', '#fff9c4', '#fff59d', '#fff176', '#ffee58', '#ffeb3b',
                         '#fdd835', '#fbc02d',
                         '#f9a825', '#f57f17', '#ffeb3b', '#fff8e1', '#ffecb3', '#ffe082', '#ffd54f', '#ffca28',
                         '#ffc107', '#ffb300',
                         '#ffa000', '#ff8f00', '#ff6f00', '#ffc107', '#fff3e0', '#ffe0b2', '#ffcc80', '#ffb74d',
                         '#ffa726', '#ff9800',
                         '#fb8c00', '#f57c00', '#ef6c00', '#e65100', '#ff9800', '#fbe9e7', '#ffccbc', '#ffab91',
                         '#ff8a65', '#ff7043',
                         '#ff5722', '#f4511e', '#e64a19', '#d84315', '#bf360c', '#ff5722', '#efebe9', '#d7ccc8',
                         '#bcaaa4', '#a1887f',
                         '#8d6e63', '#795548', '#6d4c41', '#5d4037', '#4e342e', '#3e2723', '#795548', '#fafafa',
                         '#f5f5f5', '#eeeeee',
                         '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161', '#424242', '#212121', '#9e9e9e',
                         '#eceff1', '#cfd8dc',
                         '#b0bec5', '#90a4ae', '#78909c', '#607d8b', '#546e7a', '#455a64', '#37474f', '#263238',
                         '#607d8b', '#ffffff',
                         '#000000']

        return {color: [edge.get_node_index() for edge in list_edges if edge.color == color] for color in lista_colores}

    def crear_edges(self, G):
        for parent in self.gui.founding_parents_list():
            if parent.is_loop == False:
                tree = parent.family_tree()  # falta agregar los edges extra
                for edge in tree:
                    G.add_edge(edge.node1.index, edge.node2.index, label=edge.label)
                    self.clasify_edge_style(edge)

        for parent in self.gui.founding_parents_list():
            if parent.is_loop == True:
                tree = parent.family_tree()  # falta agregar los loops
                for edge in tree:
                    G.add_edge(edge.node1.index, edge.node2.index, label=edge.label)
                    self.clasify_edge_style(edge)
    def clasify_edge_style(self,edge):
        if edge.style == "solid":
            self.solid_edges.append((edge.node1.index, edge.node2.index, edge.label))
        elif edge.style == "dashed":
            self.dashed_edges.append((edge.node1.index, edge.node2.index, edge.label))
        elif edge.style == "dotted":
            self.dotted_edges.append((edge.node1.index, edge.node2.index, edge.label))
        elif edge.style == "dashdot":
            self.dashdot_edges.append((edge.node1.index, edge.node2.index, edge.label))
    def vertex_label_dict(self):
        return {node.index : node.label for node in self.gui.nodes}

    def hamiltonian_cycle(self):
        self.G.hamiltonian_cycle()
        print("Con una cantidad de longitud:", len(self.G.hamiltonian_cycle()))


"""
 class Impresion_multigrafo(Impresion):
    def __init__(self, gui):
        self.gui = gui
        self.canvas = self.gui.canvas
        self.figsize = self.gui.figsize

        self.options = {
            'title': self.gui.title.get_title_text(),
            'vertex_size': 200 + round(130 * (len(self.gui.nodes) // 6)),
            # *(len(self.gui.nodes) // 5 + 1) es un factor de crecimiento lineal segun la cantidad de nodos en el grafo
            'vertex_labels': self.vertex_label_dict(),
            'vertex_color': '#dce775',
            'vertex_colors': self.vertex_colors_dict(),
            'layout': self.gui.layout_option.get(),
            'edge_style': 'solid',  # “solid”, “dashed”, “dotted”, dashdot”, or “-”, “–”, “:”, “-.”
            'edge_color': 'black',
            'edge_labels': True,
            'edge_thickness': 1 + 5 // (len(self.gui.edges)),
            'iterations': 250,
            'tree_orientation': 'down',
            'heights': None,
            'graph_border': False,
            'talk': False,
            'color_by_label': False,
            'partition': None,
            'dist': .150,
            'max_dist': 3,
            'loop_size': .100,
            'edge_labels_background': 'transparent',  # 'transparent' o color 'white'
            'figsize': ((len(self.gui.nodes) + math.floor(sqrt(len(self.gui.edges)))) // 4 + 2,
                        (len(self.gui.nodes) + math.floor(sqrt(len(self.gui.edges)))) // 4 + 2),
            'save_pos': True,
            'pos': self.pos_dict()}


        self.G = nx.DiGraph(multiedges = self.gui.has_multiedges())

        self.add_nodes(self.G)
        self.etiquetar_edges(self.G)
        pos = nx.spring_layout(self.G)
        edge_colors = nx.get_edge_attributes(self.G, 'color').values()
        node_colors = nx.get_node_attributes(self.G, 'color').values()
        edge_labels = nx.get_edge_attributes(self.G, 'label')

        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, font_color='red')

        if self.gui.agregar_flechas_bool.get() == True:
            arrowstyle = "-|>"
        else:
            arrowstyle = "-"
        nx.draw(self.G, pos, edge_color=edge_colors, with_labels=True,
            labels=self.vertex_label_dict(), font_weight='bold',
            linewidths=3, node_color=node_colors, connectionstyle='arc3, rad = 0.1', arrowstyle = arrowstyle, arrows = self.gui.agregar_flechas_bool.get()
                                                                                              or self.gui.has_multiedges(),) #tengo que agregar or has multiedges porque si no no dibuja los multiedges aunque no haya flechas. creoq ue est abuggeado...


        # self.P.show() -> no hace falta para poder descargar

    def descargar(self):
        __clase = self.gui.num_clase.get()
        __path = os.path.join("Figuras", str(__clase))

        # este bloque encuentra cual es el primer nombre "Clase x" disponible
        __x = 1
        __Dibujo_path = os.path.join(__path, "Dibujo " + str(__x) + ".pdf")
        while os.path.exists(__Dibujo_path):
            __x = __x + 1
            __Dibujo_path = os.path.join(__path, "Dibujo " + str(__x) + ".pdf")

        # plot = G.plot() de mas arriba del jupyter
        plt.savefig(__Dibujo_path)
        #plt.show()
        self.G.clear()
        plt.close()
        print(__Dibujo_path)

    def edge_colors_dict(self):
        lista_colores = ['#ffebee', '#ffcdd2', '#ef9a9a', '#e57373', '#ef5350', '#f44336', '#e53935', '#d32f2f',
                         '#c62828', '#b71c1c',
                         '#f44336', '#fce4ec', '#f8bbd0', '#f48fb1', '#f06292', '#ec407a', '#e91e63', '#d81b60',
                         '#c2185b', '#ad1457',
                         '#880e4f', '#e91e63', '#f3e5f5', '#e1bee7', '#ce93d8', '#ba68c8', '#ab47bc', '#9c27b0',
                         '#8e24aa', '#7b1fa2',
                         '#6a1b9a', '#4a148c', '#9c27b0', '#ede7f6', '#d1c4e9', '#b39ddb', '#9575cd', '#7e57c2',
                         '#673ab7', '#5e35b1',
                         '#512da8', '#4527a0', '#311b92', '#673ab7', '#e8eaf6', '#c5cae9', '#9fa8da', '#7986cb',
                         '#5c6bc0', '#3f51b5',
                         '#3949ab', '#303f9f', '#283593', '#1a237e', '#3f51b5', '#e3f2fd', '#bbdefb', '#90caf9',
                         '#64b5f6', '#42a5f5',
                         '#2196f3', '#1e88e5', '#1976d2', '#1565c0', '#0d47a1', '#2196f3', '#e1f5fe', '#b3e5fc',
                         '#81d4fa', '#4fc3f7',
                         '#29b6f6', '#03a9f4', '#039be5', '#0288d1', '#0277bd', '#01579b', '#03a9f4', '#e0f7fa',
                         '#b2ebf2', '#80deea',
                         '#4dd0e1', '#26c6da', '#00bcd4', '#00acc1', '#0097a7', '#00838f', '#006064', '#00bcd4',
                         '#e0f2f1', '#b2dfdb',
                         '#80cbc4', '#4db6ac', '#26a69a', '#009688', '#00897b', '#00796b', '#00695c', '#004d40',
                         '#009688', '#e8f5e9',
                         '#c8e6c9', '#a5d6a7', '#81c784', '#66bb6a', '#4caf50', '#43a047', '#388e3c', '#2e7d32',
                         '#1b5e20', '#4caf50',
                         '#f1f8e9', '#dcedc8', '#c5e1a5', '#aed581', '#9ccc65', '#8bc34a', '#7cb342', '#689f38',
                         '#558b2f', '#33691e',
                         '#8bc34a', '#f9fbe7', '#f0f4c3', '#e6ee9c', '#dce775', '#d4e157', '#cddc39', '#c0ca33',
                         '#afb42b', '#9e9d24',
                         '#827717', '#cddc39', '#fffde7', '#fff9c4', '#fff59d', '#fff176', '#ffee58', '#ffeb3b',
                         '#fdd835', '#fbc02d',
                         '#f9a825', '#f57f17', '#ffeb3b', '#fff8e1', '#ffecb3', '#ffe082', '#ffd54f', '#ffca28',
                         '#ffc107', '#ffb300',
                         '#ffa000', '#ff8f00', '#ff6f00', '#ffc107', '#fff3e0', '#ffe0b2', '#ffcc80', '#ffb74d',
                         '#ffa726', '#ff9800',
                         '#fb8c00', '#f57c00', '#ef6c00', '#e65100', '#ff9800', '#fbe9e7', '#ffccbc', '#ffab91',
                         '#ff8a65', '#ff7043',
                         '#ff5722', '#f4511e', '#e64a19', '#d84315', '#bf360c', '#ff5722', '#efebe9', '#d7ccc8',
                         '#bcaaa4', '#a1887f',
                         '#8d6e63', '#795548', '#6d4c41', '#5d4037', '#4e342e', '#3e2723', '#795548', '#fafafa',
                         '#f5f5f5', '#eeeeee',
                         '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161', '#424242', '#212121', '#9e9e9e',
                         '#eceff1', '#cfd8dc',
                         '#b0bec5', '#90a4ae', '#78909c', '#607d8b', '#546e7a', '#455a64', '#37474f', '#263238',
                         '#607d8b', '#ffffff',
                         '#000000']

        return {color: [edge.get_node_index() for edge in self.gui.edges if
                        edge.color == color and edge.is_founding_parent()] for color in lista_colores}

    def add_nodes(self,G):
        for node in self.gui.nodes:
            G.add_node(node.index,color = node.color, label = node.label, pos = (node.x,node.y))

    def etiquetar_edges(self, G):
        for parent in self.gui.founding_parents_list():
            if parent.is_loop == False:
                tree = parent.family_tree()  # falta agregar los edges extra
                for edge in tree:
                    G.add_edge(edge.node1.index, edge.node2.index, label=edge.label, color=edge.color, weight = edge.weight, dir = "forward", arrowsize = 3)


        for parent in self.gui.founding_parents_list():
            if parent.is_loop == True:
                tree = parent.family_tree()
                for loop in tree: # faltan agregar todos los loops
                    G.add_edge(loop.node1.index, loop.node2.index, xlabel=loop.label, color=loop.color, weight = loop.weight, dir = "forward", arrowsize = 3)
"""




class Node:
    def __init__(self, x, y,gui, color='#dce775', outline = "black", width = 2): #el color "#dce775" es verde manzana claro
        self.gui = gui
        self.canvas = self.gui.canvas

        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.outline = outline

        self.index = len(self.gui.nodes)
        self.label = str(self.index)
        self.edges = []

        self.canvas_id = None
        self.canvas_text_id = None

        self.draw()

        self.gui.nodes.append(self)

    def draw(self):
        self.canvas_id = self.canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill=self.color,
                                                 outline=self.outline, width = self.width, tags = "node")
        self.canvas_text_id = self.canvas.create_text(self.x, self.y, text=self.label, font=("Arial", 10), tags = "node_text")

    def delete(self):
        if self == self.gui.selected_node:
            self.gui.selected_node = None

        self.canvas.delete(self.canvas_id)
        self.canvas.delete(self.canvas_text_id)
        for edge in reversed(self.edges):
            edge.delete()
        if self in self.gui.nodes:
            self.gui.nodes.remove(self)
        self.gui.num_nodes = len(self.gui.nodes)

        for node in self.gui.nodes:
            if node.index > self.index:
                node.index = node.index - 1

        del self

    def neighbours(self):
        L = []
        for edge in self.edges:
            if edge.is_loop == False:
                if self == edge.node1:
                    L.append(edge.node2)
                else:
                    L.append(edge.node1)
            else:
                L.append(self)

        return list(set(L))

    def redraw(self):
        self.canvas.delete(self.canvas_id)
        self.canvas_id = self.canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20,
                                                 fill=self.color, outline=self.outline, width = self.width,tags = "node")

        self.canvas.delete(self.canvas_text_id)
        self.canvas_text_id = self.canvas.create_text(self.x, self.y, text=self.label, font=("Arial", 10), tags = "node_text")


        for edge in self.edges:
            edge.redraw()

    def edit_label(self):
        old_label = self.label
        self.canvas.delete(self.canvas_text_id)

        entry = tk.Entry(self.canvas, width=20)
        entry.place(x=self.x, y=self.y)

        # focus the entry widget
        entry.focus_set()

        def save_label(event):
            new_label = entry.get()
            self.label = new_label
            self.canvas_text_id = self.canvas.create_text(self.x, self.y, text=self.label, font=("Arial", 10), tags = "node_text")

            entry.destroy()
        # bind the Return key to the entry widget to save the new label and remove the entry widget
        entry.bind("<Return>", save_label)
        entry.bind("<FocusOut>", save_label)

        def escape_label(event):
            self.label = old_label
            self.canvas_text_id = self.canvas.create_text(self.x, self.y, text=self.label, font=("Arial", 10))

            entry.destroy()
        entry.bind("<Escape>", escape_label)

    def connect_node(self,node2):
        lista_edges_compatibles = list(filter(lambda e: e.nodes == {self,node2},self.gui.edges))
        if len(lista_edges_compatibles) == 0:
            Edge(self,node2,self.gui)
        elif len(lista_edges_compatibles) == 1:
            edge = lista_edges_compatibles[0]
            if self == edge.node2 and node2 == edge.node1:
                edge.create_next_edge(self, node2)

    def create_loop(self):
        if not any(filter(lambda e: e.nodes == {self}, self.gui.edges)):
            Loop(self, self.gui)
    def clear_label(self):
        self.canvas.delete(self.canvas_text_id)
        self.label = ""
        self.canvas_text_id = self.canvas.create_text(self.x, self.y, text=self.label, font=("Arial", 10),
                                                      tags="node_text")


class Edge:
    def __init__(self, node1, node2, gui, parent = None,child = None, color="black", width= 5, fill = '#29b6f6', weight = 3):
        self.is_loop = False

        self.style = gui.edge_style_option.get() #puedo elegir entre solid, dashed, dotted, dashdot
        self.dash = ""
        if self.style == "dashed":
            self.dash = "_"
        elif self.style == "dotted":
            self.dash = "."
        elif self.style == "dashdot":
            self.dash = "-."

        self.weight = weight

        self.font = font.Font(family="nimbus sans l", size=15, weight="bold")

        self.gui = gui
        self.canvas = gui.canvas

        self.fill = fill

        self.parent = parent
        if self.parent is not None:
            self.parent.child = self

        self.child = child

        self.node1 = node1
        self.node2 = node2

        self.nodes = {self.node1, self.node2}

        self.color = color
        self.width = width

        self.middle_point = None
        self.create_middle_points()
        self.x,self.y = self.middle_point[0],self.middle_point[1]
        self.label = ""

        self.canvas_id = None
        self.canvas_text_id = None
        self.hitbox_id = None

        self.arrow = None
        self.update_arrow()

        self.draw()

        self.node1.edges.append(self), self.node2.edges.append(self)
        self.gui.edges.append(self)

    def update_arrow(self):
        if self.gui.agregar_flechas_bool.get() == True:
            self.arrow = "last"
        else:
            self.arrow = None
    def get_node_index(self):
        return [self.node1.index, self.node2.index]

    def on_mouse_enter(self,event):
        pass

    def draw(self):
        x1, y1 = self.node1.x, self.node1.y
        x2, y2 = self.node2.x, self.node2.y

        r = 20
        lamb = r/math.sqrt((x2-x1)**2+(y2-y1)**2)
        x3,y3 = x2-(x2-x1)*lamb, y2-(y2-y1)*lamb

        self.create_middle_points()

        x = self.x = self.middle_point[0]
        y = self.y = self.middle_point[1]

        x0 = (self.node1.x + self.node2.x)/2
        y0 = (self.node1.y + self.node2.y)/2

        self.canvas_id = self.canvas.create_line((x1, y1), (x, y), (x3, y3), fill = self.color, dash = self.dash,
                                                 width = self.width, tags = "line", smooth=True, splinesteps=12, arrow = self.arrow, arrowshape = (25,30,10))
        self.canvas_text_id = self.canvas.create_text( (x-x0)/2 + x0, (y-y0)/2 + y0, text=self.label, font = self.font, tags = "line_text", fill = self.fill)
        self.hitbox_id = self.canvas.create_line((x1, y1), (x, y), (x2, y2), fill="", width=10, tags = "line_hitbox",  smooth=True, splinesteps=12)

        self.canvas.tag_lower(self.canvas_text_id)
        self.canvas.tag_lower(self.canvas_id)
        self.canvas.tag_lower(self.hitbox_id)

    def redraw(self):
        self.canvas.delete(self.canvas_id)
        self.canvas.delete(self.canvas_text_id)
        self.canvas.delete(self.hitbox_id)

        x1, y1 = self.node1.x, self.node1.y
        x2, y2 = self.node2.x, self.node2.y

        r = 20
        lamb = r / math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        x3, y3 = x2 - (x2 - x1) * lamb, y2 - (y2 - y1) * lamb

        self.create_middle_points()

        x = self.x = self.middle_point[0]
        y = self.y = self.middle_point[1]

        x0 = (self.node1.x + self.node2.x) / 2
        y0 = (self.node1.y + self.node2.y) / 2

        self.canvas_id = self.canvas.create_line((x1, y1), (x, y), (x3, y3), fill = self.color, dash = self.dash,
                                                 width = self.width, tags = "line", smooth=True, splinesteps=12,arrow = self.arrow, arrowshape = (25,30,10))
        self.canvas_text_id = self.canvas.create_text((x-x0)/2 + x0, (y - y0)/2 + y0, text=self.label, font = self.font, tags = "line_text", fill = self.fill)
        self.hitbox_id = self.canvas.create_line((x1, y1), (x, y), (x2, y2), fill="", width=10, tags = "line_hitbox",  smooth=True, splinesteps=12)

        self.canvas.tag_lower(self.canvas_text_id)
        self.canvas.tag_lower(self.canvas_id)
        self.canvas.tag_lower(self.hitbox_id)


    def redraw_all(self):
        list = self.next_generations()
        list.append(self)
        for edge in reversed(list):
            edge.redraw()

    def delete(self):
        n1, n2 = self.node1, self.node2

        if self in n1.edges:
            n1.edges.remove(self)
        if self in n2.edges:
            n2.edges.remove(self)

        self.canvas.delete(self.canvas_id)
        self.canvas.delete(self.canvas_text_id)
        self.canvas.delete(self.hitbox_id)
        if self in self.gui.edges:
            self.gui.edges.remove(self)

        if self.parent is not None:
            if self.child is None:
                self.parent.child = None

                self.parent.redraw()
            else:
                self.parent.child = self.child
                self.child.parent = self.parent

                self.child.redraw_all()
        else:
            if self.child is not None:
                self.child.parent = None

                self.child.redraw_all()

        del self
    def edit_label(self):
        old_label = self.label
        self.canvas.delete(self.canvas_text_id)

        x0 = (self.node1.x + self.node2.x) / 2
        y0 = (self.node1.y + self.node2.y) / 2

        entry = tk.Entry(self.canvas, width=20)
        entry.place(x=(self.x - x0)/2 + x0, y= (self.y - y0)/2 + y0)

        # focus the entry widget
        entry.focus_set()

        def save_label(event):
            new_label = entry.get()
            self.label = new_label

            x0 = (self.node1.x + self.node2.x) / 2
            y0 = (self.node1.y + self.node2.y) / 2

            self.canvas_text_id = self.canvas.create_text((self.x-x0)/2 + x0, (self.y-y0)/2 + y0, text=self.label, font=self.font, tags = "line_text", fill = self.fill)

            entry.destroy()
        # bind the Return key to the entry widget to save the new label and remove the entry widget
        entry.bind("<Return>", save_label)
        entry.bind("<FocusOut>", save_label)

        def escape_label(event):
            self.label = old_label
            self.canvas_text_id = self.canvas.create_text((self.x - x0)/2 + x0, (self.y - y0)/2 + y0, text=self.label, font=self.font, tags = "line_text", fill = self.fill)

            entry.destroy()
        entry.bind("<Escape>", escape_label)


    def equals(self, edge):
        if (self.node1 == edge.node1 and self.node2 == edge.node2) or (
                self.node1 == edge.node2 and self.node2 == edge.node1):
            return True
        else:
            return False

    def create_next_edge(self,node1,node2):
        if self.child is None:
            Edge(node1, node2,self.gui, parent = self) #cambiamos la variable self.child tendro del __init__ de Edge

    def has_child(self):
        if self.child is not None:
            return True
        else:
            return False

    def is_founding_parent(self):
        if self == self.founding_parent():
            return True
        else:
            return False

    def create_middle_points(self):
        def ortog_vect(v):
            x = v[0]
            y = v[1]
            norm = sqrt(x**2 + y**2)

            return (-y/norm, x/norm)
        def create_middle_points(xA,yA,xB,yB,n):
            middle_points = []
            xM0 = (xA + xB)/2
            yM0 = (yA + yB)/2
            middle_points.append((xM0, yM0))

            W = normal_vector_to_the_line_node1_node2 = ortog_vect(((self.node2.x - self.node1.x)/2, (self.node2.y-self.node1.y)/2))
            xW = W[0]
            yW = W[1]

            if n >= 1:
                for i in range(0,n):
                    if i % 2 == 1:
                        k = (i-1) // 2
                        lamb = sum([(1/1.5)**j for j in range(k+1)])

                    elif i %2 == 0:
                        k = i // 2
                        lamb = - sum([(1/1.5)**j for j in range(k+1)])

                    xM = 100*lamb * xW + xM0
                    yM = 100*lamb * yW + yM0

                    middle_points.append((xM,yM))

            return middle_points

        n = self.number_of_ancestors()
        tree = self.family_tree()

        xA, yA, xB, yB = (self.node1.x, self.node1.y, self.node2.x, self.node2.y)

        middle_points = create_middle_points(xA, yA, xB, yB,n)

        for i,M in enumerate(middle_points):
            x = M[0]
            y = M[1]
            member = tree[i]
            member.middle_point = (x,y)

            #member.canvas_id = self.canvas.create_line((xA, yA), (x, y), (xB, yB), smooth=True, splinesteps = 100)
            #self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5,
            #                        outline="black", fill="black", tags="token")

    def number_of_ancestors(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.number_of_ancestors()

    def founding_parent(self):
        if self.parent is None:
            return self
        else:
            return self.parent.founding_parent()
    def family_tree(self):
        founding_parent = self.founding_parent()
        def foo(member, list):
            list.append(member)
            if member.child is not None:
                return foo(member.child,list)
            else:
                return list

        tree = foo(founding_parent, [])
        return tree

    def next_generations(self):
        if self.child is None:
            return []
        else:
            list = self.child.next_generations()
            list.append(self.child)
            return list

    def clear_label(self):
        self.canvas.delete(self.canvas_text_id)
        self.label = ""

        x0 = (self.node1.x + self.node2.x) / 2
        y0 = (self.node1.y + self.node2.y) / 2
        self.canvas_text_id = self.canvas.create_text((self.x - x0) / 2 + x0, (self.y - y0) / 2 + y0, text=self.label,
                                                      font=self.font, tags="line_text", fill=self.fill)


class Loop():
    def __init__(self, node, gui, parent = None,child = None, color="gray", width= 5, fill = '#29b6f6', weight = 3):
        self.is_loop = True

        self.style = gui.edge_style_option.get() # puede ser solid, dashed, dotted o dashdot
        self.dash = ""
        if self.style == "dashed":
            self.dash = "_"
        elif self.style == "dotted":
            self.dash = "."
        elif self.style == "dashdot":
            self.dash = "-."

        self.weight = weight

        self.font = font.Font(family="nimbus sans l", size=15, weight="bold")

        self.gui = gui
        self.canvas = gui.canvas

        self.fill = fill

        self.parent = parent
        if self.parent is not None:
            self.parent.child = self

        self.child = child

        self.node1 = node
        self.node2 = node

        self.nodes = {self.node1, self.node2}

        self.color = color
        self.width = width

        self.middle_point = None
        self.create_middle_points()
        self.x,self.y = self.middle_point[0],self.middle_point[1]
        self.label = ""

        self.canvas_id = None
        self.canvas_text_id = None
        self.hitbox_id = None

        self.arrow = None
        self.update_arrow()

        self.draw()

        self.node1.edges.append(self)
        self.gui.edges.append(self)

    def update_arrow(self):
        if self.gui.agregar_flechas_bool.get() == True:
            self.arrow = "last"
        else:
            self.arrow = None
    def get_node_index(self):
        return [self.node1.index, self.node2.index]

    def on_mouse_enter(self,event):
        pass

    def draw(self):
        x1, y1 = self.node1.x, self.node1.y

        self.create_middle_points()

        x = self.x = self.middle_point[0]
        y = self.y = self.middle_point[1]

        x0 = (self.node1.x + self.node2.x)/2
        y0 = (self.node1.y + self.node2.y)/2

        r = 20
        theta = math.pi/8
        bar_theta = math.pi - math.pi/8
        x3,y3 = r*math.cos(theta) + x1 , r*math.sin(theta) + y1
        bar_x3, bar_y3 = r * math.cos(bar_theta) + x1, r * math.sin(bar_theta) + y1

        self.canvas_id = self.canvas.create_line((bar_x3, bar_y3), (x-120, y), (x+120,y), (x3,y3), fill = self.color, dash = self.dash,
                                                 width = self.width, tags = "line", smooth="raw", splinesteps=12, arrow = self.arrow, arrowshape = (25,30,10))
        self.canvas_text_id = self.canvas.create_text( (x-x0)/2 + x0, (y-y0)/2 + y0, text=self.label, font = self.font, tags = "line_text", fill = self.fill)
        self.hitbox_id = self.canvas.create_line((bar_x3, bar_y3), (x-120, y), (x+120,y), (x3,y3), fill="", width=10, tags = "line_hitbox",  smooth="raw", splinesteps=12)

        self.canvas.tag_lower(self.canvas_text_id)
        self.canvas.tag_lower(self.canvas_id)
        self.canvas.tag_lower(self.hitbox_id)

    def redraw(self):
        self.canvas.delete(self.canvas_id)
        self.canvas.delete(self.canvas_text_id)
        self.canvas.delete(self.hitbox_id)

        x1, y1 = self.node1.x, self.node1.y

        self.create_middle_points()

        x = self.x = self.middle_point[0]
        y = self.y = self.middle_point[1]

        x0 = (self.node1.x + self.node2.x) / 2
        y0 = (self.node1.y + self.node2.y) / 2

        r = 20
        theta = math.pi / 8
        bar_theta = math.pi - math.pi / 8
        x3, y3 = r * math.cos(theta) + x1, r * math.sin(theta) + y1
        bar_x3, bar_y3 = r * math.cos(bar_theta) + x1, r * math.sin(bar_theta) + y1

        self.canvas_id = self.canvas.create_line((bar_x3, bar_y3), (x-120, y), (x+120,y), (x3,y3), fill = self.color, dash = self.dash,
                                                 width = self.width, tags = "line", smooth="raw", splinesteps=12, arrow = self.arrow, arrowshape = (25,30,10))
        self.canvas_text_id = self.canvas.create_text((x-x0)/2 + x0, (y - y0)/2 + y0, text=self.label, font = self.font, tags = "line_text", fill = self.fill)
        self.hitbox_id = self.canvas.create_line((bar_x3, bar_y3), (x-120, y), (x+120,y), (x3,y3), fill="", width=10, tags = "line_hitbox",  smooth="raw", splinesteps=12)

        self.canvas.tag_lower(self.canvas_text_id)
        self.canvas.tag_lower(self.canvas_id)
        self.canvas.tag_lower(self.hitbox_id)

    def redraw_all(self):
        list = self.next_generations()
        list.append(self)
        for edge in reversed(list):
            edge.redraw()

    def delete(self):
        n1 = self.node1

        if self in n1.edges:
            n1.edges.remove(self)

        self.canvas.delete(self.canvas_id)
        self.canvas.delete(self.canvas_text_id)
        self.canvas.delete(self.hitbox_id)
        if self in self.gui.edges:
            self.gui.edges.remove(self)

        if self.parent is not None:
            if self.child is None:
                self.parent.child = None

                self.parent.redraw()
            else:
                self.parent.child = self.child
                self.child.parent = self.parent

                self.child.redraw_all()
        else:
            if self.child is not None:
                self.child.parent = None

                self.child.redraw_all()

        del self
    def edit_label(self):
        old_label = self.label
        self.canvas.delete(self.canvas_text_id)

        x0 = (self.node1.x + self.node2.x) / 2
        y0 = (self.node1.y + self.node2.y) / 2

        entry = tk.Entry(self.canvas, width=20)
        entry.place(x=(self.x - x0)/2 + x0, y= (self.y - y0)/2 + y0)

        # focus the entry widget
        entry.focus_set()

        def save_label(event):
            new_label = entry.get()
            self.label = new_label

            x0 = (self.node1.x + self.node2.x) / 2
            y0 = (self.node1.y + self.node2.y) / 2

            self.canvas_text_id = self.canvas.create_text((self.x-x0)/2 + x0, (self.y-y0)/2 + y0, text=self.label, font=self.font, tags = "line_text", fill = self.fill)

            entry.destroy()
        # bind the Return key to the entry widget to save the new label and remove the entry widget
        entry.bind("<Return>", save_label)
        entry.bind("<FocusOut>", save_label)

        def escape_label(event):
            self.label = old_label
            self.canvas_text_id = self.canvas.create_text((self.x - x0)/2 + x0, (self.y - y0)/2 + y0, text=self.label, font=self.font, tags = "line_text", fill = self.fill)

            entry.destroy()
        entry.bind("<Escape>", escape_label)

    def equals(self, edge):
        if (self.node1 == edge.node1 and self.node2 == edge.node2) or (
                self.node1 == edge.node2 and self.node2 == edge.node1):
            return True
        else:
            return False

    def create_next_edge(self):
        if self.child is None:
            Loop(self.node1,self.gui, parent = self) #cambiamos la variable self.child tendro del __init__ de Edge

    def has_child(self):
        if self.child is not None:
            return True
        else:
            return False
    def create_middle_points(self):
        def ortog_vect(v):
            x = v[0]
            y = v[1]
            norm = sqrt(x**2 + y**2)

            return (-y/norm, x/norm)
        def create_middle_points(xA,yA,n):
            middle_points = []
            xM0 = xA
            yM0 = yA + 120
            middle_points.append((xM0, yM0))

            for i in range(0,n):
                if i % 2 == 1:
                    k = (i-1) // 2
                    t = sum([(1/1.5)**j for j in range(k+1)])

                    xM = xM0
                    yM = 90 * t + yM0

                elif i %2 == 0:
                    k = i // 2
                    t = - sum([(1/1.5)**j for j in range(k+1)])

                    xM = xM0
                    yM = 90 * t + yM0 - 120

                middle_points.append((xM,yM))

            return middle_points

        n = self.number_of_ancestors()
        tree = self.family_tree()

        xA, yA = (self.node1.x, self.node1.y)

        middle_points = create_middle_points(xA, yA,n)

        for i,M in enumerate(middle_points):
            x = M[0]
            y = M[1]
            member = tree[i]
            member.middle_point = (x,y)

            #member.canvas_id = self.canvas.create_line((xA, yA), (x, y), (xB, yB), smooth=True, splinesteps = 100)
            #self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5,
            #                        outline="black", fill="black", tags="token")

    def number_of_ancestors(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.number_of_ancestors()

    def founding_parent(self):
        if self.parent is None:
            return self
        else:
            return self.parent.founding_parent()

    def is_founding_parent(self):
        if self == self.founding_parent():
            return True
        else:
            return False
    def family_tree(self):
        founding_parent = self.founding_parent()
        def foo(member, list):
            list.append(member)
            if member.child is not None:
                return foo(member.child,list)
            else:
                return list

        tree = foo(founding_parent, [])
        return tree

    def next_generations(self):
        if self.child is None:
            return []
        else:
            list = self.child.next_generations()
            list.append(self.child)
            return list

    def clear_label(self):
        self.canvas.delete(self.canvas_text_id)
        self.label = ""

        x0 = (self.node1.x + self.node2.x) / 2
        y0 = (self.node1.y + self.node2.y) / 2
        self.canvas_text_id = self.canvas.create_text((self.x - x0) / 2 + x0, (self.y - y0) / 2 + y0, text=self.label,
                                                      font=self.font, tags="line_text", fill=self.fill)


class GraphGUI:
    def __init__(self, width, height):
        self.impresion = None

        self.width = width
        self.height = height

        self.color = None
        self.figsize = 3

        self.nodes = []
        self.num_nodes = 0
        self.edges = []

        ########################
        @property
        def selected_node(self):
            return self.selected_node
        @selected_node.setter
        def selected_node(self, value):
            self.selected_node = value
        self.selected_node = None
        ########################
        @property
        def dragged_node(self):
            return self.dragged_node
        @dragged_node.setter
        def dragged_node(self, value):
            self.dragged_node = value
        self.dragged_node = None
        ########################

        @property
        def dragged_edge(self):
            return self.dragged_edge

        @dragged_edge.setter
        def dragged_edge(self, value):
            self.dragged_edge = value

        self.dragged_edge = None
        ########################

        self.mouse_x = 0
        self.mouse_y = 0
        self.draggingRightclick = False

        self.modo = "dibujar"
        # modos: "dibujar", "pintar", "borrar", "configurar", "fisicas"

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Graph GUI")

        # Create option list
        self.option_list = ["Clase " + str(i) for i in range(1, 21)]
        # create a StringVar to store the selected item
        self.num_clase = tk.StringVar(self.root)
        # set the initial value of the option menu
        self.num_clase.set("Clase 1")
        # create the option menu with the list of items and the StringVar
        clase_option_menu = tk.OptionMenu(self.root, self.num_clase, *self.option_list)
        # pack the option menu to display it
        clase_option_menu.pack()

        # Create layout list
        self.layout_list = ["none", "spring", "circular", "planar", "tree", "ranked", "graphviz", "acyclic"]
        # create a StringVar to store the selected item
        self.layout_option = tk.StringVar(self.root)
        # set the initial value of the option menu
        self.layout_option.set("spring")
        # create the option menu with the list of items and the StringVar
        clase_layout_option = tk.OptionMenu(self.root, self.layout_option, *self.layout_list)
        # pack the option menu to display it
        clase_layout_option.pack()

        # Create edge_style lsit
        self.edge_styles_list = ["solid", "dashed", "dotted", "dashdot"]
        # create a StringVar to store the selected item
        self.edge_style_option = tk.StringVar(self.root)
        # set the initial value of the option menu
        self.edge_style_option.set("solid")
        # create the option menu with the list of items and the StringVar
        edge_style_option = tk.OptionMenu(self.root, self.edge_style_option, *self.edge_styles_list)
        # pack the option menu to display it
        edge_style_option.pack()


        # Create checkboxes

        self.agregar_flechas_bool = tk.BooleanVar()
        self.agregar_flechas_checkbox = tk.Checkbutton(self.root,
                        text='Dibujar flechas',
                        command=self.update_flechas,
                        variable=self.agregar_flechas_bool,
                        onvalue=True,
                        offvalue=False).pack()

        # Create the canvas
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_drop)
        self.canvas.bind("<B3-Motion>", self.on_right_drag)

        # Create a menu
        self.menu = tk.Menu(self.root, tearoff=0)
        self.canvas.bind("<Button-4>", self.show_menu)

        def modo_dibujar():
            self.modo = "dibujar"
        self.menu.add_command(label="Modo dibujo", command= modo_dibujar)
        def modo_pintar():
            self.modo = "pintar"
            Palette(self)
        self.menu.add_command(label="Modo pintar", command= modo_pintar)
        def modo_borrar():
            self.modo = "borrar"
        self.menu.add_command(label="Modo borrar", command= modo_borrar)


        def modo_configurar():
            self.modo = "configurar"
        self.menu.add_command(label="Modo configurar", command= modo_configurar)


#        self.menu.add_command(label="Modo fisicas", command=self.modo_fisicas)

#        self.menu.add_command(label="Redibujar canvas", command=self.redraw_canvas)
        self.menu.add_command(label="Borrar etiquetas", command=self.delete_labels)
        self.menu.add_command(label="Borrar canvas", command=self.delete_canvas)
        self.menu.add_command(label="Imprimir", command=self.imprimir)
        self.menu.add_command(label="Codigo LaTeX", command=self.crear_latex)

        self.menu.add_command(label="Ciclo Hamiltoniano", command = self.hamiltonian_cycle)

        self.modos_list = ["dibujar", "pintar", "borrar", "configurar", "mover edges"]

        self.title = Titulo(self)


        # Start the main loop
        self.root.mainloop()

    def on_right_click(self,event):
        if self.modo == "dibujar":
            selected_node = self.selected_node
            node = self.get_node(event.x,event.y)
            if node is not None:
                if selected_node is None:
                    self.selected_node = node
                elif selected_node is not None and selected_node != node:
                    n1 = selected_node
                    n2 = node
                    n1.connect_node(n2)
                    self.selected_node = None
                elif selected_node is not None and selected_node == node:
                    node.create_loop()
                    self.selected_node = None

    def on_drop(self,event):
        self.dragged_node = None
        self.dragged_edge = None
    def on_drag(self,event):
        if self.modo == "dibujar":
            nodo = self.dragged_node
            edge = self.dragged_edge
            if nodo is not None:
                nodo.x,nodo.y = event.x, event.y
                nodo.redraw()
            elif edge is not None:
                edge.x,edge.y = event.x, event.y
                edge.redraw()

    def on_right_drag(self,event):
        if self.modo in ["borrar", "pintar"]:
            nodo = self.get_node(event.x,event.y)
            edge = self.get_edge(event.x, event.y)

            if self.modo == "borrar":
                if nodo is not None:
                    nodo.delete()
                elif edge is not None:
                    edge.delete()

            if self.modo == "pintar":
                if nodo is not None:
                    nodo.color = self.color
                    nodo.redraw()
                elif edge is not None:
                    edge.color = self.color
                    edge.redraw()

    def modo_fisicas(self):
        self.modo = "fisicas"
        # modos: "dibujar", "pintar", "borrar", "configurar", "fisicas"

    def on_click(self,event):
        if self.modo in self.modos_list:
            x, y = event.x, event.y
            nodo = self.get_node(x, y)
            edge = self.get_edge(x, y)

            if self.modo == "dibujar":
                if nodo is not None:
                    if nodo != self.dragged_node:
                        self.dragged_node = nodo
                elif edge is not None:
                    self.dragged_edge = edge
                elif nodo is None:
                    Node(x, y, self)

            if self.modo == "borrar":
                if nodo is not None:
                    nodo.delete()
                elif edge is not None:
                    edge.delete()

            if self.modo == "pintar":
                if nodo is not None:
                    nodo.color = self.color
                    nodo.redraw()
                elif edge is not None:
                    edge.color = self.color
                    edge.redraw()

            if self.modo == "configurar":
                if nodo is not None:
                    nodo.edit_label()
                elif edge is not None:
                    edge.edit_label()

    def get_node(self, x, y):
        __objects_under = self.canvas.find_overlapping(x-5, y-5, x+5, y+5)
        if len(__objects_under) == 0:
            return None
        else:
            for node in self.nodes:
                if node.canvas_id in __objects_under:
                    return node


        """
        for node in self.nodes:
            if abs(x - node.x) < 20 and abs(y - node.y) < 20:

                return node

        return None
        """

    def get_edge(self, x, y):
        __objects_under = self.canvas.find_overlapping(x-5, y-5, x+5, y+5)
        if len(__objects_under) == 0:
            return None
        else:
            for edge in self.edges:
                if edge.hitbox_id in __objects_under:
                    return edge


    """
        for edge in self.edges:
            if self.intersect_line_and_point(edge, x, y) == True:
                return edge

        return None
    
    def intersect_line_and_point(self, edge, x, y):

        def ortogonal(B):
            x = B[0]
            y = B[1]
            return np.array([y, -x])

        def aprox_entre(a, b, c):
            if a <= c:
                if (a <= b and a <= c) or b - 5 <= c or a <= b + 5:
                    return True
            if c <= a:
                if (c <= b and b <= a) or b - 5 <= a or c <= b + 5:
                    return True
            return False

        x1, y1 = edge.node1.x, edge.node1.y
        x2, y2 = edge.node2.x, edge.node2.y

        P = np.array([x, y])
        Z1 = np.array([x1, y1])
        Z2 = np.array([x2, y2])

        A = P - Z2
        B = Z1 - Z2
        W = ortogonal(B)

        W = W / np.linalg.norm(W)

        dot = A.dot(W) / np.linalg.norm(A)

        if abs(dot) < 0.01:
            if aprox_entre(x1, x, x2) and aprox_entre(y1, y, y2):
                return True

        return False

    """

    def choose_color(self):
        color_tuple = tk.colorchooser.askcolor(title="Choose color for nodes")

        self.color = color_tuple[1]

    def redraw_canvas(self):
        for node in self.nodes:
            node.redraw()

    def delete_canvas(self):
        for node in reversed(self.nodes):
            node.delete()

    def delete_labels(self):
        for node in self.nodes:
            node.clear_label()
        for edge in self.edges:
            edge.clear_label()
    def on_mouse_move(self, event):
        self.mouse_x, self.mouse_y = event.x, event.y

    def founding_parents_list(self):
        lista = []
        for edge in self.edges:
            if edge == edge.founding_parent():
                lista.append(edge)
        return lista

    def has_multiedges(self):
        for edge in self.edges:
            if len(edge.family_tree()) > 1:
                return True
        return False

    def update_flechas(self):
        for edge in self.edges:
            edge.update_arrow()
        self.redraw_canvas()

    def show_menu(self, event):
        self.menu.post(event.x_root, event.y_root)

    def imprimir(self):
        self.impresion = Impresion(self)
        self.impresion.descargar()
        """
        if self.has_multiedges():
            Impresion_multigrafo(self).descargar()
        else:
            Impresion(self).descargar()
        """

    def crear_latex(self):
        if self.impresion is None:
            Impresion(self).latex()
        else:
            self.impresion.latex()




    def hamiltonian_cycle(self):
        if self.impresion is None:
            Impresion(self).hamiltonian_cycle()
        else:
            self.impresion.hamiltonian_cycle()


if __name__ == "__main__":
    gui = GraphGUI(1200, 1000)
