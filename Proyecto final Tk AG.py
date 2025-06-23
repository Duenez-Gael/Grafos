# ############################################################################
# **    Proyecto       : Proyecto Final Tkinter
# **    Plataforma     : Python
# **    Herramienta    : Visual Studio Code
# **    Compilador     : IDLE Python
# **    Fecha/Hora     : 19-06-2025, 22:36 pm
# **    Descripción    : Proyecto de con interfaz grafica utilizando Tkinter 
#                        mostrando los temas de Contenedores, Pilas, Colas, 
#                        Grafos, Arboles binarios, Proyecto
#
# **   By             : Dueñez Mejia Angel Gael
# **   Grupo          : 2CV13
# **   Materia        : Programación avanzada
##############################################################################






# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :                    Importación de Módulos y Bibliotecas                    :
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
import threading
import time
import queue
import random
from tkinter import ttk
from tkinter import scrolledtext
from collections import deque



# ==============================================================================
# ||                                                                           ||   
# ||                    P R O G R A M A  G E N E R A L                         ||
# ||                                                                           ||
# ==============================================================================


cola = []
pila = []

class Cola:
    def __init__(self, padre):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("COLAS")
        self.ventana.geometry("400x300")
        self._crear_interfaz()

    def _crear_interfaz(self):
        self.etiquetac1 = tk.Label(self.ventana, text="Ingresa un valor:", font=("Arial", 10))
        self.etiquetac2 = tk.Label(self.ventana, text="Ingresa un valor:", font=("Arial", 10))
        self.entradac1 = tk.Entry(self.ventana, width=30)
        self.entradac2 = tk.Entry(self.ventana, width=30)
        self.etiqueta_mcola = tk.Label(self.ventana, text="", font=("Arial", 10))

        self.boton_encolar = tk.Button(self.ventana, text="Encolar", command=self.encolar)
        self.boton_desencolar = tk.Button(self.ventana, text="Desencolar", command=self.desencolar)
        self.boton_mostrar = tk.Button(self.ventana, text="Mostrar Cola", command=self.mostrar_cola)

        self.etiquetac1.pack(pady=5)
        self.entradac1.pack(pady=5)
        self.etiquetac2.pack(pady=5)
        self.entradac2.pack(pady=5)
        self.boton_encolar.pack(pady=5)
        self.boton_desencolar.pack(pady=5)
        self.boton_mostrar.pack(pady=5)
        self.etiqueta_mcola.pack(pady=5)

    def encolar(self):
        v1 = self.entradac1.get()
        v2 = self.entradac2.get()
        if v1 and v2:
            cola.append(v1)
            cola.append(v2)
            self.entradac1.delete(0, tk.END)
            self.entradac2.delete(0, tk.END)

    def desencolar(self):
        if cola:
            cola.pop(0)

    def mostrar_cola(self):
        self.etiqueta_mcola.config(text=f"Cola: {cola}")


class Pila:
    def __init__(self, padre):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("PILAS")
        self.ventana.geometry("400x300")
        self._crear_interfaz()

    def _crear_interfaz(self):
        self.etiquetap1 = tk.Label(self.ventana, text="Ingresa un valor:", font=("Arial", 10))
        self.etiquetap2 = tk.Label(self.ventana, text="Ingresa un valor:", font=("Arial", 10))
        self.entradap1 = tk.Entry(self.ventana, width=30)
        self.entradap2 = tk.Entry(self.ventana, width=30)
        self.etiqueta_mpila = tk.Label(self.ventana, text="", font=("Arial", 10))

        self.boton_apilar = tk.Button(self.ventana, text="Apilar", command=self.apilar)
        self.boton_desapilar = tk.Button(self.ventana, text="Desapilar", command=self.desapilar)
        self.boton_mostrar = tk.Button(self.ventana, text="Mostrar Pila", command=self.mostrar_pila)

        self.etiquetap1.pack(pady=5)
        self.entradap1.pack(pady=5)
        self.etiquetap2.pack(pady=5)
        self.entradap2.pack(pady=5)
        self.boton_apilar.pack(pady=5)
        self.boton_desapilar.pack(pady=5)
        self.boton_mostrar.pack(pady=5)
        self.etiqueta_mpila.pack(pady=5)

    def apilar(self):
        v1 = self.entradap1.get()
        v2 = self.entradap2.get()
        if v1 and v2:
            pila.append(v1)
            pila.append(v2)
            self.entradap1.delete(0, tk.END)
            self.entradap2.delete(0, tk.END)

    def desapilar(self):
        if pila:
            pila.pop()

    def mostrar_pila(self):
        self.etiqueta_mpila.config(text=f"Pila: {pila}")


