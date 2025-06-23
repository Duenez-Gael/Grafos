#Nombre: Vargas Reyes Frank Anthony
#Grupo: 2CV13
#Tkinter

import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

class Operaciones:
    def __init__(self, padre):
        self.padre = padre
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Sumar dos números")
        self.ventana.geometry("400x300")
        self._crear_interfaz()

    def _crear_interfaz(self):
        tk.Label(self.ventana, text="Número 1:", font=("Arial", 12)).pack(pady=5)
        self.entrada_num1 = tk.Entry(self.ventana, font=("Arial", 12))
        self.entrada_num1.pack(pady=5)

        tk.Label(self.ventana, text="Número 2:", font=("Arial", 12)).pack(pady=5)
        self.entrada_num2 = tk.Entry(self.ventana, font=("Arial", 12))
        self.entrada_num2.pack(pady=5)

        boton_sumar = tk.Button(self.ventana, text="Sumar", command=self._calcular_suma, font=("Arial", 12))
        boton_sumar.pack(pady=10)

        self.etiqueta_resultado = tk.Label(self.ventana, text="", font=("Arial", 12))
        self.etiqueta_resultado.pack(pady=10)

    def _calcular_suma(self):
        try:
            numero1 = int(self.entrada_num1.get())
            numero2 = int(self.entrada_num2.get())
            suma = numero1 + numero2
            self.etiqueta_resultado.config(text=f"Resultado: {suma}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números enteros válidos")
