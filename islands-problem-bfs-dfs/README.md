# Island Problem

El problema consiste en contar cuántas islas existe en el mapa.

El mapa es una matriz de n filas y m columnas. En la matriz pueden haber 1s o 0s. Los 1s indican que hay una isla y los 0 indican que hay agua. Los 1s están conectados en 2 direcciones: horizontales y verticales, no están conectados en diagonales.

Por ejemplo, el siguiente mapa contiene 4 islas.

```
111000
111000
000001
000001
100010
```

## Solución

El problema se lo puede solucionar utilizando tanto BFS como DFS. Ambas soluciones están presentes en el código.

## Instalación
Se necesita tener instalado `Python 3.7`.

Ejecutar:

```
$ cd islands-problem-bfs-dfs
$ python main.py
```