class Contenedores:
    def __init__(self, padre, tipo):
        self.tipo = tipo
        self.ventana = tk.Toplevel(padre)
        self.ventana.title(tipo.upper())
        self.ventana.geometry("400x300")
        self._crear_interfaz()

    def _crear_interfaz(self):
        if self.tipo == "listas":
            self.lista = []
            self.entrada = tk.Entry(self.ventana, width=30)
            self.boton_agregar = tk.Button(self.ventana, text="Agregar", command=self.agregar_lista)
            self.boton_eliminar = tk.Button(self.ventana, text="Eliminar", command=self.eliminar_lista)
            self.boton_mostrar = tk.Button(self.ventana, text="Mostrar", command=self.mostrar_lista)
            self.etiqueta = tk.Label(self.ventana, text="", font=("Arial", 10))

            self.entrada.pack(pady=5)
            self.boton_agregar.pack(pady=5)
            self.boton_eliminar.pack(pady=5)
            self.boton_mostrar.pack(pady=5)
            self.etiqueta.pack(pady=5)

        elif self.tipo == "tuplas":
            self.tupla = ()
            self.entrada = tk.Entry(self.ventana, width=30)
            self.boton_crear = tk.Button(self.ventana, text="Crear tupla", command=self.crear_tupla)
            self.boton_mostrar = tk.Button(self.ventana, text="Mostrar", command=self.mostrar_tupla)
            self.etiqueta = tk.Label(self.ventana, text="", font=("Arial", 10))

            self.entrada.pack(pady=5)
            self.boton_crear.pack(pady=5)
            self.boton_mostrar.pack(pady=5)
            self.etiqueta.pack(pady=5)

        elif self.tipo == "conjuntos":
            self.curso1 = set()
            self.curso2 = set()
            self.entrada1 = tk.Entry(self.ventana, width=30)
            self.entrada2 = tk.Entry(self.ventana, width=30)
            self.boton_cargar = tk.Button(self.ventana, text="Cargar alumnos", command=self.cargar_conjuntos)
            self.boton_duplicados = tk.Button(self.ventana, text="Duplicados", command=self.mostrar_duplicados)
            self.boton_exclusivos = tk.Button(self.ventana, text="Exclusivos", command=self.mostrar_exclusivos)
            self.etiqueta = tk.Label(self.ventana, text="", font=("Arial", 10))

            self.entrada1.pack(pady=5)
            self.entrada2.pack(pady=5)
            self.boton_cargar.pack(pady=5)
            self.boton_duplicados.pack(pady=5)
            self.boton_exclusivos.pack(pady=5)
            self.etiqueta.pack(pady=5)

        elif self.tipo == "diccionarios":
            self.empleados = {}
            self.entrada_id = tk.Entry(self.ventana, width=30)
            self.entrada_nombre = tk.Entry(self.ventana, width=30)
            self.entrada_puesto = tk.Entry(self.ventana, width=30)
            self.entrada_salario = tk.Entry(self.ventana, width=30)
            self.boton_agregar = tk.Button(self.ventana, text="Agregar", command=self.agregar_empleado)
            self.boton_listar = tk.Button(self.ventana, text="Listar", command=self.listar_empleados)
            self.etiqueta = tk.Label(self.ventana, text="", font=("Arial", 10))

            self.entrada_id.pack(pady=2)
            self.entrada_nombre.pack(pady=2)
            self.entrada_puesto.pack(pady=2)
            self.entrada_salario.pack(pady=2)
            self.boton_agregar.pack(pady=5)
            self.boton_listar.pack(pady=5)
            self.etiqueta.pack(pady=5)

    def agregar_lista(self):
        valor = self.entrada.get()
        self.lista.append(valor)
        self.entrada.delete(0, tk.END)

    def eliminar_lista(self):
        valor = self.entrada.get()
        if valor in self.lista:
            self.lista.remove(valor)
        self.entrada.delete(0, tk.END)

    def mostrar_lista(self):
        self.etiqueta.config(text=f"Lista: {self.lista}")

    def crear_tupla(self):
        datos = self.entrada.get().split(',')
        self.tupla = tuple(map(str.strip, datos))

    def mostrar_tupla(self):
        self.etiqueta.config(text=f"Tupla: {self.tupla}")

    def cargar_conjuntos(self):
        self.curso1 = set(map(str.strip, self.entrada1.get().split(',')))
        self.curso2 = set(map(str.strip, self.entrada2.get().split(',')))

    def mostrar_duplicados(self):
        duplicados = self.curso1 & self.curso2
        self.etiqueta.config(text=f"Duplicados: {duplicados}")

    def mostrar_exclusivos(self):
        exclusivos = (self.curso1 - self.curso2) | (self.curso2 - self.curso1)
        self.etiqueta.config(text=f"Exclusivos: {exclusivos}")

    def agregar_empleado(self):
        try:
            id_emp = self.entrada_id.get()
            nombre = self.entrada_nombre.get()
            puesto = self.entrada_puesto.get()
            salario = float(self.entrada_salario.get())
            self.empleados[id_emp] = {"nombre": nombre, "puesto": puesto, "salario": salario}
        except ValueError:
            messagebox.showerror("Error", "Salario inválido")

    def listar_empleados(self):
        texto = "\n".join([f"{id}: {info['nombre']}, {info['puesto']}, ${info['salario']}" for id, info in self.empleados.items()])
        self.etiqueta.config(text=texto or "No hay empleados registrados")


