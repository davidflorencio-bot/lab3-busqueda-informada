"""Cinco algoritmos de busqueda: BFS, DFS, costo uniforme, Greedy y A*."""
import heapq
from collections import deque


class Metricas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.expandidos = 0
        self.generados = 0
        self.frontera_max = 0

    def observar_frontera(self, tamano):
        self.frontera_max = max(self.frontera_max, tamano)

    def expandir(self):
        self.expandidos += 1

    def generar(self):
        self.generados += 1

    def fila(self, costo):
        return (self.nombre, costo, self.expandidos, self.generados, self.frontera_max)


def reconstruir(padre, meta):
    camino, actual = [], meta
    while actual is not None:
        camino.append(actual)
        actual = padre[actual]
    return camino[::-1]


def costo_camino(G, camino):
    total = 0
    for a, b in zip(camino, camino[1:]):
        total += dict(G[a])[b]
    return total


def bfs(G, inicio, meta):
    m = Metricas('BFS')
    padre = {inicio: None}
    visitados = {inicio}
    frontera = deque([inicio])
    m.generar()
    while frontera:
        m.observar_frontera(len(frontera))
        n = frontera.popleft()
        m.expandir()
        if n == meta:
            camino = reconstruir(padre, meta)
            return camino, costo_camino(G, camino), m
        for vecino, _c in G[n]:
            if vecino not in visitados:
                visitados.add(vecino)
                padre[vecino] = n
                m.generar()
                frontera.append(vecino)
    return None, None, m


def dfs(G, inicio, meta):
    m = Metricas('DFS')
    padre = {inicio: None}
    visitados = {inicio}
    frontera = [inicio]
    m.generar()
    while frontera:
        m.observar_frontera(len(frontera))
        n = frontera.pop()
        m.expandir()
        if n == meta:
            camino = reconstruir(padre, meta)
            return camino, costo_camino(G, camino), m
        for vecino, _c in reversed(G[n]):
            if vecino not in visitados:
                visitados.add(vecino)
                padre[vecino] = n
                m.generar()
                frontera.append(vecino)
    return None, None, m


def greedy_best_first(G, inicio, meta, h):
    m = Metricas('Greedy')
    padre = {inicio: None}
    frontera = [(h[inicio], 0, inicio)]
    en_frontera = {inicio}
    cerrados = set()
    orden = 0
    m.generar()
    while frontera:
        m.observar_frontera(len(frontera))
        _, _, n = heapq.heappop(frontera)
        en_frontera.discard(n)
        m.expandir()
        if n == meta:
            camino = reconstruir(padre, meta)
            return camino, costo_camino(G, camino), m
        cerrados.add(n)
        for vecino, _c in G[n]:
            if vecino in cerrados or vecino in en_frontera:
                continue
            padre[vecino] = n
            orden += 1
            en_frontera.add(vecino)
            m.generar()
            heapq.heappush(frontera, (h[vecino], orden, vecino))
    return None, None, m


def a_estrella(G, inicio, meta, h, w=1.0):
    m = Metricas('A*' if w == 1.0 else f'A*(w={w})')
    g = {inicio: 0}
    padre = {inicio: None}
    frontera = [(w * h[inicio], 0, inicio)]
    cerrados = set()
    orden = 0
    m.generar()
    while frontera:
        m.observar_frontera(len(frontera))
        _, _, n = heapq.heappop(frontera)
        if n in cerrados:
            continue
        m.expandir()
        if n == meta:
            camino = reconstruir(padre, meta)
            return camino, g[meta], m
        cerrados.add(n)
        for vecino, costo in G[n]:
            g_tentativo = g[n] + costo
            if g_tentativo < g.get(vecino, float('inf')):
                g[vecino] = g_tentativo
                padre[vecino] = n
                orden += 1
                m.generar()
                heapq.heappush(frontera, (g_tentativo + w * h[vecino], orden, vecino))
    return None, None, m


def costo_uniforme(G, inicio, meta):
    h_nula = {k: 0 for k in G}
    camino, costo, m = a_estrella(G, inicio, meta, h_nula, w=1.0)
    m.nombre = 'Costo uniforme'
    return camino, costo, m


def imprimir_tabla(resultados):
    print(f"{'Algoritmo':<16}{'Costo (km)':>12}{'Expandidos':>12}{'Generados':>12}{'Frontera max.':>15}")
    for nombre, costo, exp, gen, fmax in resultados:
        print(f"{nombre:<16}{costo:>12}{exp:>12}{gen:>12}{fmax:>15}")
