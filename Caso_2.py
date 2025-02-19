from collections import deque  
import heapq  

# Definición del grafo (ciudades y rutas con distancias)  
graph = {  
    'Tunja': {'Bogotá': 150, 'Tabio': 128,'Facatativa': 42,'Alban': 17,'Viani': 30,'Cambao':47,'Guayabal': 33,'Mariquita': 20,'Fresno': 25,'Padua': 16,'Manizales': 0},  
   
}  

# Heurística: Distancia en línea recta estimada a Manizales (valores ficticios)  
heuristic = {  
    'Tunja': 246,  
    'Tabio': 128,  
    'Facatativa': 42,  
    'Alban': 17,  
    'Viani': 30,
    'Cambao':47,
    'Guayabal': 33,
    'Mariquita': 20,
    'Fresno': 25,
    'Padua': 16,
    'Manizales': 0 
}  

# Algoritmo A*  
def a_star(graph, start, goal, heuristic):  
    open_set = []  
    heapq.heappush(open_set, (0, start))  
    came_from = {}  
    g_score = {city: float('inf') for city in graph}  
    g_score[start] = 0  
    f_score = {city: float('inf') for city in graph}  
    f_score[start] = heuristic[start]  

    while open_set:  
        _, current = heapq.heappop(open_set)  

        if current == goal:  
            path = []  
            while current in came_from:  
                path.append(current)  
                current = came_from[current]  
            path.append(start)  
            return path[::-1]  

        for neighbor, distance in graph[current].items():  
            tentative_g_score = g_score[current] + distance  
            if tentative_g_score < g_score[neighbor]:  
                came_from[neighbor] = current  
                g_score[neighbor] = tentative_g_score  
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]  
                heapq.heappush(open_set, (f_score[neighbor], neighbor))  

    return None  

# Ejecución del algoritmo  
start = 'Tunja'  
goal = 'Manizales'  
path = a_star(graph, start, goal, heuristic)  
print(f"Ruta más corta: {path}")