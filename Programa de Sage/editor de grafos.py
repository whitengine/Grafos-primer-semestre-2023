from sage.all import *

import tkinter as tk
from tkinter import colorchooser

import numpy as np

import os


class Node:
    
    def __init__(self, x, y, index, color = "white", canvas_id = None, canvas_text_id = None):
        self.x = x
        self.y = y
        self.color = color
        self.index = index
        self.label = "Node " + str(self.index)
        self.edges = []
        self.canvas_id = canvas_id
        self.canvas_text_id = canvas_text_id
        



class Edge:
    def __init__(self, node1, node2, color = "black", canvas_id = None, canvas_text_id = None):
        self.node1 = node1
        self.node2 = node2
        self.color = color
        self.canvas_id = canvas_id
        self.canvas_text_id = canvas_text_id
        self.middlepoint = ((self.node1.x - self.node2.x)/2 , (self.node1.y - self.node2.y)/2)
        self.label = ""
        
    def equals(self, edge):
        if (self.node1 == edge.node1 and self.node2 == edge.node2) or (self.node1 == edge.node2 and self.node2 == edge.node1):
            return True
        else:
            return False

class GraphGUI:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.color = None

        self.nodes = []
        self.num_nodes = 0
        self.edges = []
        


        ########################
        @property
        def selected_node(self):
            return self.selected_node
        
        @selected_node.setter
        def selected_node(self,value):
            self.selected_node = value
            
        self.selected_node = None
        ########################

        
        self.mouse_x = 0
        self.mouse_y = 0

        self.modo = "dibujar"
        #modos: "dibujar", "pintar", "borrar", "configurar", "fisicas"

        
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Graph GUI")


        #Create option list
        self.option_list = ["Clase "+ str(i) for i in range(1,21)]
        # create a StringVar to store the selected item
        self.num_clase = tk.StringVar(self.root)
        # set the initial value of the option menu
        self.num_clase.set("Elegir número de Clase")
        # create the option menu with the list of items and the StringVar
        clase_option_menu = tk.OptionMenu(self.root, self.num_clase, *self.option_list)
        # pack the option menu to display it
        clase_option_menu.pack()


        

        # Create the canvas
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_drop)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.bind("<B3-Motion>", self.on_right_drag)
        self.canvas.bind("<Motion>", self.on_mouse_move)
        
        # Create a menu
        self.menu = tk.Menu(self.root, tearoff=0)
        self.canvas.bind("<Button-2>", self.show_menu)
        self.menu.add_command(label="Modo dibujo", command=self.modo_dibujo)
        self.menu.add_command(label="Modo pintar", command=self.modo_pintar)
        self.menu.add_command(label="Modo borrar", command=self.modo_borrar)
        self.menu.add_command(label="Modo configurar", command=self.modo_configurar)
        self.menu.add_command(label="Modo fisicas", command=self.modo_fisicas)
        self.menu.add_command(label="Redibujar canvas", command=self.redraw_canvas)
        self.menu.add_command(label="Imprimir", command=self.imprimir)


        # Start the main loop
        self.root.mainloop()


    def modo_dibujo(self):
        self.modo = "dibujar"
        #modos: "dibujar", "pintar", "borrar", "configurar", "fisicas"

        
    def modo_pintar(self):
        self.modo = "pintar"
        self.choose_color()
        #modos: "dibujar", "pintar", "borrar", "configurar", "fisicas"



    def modo_borrar(self):
        self.modo = "borrar"
        #modos: "dibujar", "pintar", "borrar", "configurar", "fisicas"



    def modo_configurar(self):
        self.modo = "configurar"
        #modos: "dibujar", "pintar", "borrar", "configurar", "fisicas"



    def modo_fisicas(self):
        self.modo = "fisicas"
        #modos: "dibujar", "pintar", "borrar", "configurar", "fisicas"





    def create_node(self,x,y):
        node = Node(x,y,self.num_nodes)
        self.nodes.append(node)
        self.num_nodes = self.num_nodes + 1

        self.draw_node(node)
        
        

        

    def get_node(self,x,y):
        for node in self.nodes:
            if abs(x - node.x) < 20 and abs(y - node.y) < 20:
                return node

        return None


    def get_edge(self,x,y):
        for edge in self.edges:
            if self.intersect_line_and_point(edge,x,y) == True:
                return edge

        return None

    def intersect_line_and_point(self,edge,x,y):

        def ortogonal(B):
            x = B[0]
            y = B[1]
            return np.array([y,-x])

        def aprox_entre(a,b,c):
            if a <= c:
                if (a <= b and a <= c) or b - 5 <= c or a <= b + 5 :
                    return True
            if c <= a:
                if (c <= b and b <= a) or b - 5 <= a or c <= b + 5 :
                    return True
            return False
                
        
        x1,y1 = edge.node1.x, edge.node1.y
        x2,y2 = edge.node2.x, edge.node2.y

        P = np.array([x,y])
        Z1 = np.array([x1,y1])
        Z2 = np.array([x2,y2])

        A = P-Z2
        B = Z1 - Z2
        W = ortogonal(B)

        W = W/np.linalg.norm(W)

        dot = A.dot(W) /np.linalg.norm(A)

        if abs(dot) < 0.01:
            if aprox_entre(x1,x,x2) and aprox_entre(y1,y,y2):
                return True

        return False


        '''
    
    def intersect_line_and_point(self,edge,x,y):        
        x1,y1 = edge.node1.x, edge.node1.y
        x2,y2 = edge.node2.x, edge.node2.y

        P = np.array([x,y])
        P1 = np.array([x1,y1])
        P2 = np.array([x2,y2])

        norm = np.linalg.norm
        
        distance_P_to_line = norm(np.cross(P2-P1,P1 - P))/norm(P2-P1)
        print(distance_P_to_line)

        def aprox_entre(a,b,c):
            if a <= c:
                if (a <= b and a <= c) or b - 5 <= c or a <= b + 5 :
                    return True
            if c <= a:
                if (c <= b and b <= a) or b - 5 <= a or c <= b + 5 :
                    return True
            return False

        if distance_P_to_line < 10:
            if aprox_entre(x1,x,x2) and aprox_entre(y1,y,y2):
                return True

        return False

    '''


    

    def delete_node(self,node):
        self.nodes.remove(node)
        self.num_nodes = self.num_nodes - 1
        node_index = node.index

        incident_edges = []
        for e in node.edges:
            incident_edges.append(e)

        for e in incident_edges:
            self.delete_edge(e)
        
        for n in self.nodes:
            if n.index > node_index:
                n.index = n.index-1
                self.redraw_node(n)
        self.canvas.delete(node.canvas_id)
        self.canvas.delete(node.canvas_text_id)

        del node

        
        #self.redraw_canvas()
        #self.canvas.update()
        #for n in self.nodes:
        #    print(n,n.index)
        


    def delete_edge(self,edge):
        if edge in self.edges:
            self.edges.remove(edge)
            self.canvas.delete(edge.canvas_id)
            self.canvas.delete(edge.canvas_text_id)

        
        n1,n2 = edge.node1, edge.node2
        
        if edge in n1.edges:
            n1.edges.remove(edge)
        if edge in n2.edges:
            n2.edges.remove(edge)

        
        del edge

        #self.canvas.update()
        
        


    def on_click(self, event):
        x, y = event.x, event.y


        ya_hay_nodo = False
        for node in self.nodes:
            if abs(x - node.x) < 20 and abs(y - node.y) < 20:
                ya_hay_nodo = True
                self.selected_node = node
                break


        #####################################            
        #Modo dibujar
        if self.modo == "dibujar":
            node = self.get_node(x,y)
            if node is None:
                self.create_node(x,y)
                self.selected_node = node





        #####################################
        if (self.modo == "pintar") and (self.color is not None):
            while True:
                node = self.get_node(x,y)
                if node is not None:
                    node.color = self.color
                    self.redraw_node(node)
                    break

                edge = self.get_edge(x,y)
                if edge is not None:
                    edge.color = self.color
                    self.redraw_edge(edge)

                break


        #####################################
        #Modo borrar
        if self.modo == "borrar":
            while True:
                node = self.get_node(x,y)
                if node is not None:
                    self.delete_node(node)
                    break

                edge = self.get_edge(x,y)
                if edge is not None:
                    self.delete_edge(edge)

                break




        #####################################
        #Modo configurar
        if self.modo == "configurar":
            #
            print("calamardo")




        #####################################
        #Modo fisicas
        if self.modo == "fisicas":
            #
            print("calamardo")




        #####################################


    
        
            


    def on_right_click(self, event):
        x, y = event.x, event.y


        #####################################            
        #Modo dibujar
        if self.modo == "dibujar":
            if self.selected_node is not None:
                nodo = self.get_node(x,y)
                if nodo != self.selected_node:
                    if nodo is not None:
                        self.create_edge(nodo,self.selected_node)
                        self.selected_node = None

            else:
                nodo = self.get_node(x,y)
                self.selected_node = nodo




        #####################################
        #Modo pintar
        if self.modo == "pintar":
            #
            print("calamardo")
            





        #####################################
        #Modo borrar
        if self.modo == "borrar":
            #
            print("calamardo")





        #####################################
        #Modo configurar
        if self.modo == "configurar":
            #
            print("calamardo")




        #####################################
        #Modo fisicas
        if self.modo == "fisicas":
            #
            print("calamardo")




        #####################################
        
       

        

    def on_drag(self, event):
        x, y = event.x, event.y

        #####################################            
        #Modo dibujar
        if self.modo == "dibujar":
            if self.selected_node is not None:
                node = self.selected_node
                node.x = x
                node.y = y
                self.redraw_node(node)
        



        #####################################
        #Modo pintar
        if self.modo == "pintar":
            #
            print("calamardo")
            





        #####################################
        #Modo borrar
        if self.modo == "borrar":
            #
            print("calamardo")





        #####################################
        #Modo configurar
        if self.modo == "configurar":
            #
            print("calamardo")




        #####################################
        #Modo fisicas
        if self.modo == "fisicas":
            #
            print("calamardo")




        #####################################


    def on_drop(self,event):
        x,y = event.x,event.y


        #####################################            
        #Modo dibujar
        if self.modo == "dibujar":
            if self.selected_node is not None:
                node = self.selected_node
                node.x = x
                node.y = y
                self.redraw_node(node)

                self.selected_node = None
        



        #####################################
        #Modo pintar
        if self.modo == "pintar":
            pass
            





        #####################################
        #Modo borrar
        if self.modo == "borrar":
            pass





        #####################################
        #Modo configurar
        if self.modo == "configurar":
            pass




        #####################################
        #Modo fisicas
        if self.modo == "fisicas":
            pass




        #####################################        

        

    def on_right_drag(self, event):
        x,y = event.x, event.y
        
        #####################################            
        #Modo dibujar
        #if self.modo == "dibujar":
            





        #####################################
        #Modo pintar
        if (self.modo == "pintar") and (self.color is not None):
            while True:
                node = self.get_node(x,y)
                if node is not None:
                    node.color = self.color
                    self.redraw_node(node)
                    break

                edge = self.get_edge(x,y)
                if edge is not None:
                    edge.color = self.color
                    self.redraw_edge(edge)

                break




        #####################################
        #Modo borrar
        if self.modo == "borrar":
            node = self.get_node(x,y)
            if node is not None:
                self.delete_node(node)

            edge = self.get_edge(x,y)
            if edge is not None:
                self.delete_edge(edge)





        #####################################
        #Modo configurar
        if self.modo == "configurar":
            #
            print("calamardo")




        #####################################
        #Modo fisicas
        if self.modo == "fisicas":
            #
            print("calamardo")




        #####################################

        

    def draw_node(self, node):
        x, y = node.x, node.y
        label = node.label
        color = node.color
        index = node.index
                
        node.canvas_id = self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color, outline="black", tag = label)
        node.canvas_text_id = self.canvas.create_text(x, y, text=str(index), font=("Arial", 10))


    def choose_color(self):    
        color_tuple = tk.colorchooser.askcolor(title="Choose color for nodes")

        self.color = color_tuple[1]


    def create_edge(self, node1,node2):

        edge = Edge(node1,node2)

        is_edge_repetido = False
        for e in self.edges:
            if e.equals(edge):
                is_edge_repetido = True

        if is_edge_repetido == False:
            color = edge.color
            self.draw_edge(edge)
            
            node1.edges.append(edge)
            node2.edges.append(edge)
            self.edges.append(edge)

        


    def draw_edge(self,edge):
        x1,y1 = edge.node1.x, edge.node1.y
        x2,y2 = edge.node2.x, edge.node2.y
        color = edge.color

        P = edge.middlepoint
        x = P[0]
        y = P[1]

        label = edge.label
        
        edge.canvas_id = self.canvas.create_line(x1, y1, x2, y2, fill=color, width = 1)
        edge.canvas_text_id = self.canvas.create_text(x, y, text= label, font=("Arial", 10))

        self.canvas.tag_lower(edge.canvas_text_id)
        self.canvas.tag_lower(edge.canvas_id)


    def redraw_edge(self,edge):
        x1,y1 = edge.node1.x, edge.node1.y
        x2,y2 = edge.node2.x, edge.node2.y
        color = edge.color

        P = edge.middlepoint
        x = P[0]
        y = P[1]

        label = edge.label

        self.canvas.delete(edge.canvas_id)
        self.canvas.delete(edge.canvas_text_id)
        
        edge.canvas_id = self.canvas.create_line(x1, y1, x2, y2, fill=color, width = 1)
        edge.canvas_text_id =self.canvas.create_text(x, y, text= label, font=("Arial", 10))

        self.canvas.tag_lower(edge.canvas_text_id)
        self.canvas.tag_lower(edge.canvas_id)

        

    '''

    def connect_nodes(self):
        self.canvas.create_text(self.mouse_x, self.mouse_y, text="Click to connect", tags="menu")
        
        self.canvas.unbind("<Button-1>")
        #self.canvas.delete("menu")
        self.canvas.unbind("<Button-3>")
        self.canvas.bind("<Button-1>", self.on_connect_click)

    def on_connect_click(self, event):
        x, y = event.x, event.y
        for node in self.nodes:
            if abs(x - node.x) < 20 and abs(y - node.y) < 20:
                if self.selected_node is not None and node != self.selected_node:
                    color = tk.colorchooser.askcolor(title="Choose color for edge")
                    edge.color = color[1]
                    edge = Edge(self.selected_node, node)
                    self.edges.append(edge)
                    self.selected_node.edges.append(edge)
                    node.edges.append(edge)
                    self.draw_edge(edge)
                    self.selected_node = None
                    break
            else:
                self.selected_node = None

    '''


    def redraw_canvas(self):
        self.modo = "Redibujar canvas"
        for n in self.nodes:
            self.redraw_node(n)

    def redraw_node(self,node):
        self.canvas.delete(node.canvas_id)
        self.canvas.delete(node.canvas_text_id)
        self.draw_node(node)
        
        for edge in node.edges:
            self.canvas.delete(edge.canvas_id)
            self.canvas.delete(edge.canvas_text_id)
            self.draw_edge(edge)
        

    def on_mouse_move(self,event):
        self.mouse_x, self.mouse_y = event.x, event.y

    def show_menu(self, event):
        self.menu.post(event.x_root, event.y_root)


    def imprimir(self):
        G = Graph({node.index : node.edges for node in self.nodes})
        title = self.tkinter.simpledialog.askstring("Titluo del grafo", "Titulo del grafo")
        if title is None:
            title = ""
            
        plot = G.plot(title = title)

        plot.show(figsize = 3)

        descargar()

        def descargar():
            clase = self.num_clase.get()
            raiz = os.path.join("..","Users", "yo","Desktop","Doctorado Chile", "Clases", "2023", "Primer semestre", "Grafos", "Programa de Sage")
            path = os.path.join(raiz,"Figuras", str(clase))
            
            #este bloque encuentra cual es el primer nombre "Clase x" disponible
            x = 1
            Dibujo_path = os.path.join(path, "Dibujo " + str(x) + ".pdf")
            while os.path.exists(Dibujo_path):   
                x = x + 1
                Dibujo_path = os.path.join(path, "Dibujo " + str(x) + ".pdf")
            
            #plot = G.plot() de mas arriba del jupyter
            plot.save(Dibujo_path) #guarda el archivo.
            print(Dibujo_path)

        

        
        


if __name__ == "__main__":
    gui = GraphGUI(800, 600)