class Grafo:
    def __init__(self, padre, tipo):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title(f"Grafo {tipo}")
        self.ventana.geometry("400x150")
        self.tipo = tipo
        self._crear_interfaz()

    def _crear_interfaz(self):
        etiqueta = tk.Label(self.ventana, text=f"Grafo {self.tipo}", font=("Arial", 12, "bold"))
        etiqueta.pack(pady=10)

        boton_mostrar = tk.Button(self.ventana, text="Mostrar grafo", command=self.mostrar_grafo)
        boton_mostrar.pack(pady=10)

    def mostrar_grafo(self):
        if self.tipo == "No Dirigido":
            self.grafo_no_dirigido()
        elif self.tipo == "Dirigido":
            self.grafo_dirigido()
        elif self.tipo == "Ponderado":
            self.grafo_ponderado()
        elif self.tipo == "Matriz de Adyacencia":
            self.grafo_matriz_adyacencia()

    def grafo_no_dirigido(self):
        G = nx.Graph()
        G.add_nodes_from(["A", "B", "C", "D"])
        G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])
        plt.figure()
        plt.gcf().canvas.manager.set_window_title("Grafo No Dirigido")
        nx.draw(G, with_labels=True)
        plt.show()

    def grafo_dirigido(self):
        g = nx.DiGraph()
        g.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
        g.add_edges_from([
            ('A', 'B'), ('A', 'C'),
            ('B', 'D'), ('B', 'E'),
            ('B', 'F')
        ])
        plt.figure(figsize=(5, 5))
        plt.gcf().canvas.manager.set_window_title("Grafo Dirigido")
        nx.draw(g, with_labels=True, arrows=True,
                node_color='skyblue', edge_color='black',
                node_size=2000, font_size=12)
        plt.title("Grafo Dirigido \n Angel Gael")
        plt.show()

    def grafo_ponderado(self):
        g = nx.DiGraph()
        g.add_edge('A', 'B', weight=8)
        g.add_edge('A', 'C', weight=22)
        g.add_edge('B', 'C', weight=4)

        pos = nx.spring_layout(g)
        plt.figure()
        nx.draw(g, pos, with_labels=True, font_color='black',
                node_color='skyblue', node_size=2000,
                font_size=15, font_weight='bold', arrows=True)

        edge_labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
        plt.gcf().canvas.manager.set_window_title("Grafo Ponderado")
        plt.title("Grafo Ponderado")
        plt.show()

    def grafo_matriz_adyacencia(self):
        class MatrizGrafo:
            def __init__(self, numVertices, dirigido=False):
                self.numVertices = numVertices
                self.dirigido = dirigido
                self.matriz = [[0] * numVertices for _ in range(numVertices)]

            def agregar_arista(self, origen, destino, peso=1):
                self.matriz[origen][destino] = peso
                if not self.dirigido:
                    self.matriz[destino][origen] = peso

            def visualizar(self):
                G = nx.DiGraph() if self.dirigido else nx.Graph()
                for i in range(self.numVertices):
                    G.add_node(i)
                for i in range(self.numVertices):
                    for j in range(self.numVertices):
                        if self.matriz[i][j] != 0:
                            G.add_edge(i, j, weight=self.matriz[i][j])
                pos = nx.spring_layout(G)
                plt.figure()
                nx.draw(G, pos, with_labels=True, node_color='skyblue',
                        edge_color='black', node_size=2000, font_size=12)
                edge_labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
                plt.title("Matriz y Grafo\nAGael")
                plt.gcf().canvas.manager.set_window_title("Matriz de Adyacencia")
                plt.show()

        grafo = MatrizGrafo(4, dirigido=False)
        grafo.agregar_arista(0, 1)
        grafo.agregar_arista(0, 2)
        grafo.agregar_arista(1, 3)
        grafo.visualizar()


