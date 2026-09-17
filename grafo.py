"""Carga, limpieza y construccion del grafo de rutas."""
import csv
import heapq

ALIAS = {
    'nazca': 'Nasca',
}

def leer_aristas(ruta):
    filas = []
    with open(ruta, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            filas.append({'origen': r['origen'], 'destino': r['destino'], 'distancia_km': r['distancia_km']})
    return filas

def leer_heuristica(ruta):
    H = {}
    with open(ruta, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            H[r['ciudad'].strip()] = int(r['h_km'])
    return H

def limpiar(filas):
    vistas, limpio = set(), []
    for f in filas:
        origen = f['origen'].strip()
        destino = f['destino'].strip()
        if origen.lower() in ALIAS: origen = ALIAS[origen.lower()]
        if destino.lower() in ALIAS: destino = ALIAS[destino.lower()]
        try:
            distancia = int(f['distancia_km'])
        except (ValueError, TypeError):
            continue
        clave = frozenset({origen, destino})
        if clave in vistas: continue
        vistas.add(clave)
        limpio.append((origen, destino, distancia))
    return limpio

def construir_grafo(aristas):
    G = {}
    for origen, destino, distancia in aristas:
        G.setdefault(origen, []).append((destino, distancia))
        G.setdefault(destino, []).append((origen, distancia))
    for ciudad in G:
        G[ciudad] = sorted(G[ciudad])
    return G

def costos_optimos_a(G, meta):
    dist = {meta: 0}
    pq = [(0, meta)]
    while pq:
        d, n = heapq.heappop(pq)
        if d > dist.get(n, float('inf')): continue
        for m, costo in G[n]:
            if d + costo < dist.get(m, float('inf')):
                dist[m] = d + costo
                heapq.heappush(pq, (d + costo, m))
    return dist

def verificar_heuristica(G, H, meta):
    h_estrella = costos_optimos_a(G, meta)
    no_admisibles = [n for n in H if H[n] > h_estrella.get(n, float('inf'))]
    inconsistentes = []
    for n in G:
        for m, costo in G[n]:
            if n in H and m in H and H[n] > costo + H[m]:
                inconsistentes.append((n, m))
    return no_admisibles, inconsistentes
