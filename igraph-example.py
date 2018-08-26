from igraph import *
import csv

contatos = []
relacionamentos = []

with open('relacionamentos.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:
            continue    
        relacionamentos.append(( int(row[0]) ,int(row[1])))
        
with open('contatos.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:
            continue
    
        contatos.append((row[0]))

g = Graph(vertex_attrs={"label":contatos}, edges=relacionamentos)

g.vs['size'] = ['60']
g.vs['color'] = ['green','red','blue','yellow']

layout = g.layout("kk")
#g.write_svg('primeiro.svg', layout=layout, vertex_size=20)

plot(g,layout=layout,bbox = (500, 300), margin = 50)