class Nodo:
    def __init__(self, codigo, nombre, domicilio):
        self.codigo = codigo
        self.nombre = nombre
        self.domicilio = domicilio
        self.izquierdo = None
        self.derecho = None

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.domicilio}"

class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, codigo, nombre, domicilio):
        if self.raiz is None:
            self.raiz = Nodo(codigo, nombre, domicilio)
        else:
            self._insertar(self.raiz, codigo, nombre, domicilio)

    def _insertar(self, actual, codigo, nombre, domicilio):
        if codigo < actual.codigo:
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(codigo, nombre, domicilio)
            else:
                self._insertar(actual.izquierdo, codigo, nombre, domicilio)
        elif codigo > actual.codigo:
            if actual.derecho is None:
                actual.derecho = Nodo(codigo, nombre, domicilio)
            else:
                self._insertar(actual.derecho, codigo, nombre, domicilio)

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append(str(nodo))
            self._inorden(nodo.derecho, resultado)

    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        if nodo:
            resultado.append(str(nodo))
            self._preorden(nodo.izquierdo, resultado)
            self._preorden(nodo.derecho, resultado)

    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        if nodo:
            self._postorden(nodo.izquierdo, resultado)
            self._postorden(nodo.derecho, resultado)
            resultado.append(str(nodo))

    def graficar(self):
        G = nx.DiGraph()
        etiquetas = {}

        def agregar_nodos(nodo):
            if nodo:
                G.add_node(nodo.codigo)
                etiquetas[nodo.codigo] = f"{nodo.codigo}\n{nodo.nombre}"
                if nodo.izquierdo:
                    G.add_edge(nodo.codigo, nodo.izquierdo.codigo)
                    agregar_nodos(nodo.izquierdo)
                if nodo.derecho:
                    G.add_edge(nodo.codigo, nodo.derecho.codigo)
                    agregar_nodos(nodo.derecho)

        agregar_nodos(self.raiz)
        pos = nx.spring_layout(G)
        plt.figure()
        nx.draw(G, pos, labels=etiquetas, with_labels=True,
                node_color='lightblue', node_size=2000, font_size=10, arrows=True)
        plt.title("Árbol Binario")
        plt.gcf().canvas.manager.set_window_title("Árbol Binario")
        plt.show()