class GrafoC:
    def __init__(self):
        self.grafo = {}

    def agregarArista(self, origen, destino):
        if origen not in self.grafo:
            self.grafo[origen] = []
        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        recorrido = []

        while cola:
            nodo = cola.popleft()
            if nodo not in visitados:
                visitados.add(nodo)
                recorrido.append(nodo)
                for vecino in self.grafo.get(nodo, []):
                    if vecino not in visitados:
                        cola.append(vecino)
        return recorrido

    def graficar(self, recorrido=None):
        G = nx.Graph()

        for nodo, vecinos in self.grafo.items():
            for vecino in vecinos:
                G.add_edge(nodo, vecino)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=10, font_weight='bold')

        if recorrido:
            path_edges = list(zip(recorrido, recorrido[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

        plt.title("Grafo de Recomendación de Celulares")
        plt.show()

class RecomendacionCelulares:
    import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


#Metodos y funcones de RecomendacionCelulares
class RecomendacionCelulares:
    def __init__(self, padre):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Recomendación de Celulares")
        self.ventana.geometry("600x500")
        # Variables para las selecciones
        self.gama_seleccionada = tk.IntVar()
        self.caracteristica_seleccionada = tk.IntVar()
        # Grafo para mostrar resultados
        self.grafo = None
        self.recorrido = None
        self._crear_interfaz()



    def _crear_interfaz(self):
        # Título principal
        tk.Label(self.ventana, text="Recomendación de Celulares",
                font=("Arial", 16, "bold")).pack(pady=10)

        # Frame para gama
        frame_gama = tk.Frame(self.ventana)
        frame_gama.pack(pady=10, fill=tk.X, padx=20)
        tk.Label(frame_gama, text="Selecciona la Gama:",
                font=("Arial", 10)).pack(anchor=tk.W)

        # Opciones de gama
        opciones_gama = [
            ("Gama Alta", 1),
            ("Gama Media", 3),
            ("Gama Baja", 2)
        ]

        for texto, valor in opciones_gama:
            tk.Radiobutton(frame_gama, text=texto, variable=self.gama_seleccionada,
                          value=valor).pack(anchor=tk.W)

        # Frame para características
        frame_carac = tk.Frame(self.ventana)
        frame_carac.pack(pady=10, fill=tk.X, padx=20)
        tk.Label(frame_carac, text="Selecciona la Característica Principal:",
                font=("Arial", 10)).pack(anchor=tk.W)

        # Opciones de características
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

        # Botón de búsqueda
        tk.Button(self.ventana, text="Buscar Recomendación",
                 command=self.buscar_recomendacion).pack(pady=20)

        # Área para mostrar resultados
        self.texto_resultado = tk.Text(self.ventana, height=10, width=60, state='disabled')
        self.texto_resultado.pack(pady=10, padx=20)

        # Botón para mostrar grafo
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

        # Mostrar resultados en el área de texto
        self.texto_resultado.config(state='normal')
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_resultado.insert(tk.END, f"Recorrido BFS desde '{inicio}':\n\n")
        for i, nodo in enumerate(self.recorrido):
            self.texto_resultado.insert(tk.END, f"{i+1}. {nodo}\n")
        self.texto_resultado.config(state='disabled')

        # Habilitar botón para mostrar grafo
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

class MenuPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Academia de Computación")
        self.ventana.geometry("800x600")
        self.crear_menu()

    def _mostrar_tuplas(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Tuplas")
        ventana.geometry("400x300")

        tk.Label(ventana, text="Ingresa valores separados por comas:", font=("Arial", 12)).pack(pady=10)

        entrada = tk.Entry(ventana, font=("Arial", 12), width=40)
        entrada.pack(pady=10)

        resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="green")
        resultado.pack(pady=10)

        def crear_tupla():
            datos = entrada.get()
            elementos = tuple(int(x.strip()) for x in datos.split(','))
            resultado.config(text=f"Tupla creada: {elementos}")

        boton = tk.Button(ventana, text="Crear tupla", command=crear_tupla, font=("Arial", 12))
        boton.pack(pady=10)
    def _mostrar_listas (self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Listas")
        ventana.geometry("400x300")

        tk.Label(ventana, text="Ingresa valores separados por comas:", font=("Arial", 12)).pack(pady=10)

        entrada = tk.Entry(ventana, font=("Arial", 12), width=40)
        entrada.pack(pady=10)

        resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="green")
        resultado.pack(pady=10)
        def crear_lista():
            datos = entrada.get()
            elementos = [int(x.strip()) for x in datos.split(',')]
            resultado.config(text=f"lista creada: {elementos}")

        boton = tk.Button(ventana, text="Crear lista", command=crear_lista, font=("Arial", 12))
        boton.pack(pady=10)

    def _mostrar_conjuntos(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("conjuntos")
        ventana.geometry("400x300")

        tk.Label(ventana, text="Ingresa valores separados por comas:", font=("Arial", 12)).pack(pady=10)

        entrada = tk.Entry(ventana, font=("Arial", 12), width=40)
        entrada.pack(pady=10)

        resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="green")
        resultado.pack(pady=10)
        def crear_conjunto():
            try:
                datos = entrada.get()
                elementos = set(int(x.strip()) for x in datos.split(','))
                texto = ', '.join(str(n) for n in sorted(elementos))
                resultado.config(text=f"Conjunto creado: {texto}")
            except ValueError:
                messagebox.showerror("Error", "Ingresa solo numeros enteros separados por comas.")

        boton = tk.Button(ventana, text="Crear conjunto", command=crear_conjunto, font=("Arial", 12))
        boton.pack(pady=10)

    def _mostrar_pilas(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Pilas")
        ventana.geometry("400x400")

        self.pila = []

        tk.Label(ventana, text="Ingresa un valor para apilar:", font=("Arial", 12)).pack(pady=10)

        entrada = tk.Entry(ventana, font=("Arial", 12), width=30)
        entrada.pack(pady=5)

        resultado = tk.Label(ventana, text="Pila actual: []", font=("Arial", 12), fg="green")
        resultado.pack(pady=10)

        def push():
            valor = entrada.get().strip()
            if valor:
                self.pila.append(valor)
                actualizar_pila()
                entrada.delete(0, tk.END)
            else:
                messagebox.showwarning("Advertencia", "El campo no puede estar vacio.")

        def pop():
            if self.pila:
                eliminado = self.pila.pop()
                messagebox.showinfo("Elemento desapilado", f"Se elimino: {eliminado}")
                actualizar_pila()
            else:
                messagebox.showwarning("Pila vacia", "No hay elementos en la pila.")

        def actualizar_pila():
            texto = ', '.join(self.pila)
            resultado.config(text=f"Pila actual: [{texto}]")

        tk.Button(ventana, text="Agregar", command=push, font=("Arial", 12)).pack(pady=5)
        tk.Button(ventana, text="Eliminar", command=pop, font=("Arial", 12)).pack(pady=5)

    def _mostrar_colas(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Colas")
        ventana.geometry("400x400")

        self.cola = []

        tk.Label(ventana, text="Ingresa un valor para encolar:", font=("Arial", 12)).pack(pady=10)

        entrada = tk.Entry(ventana, font=("Arial", 12), width=30)
        entrada.pack(pady=5)

        resultado = tk.Label(ventana, text="Cola actual: []", font=("Arial", 12), fg="green")
        resultado.pack(pady=10)

        def enqueue():
            valor = entrada.get().strip()
            if valor:
                self.cola.append(valor)
                actualizar_cola()
                entrada.delete(0, tk.END)
            else:
                messagebox.showwarning("Advertencia", "El campo no puede estar vacio.")

        def dequeue():
            if self.cola:
                eliminado = self.cola.pop(0)
                messagebox.showinfo("elemento desencolado", f"Se elimino: {eliminado}")
                actualizar_cola()
            else:
                messagebox.showwarning("Cola vacia", "No hay elementos en la cola.")

        def actualizar_cola():
            texto = ', '.join(self.cola)
            resultado.config(text=f"cola actual: [{texto}]")

        tk.Button(ventana, text="agregar", command=enqueue, font=("Arial", 12)).pack(pady=5)
        tk.Button(ventana, text="eliminar", command=dequeue, font=("Arial", 12)).pack(pady=5)

    def _mostrar_recursividad(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Recursividad - Factorial")
        ventana.geometry("500x400")

        tk.Label(ventana, text="Ingresa un numero entero:", font=("Arial", 12)).pack(pady=10)

        entrada = tk.Entry(ventana, font=("Arial", 12), width=20)
        entrada.pack(pady=5)

        resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="green")
        resultado.pack(pady=10)

        proceso = tk.Text(ventana, height=10, width=50, font=("Courier", 10))
        proceso.pack(pady=10)

        def calcular_factorial():
            try:
                n = int(entrada.get())
                if n < 0:
                    messagebox.showerror("Error", "El numero debe ser positivo.")
                    return
                proceso.delete("1.0", tk.END)
                resultado_final = factorial(n)
                resultado.config(text=f"Resultado final: {resultado_final}")
            except ValueError:
                messagebox.showerror("Error", "Por favor ingresa un número entero valido.")

        def factorial(n):
            if n == 0:
                proceso.insert(tk.END, "factorial(0) = 1\n")
                return 1
            else:
                proceso.insert(tk.END, f"factorial({n}) = {n} * factorial({n-1})\n")
                return n * factorial(n - 1)

        tk.Button(ventana, text="Calcular factorial", command=calcular_factorial, font=("Arial", 12)).pack(pady=5)

    def _mostrar_iteracion(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Iteracion suma de N numeros naturales")
        ventana.geometry("500x400")

        tk.Label(ventana, text="Ingresa un numero entero:", font=("Arial", 12)).pack(pady=10)

        entrada = tk.Entry(ventana, font=("Arial", 12), width=20)
        entrada.pack(pady=5)

        resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="green")
        resultado.pack(pady=10)

        def suma_n_naturales(n):
            if n == 0:
                return 0
            else:
                return n + suma_n_naturales(n - 1)

        def calcular_suma():
            try:
                n = int(entrada.get())
                if n < 0:
                    messagebox.showerror("Error", "el numero debe ser positivo.")
                    return
                suma = suma_n_naturales(n)
                resultado.config(text=f"Su suma con los numeros anteriores de {n} es: {suma}")
            except ValueError:
                    messagebox.showerror("Error", "por favor ingresa un numero entero valido.")

        tk.Button(ventana, text="Calcular suma", command=calcular_suma, font=("Arial", 12)).pack(pady=10)

    def _mostrar_grafos_dirigidos(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Grafos Dirigidos")
        ventana.geometry("500x500")

        tk.Label(ventana, text="Ingrese nodos separados por comas:", font=("Arial", 12)).pack(pady=5)
        entrada_nodos = tk.Entry(ventana, font=("Arial", 12), width=40)
        entrada_nodos.pack(pady=5)

        tk.Label(ventana, text="Ingrese aristas (formato: A->B, B->C):", font=("Arial", 12)).pack(pady=5)
        entrada_aristas = tk.Entry(ventana, font=("Arial", 12), width=40)
        entrada_aristas.pack(pady=5)

        resultado = tk.Text(ventana, height=10, width=50)
        resultado.pack(pady=10)

        def mostrar_grafo():
            nodos_texto = entrada_nodos.get()
            aristas_texto = entrada_aristas.get()

            try:
                nodos = [n.strip() for n in nodos_texto.split(",") if n.strip()]
                aristas = [a.strip() for a in aristas_texto.split(",") if a.strip()]

                aristas_dirigidas = []
                for arista in aristas:
                    if "->" not in arista:
                        messagebox.showerror("Error", f"Arista '{arista}' no tiene formato origen->destino")
                        return
                    origen, destino = arista.split("->")
                    origen, destino = origen.strip(), destino.strip()
                    if origen not in nodos or destino not in nodos:
                        messagebox.showerror("Error", f"Arista '{arista}' usa nodo no declarado")
                        return
                    aristas_dirigidas.append((origen, destino))

                resultado.delete("1.0", tk.END)
                resultado.insert(tk.END, "Nodos:\n")
                resultado.insert(tk.END, ", ".join(nodos) + "\n\n")
                resultado.insert(tk.END, "Aristas dirigidas:\n")
                for origen, destino in aristas_dirigidas:
                    resultado.insert(tk.END, f"{origen} -> {destino}\n")

                G = nx.DiGraph()
                G.add_nodes_from(nodos)
                G.add_edges_from(aristas_dirigidas)

                plt.figure(figsize=(6, 4))
                pos = nx.spring_layout(G)
                nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, arrows=True, font_size=10)
                nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{u}->{v}" for u, v in G.edges()}, font_color='red')
                plt.title("Grafo Dirigido")
                plt.tight_layout()
                plt.show()

            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        tk.Button(ventana, text="Mostrar Grafo", command=mostrar_grafo, font=("Arial", 12)).pack(pady=10)

    def _mostrar_grafos_no_dirigidos(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Grafos No Dirigidos")
        ventana.geometry("500x500")

        tk.Label(ventana, text="Ingrese nodos separados por comas:", font=("Arial", 12)).pack(pady=5)
        entrada_nodos = tk.Entry(ventana, font=("Arial", 12), width=40)
        entrada_nodos.pack(pady=5)

        tk.Label(ventana, text="Ingrese aristas (formato: A-B, B-C):", font=("Arial", 12)).pack(pady=5)
        entrada_aristas = tk.Entry(ventana, font=("Arial", 12), width=40)
        entrada_aristas.pack(pady=5)

        resultado = tk.Text(ventana, height=10, width=50)
        resultado.pack(pady=10)

        def mostrar_grafo():
            nodos_texto = entrada_nodos.get()
            aristas_texto = entrada_aristas.get()

            try:
                nodos = [n.strip() for n in nodos_texto.split(",") if n.strip()]
                aristas = [a.strip() for a in aristas_texto.split(",") if a.strip()]

                aristas_no_dirigidas = []
                for arista in aristas:
                    if "-" not in arista:
                        messagebox.showerror("Error", f"Arista '{arista}' no tiene formato A-B")
                        return
                    a, b = arista.split("-")
                    a, b = a.strip(), b.strip()
                    if a not in nodos or b not in nodos:
                        messagebox.showerror("Error", f"Arista '{arista}' usa nodo no declarado")
                        return
                    aristas_no_dirigidas.append((a, b))

                resultado.delete("1.0", tk.END)
                resultado.insert(tk.END, "Nodos:\n")
                resultado.insert(tk.END, ", ".join(nodos) + "\n\n")
                resultado.insert(tk.END, "Aristas:\n")
                for a, b in aristas_no_dirigidas:
                    resultado.insert(tk.END, f"{a} - {b}\n")

                G = nx.Graph()
                G.add_nodes_from(nodos)
                G.add_edges_from(aristas_no_dirigidas)

                plt.figure(figsize=(6, 4))
                pos = nx.spring_layout(G)
                nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='black', node_size=2000, font_size=10)
                nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{u}-{v}" for u, v in G.edges()}, font_color='blue')
                plt.title("Grafo No Dirigido")
                plt.tight_layout()
                plt.show()

            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        tk.Button(ventana, text="Mostrar Grafo", command=mostrar_grafo, font=("Arial", 12)).pack(pady=10)

    def _mostrar_grafos_ponderados(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Grafos Ponderados")
        ventana.geometry("550x550")

        tk.Label(ventana, text="Ingrese nodos separados por comas:", font=("Arial", 12)).pack(pady=5)
        entrada_nodos = tk.Entry(ventana, font=("Arial", 12), width=50)
        entrada_nodos.pack(pady=5)

        tk.Label(ventana, text="Ingrese aristas con pesos (formato: A-B:3, B-C:7):", font=("Arial", 12)).pack(pady=5)
        entrada_aristas = tk.Entry(ventana, font=("Arial", 12), width=50)
        entrada_aristas.pack(pady=5)

        resultado = tk.Text(ventana, height=10, width=60)
        resultado.pack(pady=10)

        def mostrar_grafo():
            nodos_texto = entrada_nodos.get()
            aristas_texto = entrada_aristas.get()

            try:
                nodos = [n.strip() for n in nodos_texto.split(",") if n.strip()]
                aristas = [a.strip() for a in aristas_texto.split(",") if a.strip()]

                aristas_ponderadas = []
                for arista in aristas:
                    if "-" not in arista or ":" not in arista:
                        messagebox.showerror("Error", f"Formato incorrecto en: '{arista}'")
                        return
                    extremos, peso = arista.split(":")
                    a, b = extremos.split("-")
                    a, b = a.strip(), b.strip()
                    peso = float(peso.strip())
                    if a not in nodos or b not in nodos:
                        messagebox.showerror("Error", f"Nodos no válidos en arista '{arista}'")
                        return
                    aristas_ponderadas.append((a, b, peso))

                resultado.delete("1.0", tk.END)
                resultado.insert(tk.END, "Nodos:\n")
                resultado.insert(tk.END, ", ".join(nodos) + "\n\n")
                resultado.insert(tk.END, "Aristas con peso:\n")
                for a, b, p in aristas_ponderadas:
                    resultado.insert(tk.END, f"{a} - {b}: {p}\n")

                G = nx.Graph()
                G.add_nodes_from(nodos)
                for a, b, p in aristas_ponderadas:
                    G.add_edge(a, b, weight=p)

                pos = nx.spring_layout(G)
                weights = nx.get_edge_attributes(G, 'weight')

                plt.figure(figsize=(6, 4))
                nx.draw(G, pos, with_labels=True, node_color='lightyellow', edge_color='gray',
                        node_size=2000, font_size=10)
                nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_color='blue')
                plt.title("Grafo Ponderado")
                plt.tight_layout()
                plt.show()

            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        tk.Button(ventana, text="Mostrar Grafo", command=mostrar_grafo, font=("Arial", 12)).pack(pady=10)

    def _mostrar_arbol_abb(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Árbol Binario de Búsqueda (ABB)")
        ventana.geometry("600x600")

        tk.Label(ventana, text="Ingrese números separados por comas:", font=("Arial", 12)).pack(pady=10)
        entrada = tk.Entry(ventana, font=("Arial", 12), width=40)
        entrada.pack(pady=5)

        resultado = tk.Text(ventana, height=15, width=60, font=("Courier", 10))
        resultado.pack(pady=10)

        class NodoABB:
            def __init__(self, valor):
                self.valor = valor
                self.izq = None
                self.der = None

        class ArbolABB:
            def __init__(self):
                self.raiz = None
                self.G = nx.DiGraph()

            def insertar(self, valor):
                self.raiz = self._insertar_rec(self.raiz, valor)

            def _insertar_rec(self, nodo, valor):
                if nodo is None:
                    return NodoABB(valor)
                if valor < nodo.valor:
                    nodo.izq = self._insertar_rec(nodo.izq, valor)
                elif valor > nodo.valor:
                    nodo.der = self._insertar_rec(nodo.der, valor)
                return nodo

            def recorrido_inorden(self, nodo):
                return self.recorrido_inorden(nodo.izq) + [nodo.valor] + self.recorrido_inorden(nodo.der) if nodo else []

            def recorrido_preorden(self, nodo):
                return [nodo.valor] + self.recorrido_preorden(nodo.izq) + self.recorrido_preorden(nodo.der) if nodo else []

            def recorrido_postorden(self, nodo):
                return self.recorrido_postorden(nodo.izq) + self.recorrido_postorden(nodo.der) + [nodo.valor] if nodo else []

            def construir_grafo(self, nodo):
                if nodo:
                    self.G.add_node(nodo.valor)
                    if nodo.izq:
                        self.G.add_edge(nodo.valor, nodo.izq.valor)
                        self.construir_grafo(nodo.izq)
                    if nodo.der:
                        self.G.add_edge(nodo.valor, nodo.der.valor)
                        self.construir_grafo(nodo.der)

        def construir_arbol():
            texto = entrada.get()
            try:
                numeros = [int(n.strip()) for n in texto.split(",") if n.strip()]
                if not numeros:
                    raise ValueError

                arbol = ArbolABB()
                for n in numeros:
                    arbol.insertar(n)

                resultado.delete("1.0", tk.END)
                resultado.insert(tk.END, f"Inorden: {arbol.recorrido_inorden(arbol.raiz)}\n")
                resultado.insert(tk.END, f"Preorden: {arbol.recorrido_preorden(arbol.raiz)}\n")
                resultado.insert(tk.END, f"Postorden: {arbol.recorrido_postorden(arbol.raiz)}\n")

                arbol.construir_grafo(arbol.raiz)
                pos = hierarchy_pos(arbol.G, arbol.raiz.valor)

                plt.figure(figsize=(8, 5))
                nx.draw(arbol.G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12)
                plt.title("Árbol Binario de Búsqueda (ABB)")
                plt.show()

            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese números enteros válidos separados por comas.")

        def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
            pos = {}
            def _hierarchy_pos(G, root, left, right, vert_loc=0, xcenter=0.5, pos=None):
                if pos is None:
                    pos = {}
                pos[root] = (xcenter, vert_loc)
                neighbors = list(G.neighbors(root))
                if len(neighbors) >= 1:
                    dx = (right - left) / 2
                    nextx = left
                    for neighbor in neighbors:
                        pos = _hierarchy_pos(G, neighbor, nextx, nextx + dx, vert_loc - vert_gap, nextx + dx / 2, pos)
                        nextx += dx
                return pos
            return _hierarchy_pos(G, root, 0, width, vert_loc, xcenter)

        tk.Button(ventana, text="Construir ABB", command=construir_arbol, font=("Arial", 12)).pack(pady=10)


    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)

        estructura_menus = {
            "Principal": {
                "Salir": self._salir,
            },
            "Programación Avanzada": {
                "Contenedores": {
                    "Tuplas": self._mostrar_tuplas,
                    "Lista": self._mostrar_listas,
                    "Conjuntos": self._mostrar_conjuntos
                },
                "Pilas y Colas": {
                    "Pilas": self._mostrar_pilas,
                    "Colas": self._mostrar_colas
                },
                "Estructura y algoritmos avanzados": {
                    "Recursividad": self._mostrar_recursividad,
                    "iteracion": self._mostrar_iteracion
                },
                "Grafos": {
                    "grafos dirigidos": self._mostrar_grafos_dirigidos,
                    "grafos no dirigidos": self._mostrar_grafos_no_dirigidos,
                    "grafos ponderados": self._mostrar_grafos_ponderados
                },
                "Arboles": {
                    "ABB": self._mostrar_arbol_abb
                },
            },
            "Proyecto": {
                "recomendacion grafos": lambda: RecomendacionCelulares(self.ventana)
            },
            "Ayuda": {
                "Acerca de": None
            }
        }


        def crear_submenu(padre, estructura):
            for etiqueta, contenido in estructura.items():
                if callable(contenido):
                    padre.add_command(label=etiqueta, command=contenido)
                elif contenido is None:
                    padre.add_command(label=etiqueta, command=lambda s=etiqueta: self._accion(s))
                else:
                    submenu = tk.Menu(padre, tearoff=0)
                    crear_submenu(submenu, contenido)
                    padre.add_cascade(label=etiqueta, menu=submenu)

        crear_submenu(barra_menu, estructura_menus)
        self.ventana.config(menu=barra_menu)

    def _salir(self):
        self.ventana.quit()
        self.ventana.destroy()

    def _abrir_operaciones(self):
        Operaciones(self.ventana)

    def _accion(self, nombre):
        if nombre == "Acerca de":
            messagebox.showinfo("Acerca de", "Programa de Programación Avanzada\nGrupo 2cv13\npor Vargas Reyes")
        else:
            nueva_ventana = tk.Toplevel(self.ventana)
            nueva_ventana.title(nombre)
            nueva_ventana.geometry("400x300")
            etiqueta = tk.Label(nueva_ventana, text=f"Esta es la ventana para: {nombre}", font=("Arial", 14))
            etiqueta.pack(pady=20)

if __name__ == "__main__":
    aplicacion = MenuPrincipal()
    aplicacion.ventana.mainloop()
