
import numpy as np
import json

def loadIndice():
  with open('./MetricSpaces/testE.json') as f:
    data = json.load(f)
  return data

Indice=loadIndice()

space.loadDB(Indice["db"])

def inter(l):
  s1=set(l[0])
  for i in range(1,len(l)):
    s1=s1.intersection(l[i])
  return list(s1)

def perm(l1):
  l1.append(l1[0].copy())
  l1[1].sort()
  l2=l1[0].copy()
  aux=list()

  for i in l1[1]:
    j=l1[0].index(i)
    aux.append(j+1)
    l1[0][j]=-1

  return aux

def ordenar(l1):
  l1.append(l1[0].copy())
  l1[1].sort()
  aux=list()
  for i in l1[1]:
    j=l1[0].index(i)
    aux.append(j+1)
    l1[0][j]=-1
  return aux

def perminv(l1):
  aux=list()
  for i in range(len(l1)):
    res=l1.index(i+1)
    aux.append(res+1)
  return aux

def Prom(l1):
  aux=0
  for i in l1:
    aux=aux+i
  return (int)(aux/len(l1))

def Sradio(can,r):
  for x in can:
    distqu=space.Distance(0,x)
    if(distqu<=r):
      print(can.index(x))
      space.printObj(x,distqu)

def Skvecinos(can,k):
  r=999999999
  nn=list()
  nnaux=list()
  for x in can:
    if(len(nn)==k):
      r=max(nnaux)
      if(space.Distance(0,x)<r):
        nn[-1]=x
        nnaux[-1]=space.Distance(0,x)
        aux1=list()
        nnaux1=nnaux.copy()
        nnaux1.sort()
        for i in nnaux1:
          aux1.append(nn[nnaux.index(i)])
        nn=aux1
        nnaux=nnaux1

    else:
      aux1=list()
      nn.append(x)
      nnaux.append(space.Distance(0,x))
      nnaux1=nnaux.copy()
      nnaux1.sort()
      for i in nnaux1:
        aux1.append(nn[nnaux.index(i)])
      nn=aux1
      nnaux=nnaux1
  for i in range(k):
    space.printObj(nn[i],nnaux[i])





"""# Pivotes"""

def Search(q,r):
  mmdistqp=np.zeros([len(Indice["piv"]),2]).astype(int)
  space.add(q)
  qip=0
  for x in Indice["piv"]:
    max=space.distance(x,0)+r
    min=abs(space.distance(x,0)-r)
    mmdistqp[Indice["piv"].index(x),0]=min
    mmdistqp[Indice["piv"].index(x),1]=max
    if(space.distance(x,0)==0):
      qip=x
  #print(mmdistqp)
  #print(distpiv)
  rwi=list()
  for i in range(len(Indice["tabla"])):
    aux=list()
    for j in range(len(Indice["tabla"][i])):
      if(Indice["tabla"][i][j]>=mmdistqp[i,0] and Indice["tabla"][i][j]<=mmdistqp[i,1]):
        aux.append(j)
    rwi.append(aux)
  rwi=inter(rwi)
  if(qip!=0):
    rwi.append(qip)
    
  #print(rwi)

  if(r>0):
    Sradio(rwi,r)
  else:
    Skvecinos(rwi,abs(r))
    