class ArbolBinario:
    def __init__(self, padre):
        self.abb = ABB()
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Árbol Binario")
        self.ventana.geometry("500x500")
        self._crear_interfaz()

    def _crear_interfaz(self):
        tk.Label(self.ventana, text="Código:").pack()
        self.entry_codigo = tk.Entry(self.ventana)
        self.entry_codigo.pack()

        tk.Label(self.ventana, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self.ventana)
        self.entry_nombre.pack()

        tk.Label(self.ventana, text="Domicilio:").pack()
        self.entry_domicilio = tk.Entry(self.ventana)
        self.entry_domicilio.pack()

        tk.Button(self.ventana, text="Insertar Nodo", command=self.insertar_nodo).pack(pady=10)
        tk.Button(self.ventana, text="Mostrar Grafo", command=self.abb.graficar).pack(pady=10)

        self.texto_resultado = tk.Text(self.ventana, height=15, width=60)
        self.texto_resultado.pack()

    def insertar_nodo(self):
        codigo = self.entry_codigo.get()
        nombre = self.entry_nombre.get()
        domicilio = self.entry_domicilio.get()
        if codigo and nombre and domicilio:
            try:
                codigo = int(codigo)
                self.abb.insertar(codigo, nombre, domicilio)
                self.entry_codigo.delete(0, tk.END)
                self.entry_nombre.delete(0, tk.END)
                self.entry_domicilio.delete(0, tk.END)
                self.mostrar_recorridos()
            except ValueError:
                messagebox.showerror("Error", "Código debe ser un número entero")
        else:
            messagebox.showwarning("Campos vacíos", "Completa todos los campos")

    def mostrar_recorridos(self):
        inorden = "\n".join(self.abb.inorden())
        preorden = "\n".join(self.abb.preorden())
        postorden = "\n".join(self.abb.postorden())

        texto = f"--- Inorden ---\n{inorden}\n\n--- Preorden ---\n{preorden}\n\n--- Postorden ---\n{postorden}"
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_resultado.insert(tk.END, texto)



lockA = threading.Lock()
lockB = threading.Lock()

def caja_segura(nombre):
    primero, segundo = sorted([lockA, lockB], key=id)
    with primero:
        time.sleep(0.1)
        with segundo:
            print(f"{nombre} logró acceso seguro")

class DulceriaCP:
    def __init__(self, text_widget):
        self.cola_clientes = queue.PriorityQueue()
        self.lock = threading.Lock()
        self.sem = threading.Semaphore(3)
        self.atendidos = 0
        self.text_widget = text_widget

    def _print(self, msg):
        self.text_widget.configure(state='normal')
        self.text_widget.insert(tk.END, msg + "\n")
        self.text_widget.see(tk.END)
        self.text_widget.configure(state='disabled')

    def llegada_clientes(self, total):
        for i in range(1, total + 1):
            time.sleep(random.uniform(0.05, 0.2))
            prioridad = random.randint(5, 10)
            self.cola_clientes.put((prioridad, f"Cliente-{i}"))
            self._print(f"Llegó Cliente-{i} con prioridad {prioridad} (En cola: {self.cola_clientes.qsize()})")

    def caja(self, numero):
        while True:
            try:
                prioridad, cliente = self.cola_clientes.get(timeout=2)
            except queue.Empty:
                break
            with self.sem:
                self._print(f"[Caja-{numero}] Atendiendo a {cliente} (Prioridad {prioridad})")
                time.sleep(random.uniform(0.3, 0.6))
                with self.lock:
                    self.atendidos += 1
                self._print(f"[Caja-{numero}] Terminó con {cliente} | Total atendidos: {self.atendidos}")
                self.cola_clientes.task_done()

    def caja_prioritaria(self):
        while True:
            with self.sem:
                prioridad = 1
                cliente = f"Cliente-P-{int(time.time() * 1000) % 1000}"
                self.cola_clientes.put((prioridad, cliente))
                self._print(f"[PRIORIDAD] Insertó {cliente} con prioridad {prioridad}")
                time.sleep(0.1)




