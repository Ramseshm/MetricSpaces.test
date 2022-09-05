# -*- coding: utf-8 -*-
"""Main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wMOza5siY7szftCoKze8zRphMLQ_MruP
"""

import numpy as np
import json
import random
#from ...espacio import String as space
from ...espacio import Vectors as space

def Naive(q,r):
  space.add(q)
  for x in range(1,space.tam()):
    v1=space.distance(0,x)
    if(v1<=r):
      space.printObj(x,v1)
  space.pop()

#Naive("casa",1)

#Cargar db-------------------------------------
dbloc=""
#----------------------------------------------



region=0.00025
PermlenMin=4
PermlenMax=8
"""# Permutaciones"""

def perm(l1):
  l1.append(l1[0].copy())
  l2=l1[0].copy()
  l1[1].sort()
  aux=list()
  contador=0
  for i in l1[1]:
    j=l1[0].index(i)
    aux.append(j+1)
    l1[0][j]=-1
  for i in range(len(l1[1])):
    if(l1[1][i]<=region):
      contador=contador+1

  if(contador==0):
    d=l2[aux[0]-1]
    dr=d+(region-d)
    
    for i in range(len(l1[1])):
      if(l1[1][i]<=dr):
        contador=contador+1
    if(contador>PermlenMax):
      return aux[:PermlenMax]
    elif(contador<PermlenMin):
      return aux[:PermlenMin]
    else:
      return aux[:contador]

  elif(contador>PermlenMax):
    return aux[:PermlenMax]
  elif(contador<PermlenMin):
    return aux[:PermlenMin]
  else:
    return aux[:contador]


#print(perm([[10,20,11,14,16]]))

def Permutantes(nper):
  ##Seleccionar permutantes
  per=list()
  for i in range(1,nper):
    per.append(random.randint(1,(space.tam())))
    
  ##matriz de permutaciones
  Pi=[[]]
  for i in range(1,(space.tam())):
    aux=[[]]
    for j in per:
      aux[0].append(space.Distance(i,j))  
    Pi.append(perm(aux))

  #promedio de "cortes"
  prom=0
  for i in range(1,len(Pi)):
    prom=prom+len(Pi[i])
  prom=int((prom/(len(Pi)-1)))

  #creacion de indice
  indice={"db":dbloc,"perm":per,"tablaPerm":Pi,"PromCorte":prom}

  return indice


#Permutantes()
#print(Permutantes()["tablaPermInv"][0])

def Build(loc,np,indexname="indexPermutantes"):
  global dbloc
  dbloc=loc
  space.loadDB(dbloc)
  data=Permutantes(np)
  #print(data["perm"])
  path="./"+indexname+".json"
  with open(path, 'w') as f:
    json.dump(data, f,indent=4)