class GrafoC:
    def __init__(self):
        self.adyacencias = {}

    def agregarArista(self, origen, destino):
        self.adyacencias.setdefault(origen, []).append(destino)
        self.adyacencias.setdefault(destino, []).append(origen)

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        recorrido = []

        while cola:
            nodo = cola.popleft()
            if nodo not in visitados:
                visitados.add(nodo)
                recorrido.append(nodo)
                cola.extend([vecino for vecino in self.adyacencias[nodo] if vecino not in visitados])
        return recorrido

    def graficar(self, recorrido):
        G = nx.Graph()
        for nodo, vecinos in self.adyacencias.items():
            for vecino in vecinos:
                G.add_edge(nodo, vecino)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray', node_size=800, font_weight='bold')

        colores = ['red', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']
        for i, nodo in enumerate(recorrido):
            nx.draw_networkx_nodes(G, pos, nodelist=[nodo], node_color=colores[i % len(colores)], node_size=800)

        plt.title(f"Recorrido BFS desde '{recorrido[0]}'")
        plt.show()
        

class RecomendacionCelulares:
    def __init__(self, padre):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Recomendación de Celulares")
        self.ventana.geometry("800x650")

        self.gama_seleccionada = tk.IntVar()
        self.caracteristica_seleccionada = tk.IntVar()

        self.grafo = None
        self.recorrido = None
        self._crear_interfaz()
        
        
    def _crear_interfaz(self):
        tk.Label(self.ventana, text="Recomendación de Celulares", 
                font=("Arial", 16, "bold")).pack(pady=10)
        
        frame_gama = tk.Frame(self.ventana)
        frame_gama.pack(pady=10, fill=tk.X, padx=20)
        tk.Label(frame_gama, text="Selecciona la Gama:", 
                font=("Arial", 10)).pack(anchor=tk.W)
        
        opciones_gama = [
            ("Gama Alta", 1),
            ("Gama Media", 3),
            ("Gama Baja", 2)
        ]
        
        for texto, valor in opciones_gama:
            tk.Radiobutton(frame_gama, text=texto, variable=self.gama_seleccionada,
                          value=valor).pack(anchor=tk.W)
        
        frame_carac = tk.Frame(self.ventana)
        frame_carac.pack(pady=10, fill=tk.X, padx=20)
        tk.Label(frame_carac, text="Selecciona la Característica Principal:", 
                font=("Arial", 10)).pack(anchor=tk.W)
        
        opciones_carac = [
            ("Cámara", 1),
            ("Batería", 2),
            ("Almacenamiento", 3),
            ("Memoria RAM", 4),
            ("Procesador", 5)
        ]
        
        for texto, valor in opciones_carac:
            tk.Radiobutton(frame_carac, text=texto, variable=self.caracteristica_seleccionada,
                          value=valor).pack(anchor=tk.W)
        
        tk.Button(self.ventana, text="Buscar Recomendación", 
                 command=self.buscar_recomendacion).pack(pady=20)
        
        # Área para mostrar resultados
        self.texto_resultado = tk.Text(self.ventana, height=10, width=60, state='disabled')
        self.texto_resultado.pack(pady=10, padx=20)
        
        self.boton_grafo = tk.Button(self.ventana, text="Mostrar Grafo", 
                                    command=self.mostrar_grafo, state='disabled')
        self.boton_grafo.pack(pady=10)

    def buscar_recomendacion(self):
        gama = self.gama_seleccionada.get()
        caracteristica = self.caracteristica_seleccionada.get()
        
        if not gama or not caracteristica:
            messagebox.showwarning("Campos vacíos", "Selecciona una gama y una característica")
            return
            
        grafo = GrafoC()
        inicio = ""
        
        if caracteristica == 1:
            if gama == 1:
                grafo.agregarArista('Camara Pro', 'Apple\niPhone 16 Pro Max')
                grafo.agregarArista('Camara Pro', 'Samsung\nGalaxy S25 Ultra')
                grafo.agregarArista('Apple\niPhone 16 Pro Max', 'Google\nPixel 9 Pro')
                grafo.agregarArista('Samsung\nGalaxy S25 Ultra', 'Xiaomi\nXiaomi 15 Ultra')
                inicio = 'Camara Pro'
            elif gama == 2:
                grafo.agregarArista('Buena Camara', 'Motorola\nMoto E13')
                grafo.agregarArista('Buena Camara', 'Xiaomi\nRedmi A2')
                grafo.agregarArista('Motorola\nMoto E13', 'Samsung\nGalaxy A03')
                grafo.agregarArista('Xiaomi\nRedmi A2', 'Infinix\nInfinix Smart 7')
                inicio = 'Buena Camara'
            elif gama == 3:
                grafo.agregarArista('Camara Equilibrada', 'Samsung\nGalaxy A24')
                grafo.agregarArista('Camara Equilibrada', 'Xiaomi\nRedmi Note 12')
                grafo.agregarArista('Samsung\nGalaxy A24', 'Realme\nRealme C55')
                grafo.agregarArista('Xiaomi\nRedmi Note 12', 'Motorola\nMoto G32')
                inicio = 'Camara Equilibrada'

        elif caracteristica == 2:
            if gama == 1:
                grafo.agregarArista('Bateria Premium', 'Apple\niPhone 15 Plus')
                grafo.agregarArista('Bateria Premium', 'Samsung\nGalaxy S24 Ultra')
                grafo.agregarArista('Apple\niPhone 15 Plus', 'OnePlus\nOneplus 12R')
                grafo.agregarArista('Xiaomi\nXiaomi 13 Ultra', 'Samsung\nGalaxy S23 Ultra')
                inicio = 'Bateria Premium'
            elif gama == 2:
                grafo.agregarArista('Buena Bateria', 'Xiaomi\nRedmi 10C')
                grafo.agregarArista('Buena Bateria', 'Motorola\nMoto G13')
                grafo.agregarArista('Motorola\nMoto G13', 'Itel\nIntel P40')
                inicio = 'Buena Bateria'
            elif gama == 3:
                grafo.agregarArista('Bateria Equilibrada', 'Samsung\nSamsung M14')
                grafo.agregarArista('Bateria Equilibrada', 'Realme\nRealme Narzo 50A')
                grafo.agregarArista('Realme\nRealme Narzo 50A', 'Xiaomi\nXiaomi Redmi Note 11')
                inicio = 'Bateria Equilibrada'

        elif caracteristica == 3:
            if gama == 1:
                grafo.agregarArista('Almacenamiento Alto', 'Samsung\nGalaxy S24 Ultra')
                grafo.agregarArista('Almacenamiento Alto', 'Apple\niPhone 15 Pro Max')
                inicio = 'Almacenamiento Alto'
            elif gama == 2:
                grafo.agregarArista('Almacenamiento Básico', 'Infinix\nInfinix Smart 6')
                grafo.agregarArista('Almacenamiento Básico', 'Tecno\nTecno Spark 10')
                inicio = 'Almacenamiento Básico'
            elif gama == 3:
                grafo.agregarArista('Almacenamiento Medio', 'Xiaomi\nRedmi Note 11')
                grafo.agregarArista('Almacenamiento Medio', 'Motorola\nMoto G22')
                inicio = 'Almacenamiento Medio'

        elif caracteristica == 4:
            if gama == 1:
                grafo.agregarArista('RAM Premium', 'Apple\niPhone 15 Pro')
                grafo.agregarArista('RAM Premium', 'Samsung\nGalaxy S23 Ultra')
                inicio = 'RAM Premium'
            elif gama == 2:
                grafo.agregarArista('RAM Básica', 'Xiaomi\nRedmi A1')
                grafo.agregarArista('RAM Básica', 'Motorola\nMoto E20')
                inicio = 'RAM Básica'
            elif gama == 3:
                grafo.agregarArista('RAM Intermedia', 'Realme\nRealme C25Y')
                grafo.agregarArista('RAM Intermedia', 'Xiaomi\nXiaomi Redmi 10')
                inicio = 'RAM Intermedia'

        elif caracteristica == 5:
            if gama == 1:
                grafo.agregarArista('Procesador Premium', 'Oneplus\nOneplus 12R')
                grafo.agregarArista('Procesador Premium',  'Apple\niPhone 15 Pro Max')
                inicio = 'Procesador Premium'
            elif gama == 2:
                grafo.agregarArista('Procesador Básico', 'Infinix\nInfinix Hot 11')
                grafo.agregarArista('Procesador Básico', 'Xiaomi\nRedmi 10A')
                inicio = 'Procesador Básico'
            elif gama == 3:
                grafo.agregarArista('Procesador Medio', 'Motorola\nMoto esge 50 neo')
                grafo.agregarArista('Procesador Medio', 'Xiaomi\nRedmi note 13 pro')
                inicio = 'Procesador Medio'

        self.recorrido = grafo.bfs(inicio)
        self.grafo = grafo
        
        self.texto_resultado.config(state='normal')
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_resultado.insert(tk.END, f"Recorrido BFS desde '{inicio}':\n\n")
        for i, nodo in enumerate(self.recorrido):
            self.texto_resultado.insert(tk.END, f"{i+1}. {nodo}\n")
        self.texto_resultado.config(state='disabled')
        
        self.boton_grafo.config(state='normal')

    def mostrar_grafo(self):
        if self.grafo and self.recorrido:
            self.grafo.graficar(self.recorrido)




class MenuPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Proyecto Final AG")
        self.ventana.geometry("600x400")
        self.crear_menu()

    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)

        estructura_menus = {
            "Principal": {
                "Salir": self._salir
            },
            "Programación Avanzada": {
                "Contenedores": {
                    "Listas": lambda: Contenedores(self.ventana, "listas"),
                    "Tuplas": lambda: Contenedores(self.ventana, "tuplas"),
                    "Conjuntos": lambda: Contenedores(self.ventana, "conjuntos"),
                    "Diccionarios": lambda: Contenedores(self.ventana, "diccionarios")
                },
                "Pilas y Colas": {
                    "Pilas": lambda: Pila(self.ventana),
                    "Colas": lambda: Cola(self.ventana)
                },
                "Grafos": {
                    "No Dirigidos": lambda: Grafo(self.ventana, "No Dirigido"),
                    "Dirigidos": lambda: Grafo(self.ventana, "Dirigido"),
                    "Ponderado": lambda: Grafo(self.ventana, "Ponderado"),
                    "Matriz de Adyacencia": lambda: Grafo(self.ventana, "Matriz de Adyacencia")
                },
                "Arbol Binario":{
                    "Visualizar Árbol": lambda: ArbolBinario(self.ventana)
                },
                "Concurrencia":{
                    "Simulación Dulcería": self.abrir_ventana_concurrencia
                    
                }
            },
            "Proyecto":{
                "Ver proyecto": {
                    "Recomendación de Celulares": lambda: RecomendacionCelulares(self.ventana)
                }
            
            },
            
            "Ayuda": {
                "Acerca de": self._acerca
            }
        }

        def crear_submenu(padre, estructura):
            for etiqueta, accion in estructura.items():
                if callable(accion):
                    padre.add_command(label=etiqueta, command=accion)
                elif isinstance(accion, dict):
                    submenu = tk.Menu(padre, tearoff=0)
                    crear_submenu(submenu, accion)
                    padre.add_cascade(label=etiqueta, menu=submenu)

        crear_submenu(barra_menu, estructura_menus)
        self.ventana.config(menu=barra_menu)
        

    def abrir_ventana_concurrencia(self):
            ventana_conc = tk.Toplevel(self.ventana)
            ventana_conc.title("Simulación de concurrencia")
            ventana_conc.geometry("600x400")

            titulo = tk.Label(ventana_conc, text="Simulación de concurrencia", font=("Arial", 16))
            titulo.pack(pady=10)

            boton_iniciar = tk.Button(ventana_conc, text="Iniciar Simulación")
            boton_iniciar.pack(pady=10)

            texto_salida = scrolledtext.ScrolledText(ventana_conc, width=70, height=15, state='disabled')
            texto_salida.pack(padx=10, pady=10)

            dulceria = DulceriaCP(texto_salida)

            def iniciar_simulacion():
                boton_iniciar.config(state='disabled')
                hilo_productor = threading.Thread(target=dulceria.llegada_clientes, args=(30,))
                hilo_productor.start()

                hilos_cajas = [threading.Thread(target=dulceria.caja, args=(i,)) for i in range(1, 4)]
                for h in hilos_cajas:
                    h.start()

                threading.Thread(target=dulceria.caja_prioritaria, daemon=True).start()

                threading.Thread(target=caja_segura, args=("CajaSegura-1",)).start()
                threading.Thread(target=caja_segura, args=("CajaSegura-2",)).start()

            boton_iniciar.config(command=iniciar_simulacion)
               

    def _salir(self):
        self.ventana.quit()
        self.ventana.destroy()

    def _acerca(self):
        messagebox.showinfo("Acerca de", "Programa de Programación Avanzada\npor Angel Gael Dueñez Mejia\nGrupo 2CV13")




# ==============================================================================
# ||                                                                           ||
# ||        P R O G R A M A / F U N C I O N    P R I N C I P A L               ||
# ||                                                                           ||
# ==============================================================================

if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.ventana.mainloop()