###########################################
#Grupo:
#   Gustavo Rodrigues Cayres, nUSP: 8584323
#   Pedro Marcondes, nUSP: 8941168
###########################################

from pyeda.inter import *
import sys
from parser import CTLtree

def set_subtraction(X, Y):
    return [item for item in X if item not in Y]

def set_intersection(X, Y):
    return list(set(X) & set(Y))

def set_union(X, Y):
    return list(set(X) | set(Y))

def pre_imagem_fraca(S, transitions, X):
    pre_imagem_fraca = []
    for arrow in transitions:
        if arrow[1] in X:
            pre_imagem_fraca.append(arrow[0])
    return pre_imagem_fraca
    
def pre_imagem_forte(S, transitions, X):
    return set_subtraction(S, pre_imagem_fraca(S, transitions, set_subtraction(S, X)))

def SAT(S, transitions, formula):
    if formula.kind == "1":
        return S
    if formula.kind == "0":
        return []
    if formula.kind[0] == "x":
        sat_states = []
        for i in S:
            if formula.kind in states[i]:
                sat_states.append(i)
        return sat_states
    if formula.kind == "-":
        return set_subtraction(S, SAT(S, transitions, formula.childs[0]))
    if formula.kind == "*":
        return set_intersection(SAT(S, transitions, formula.childs[0]), SAT(S, transitions, formula.childs[1]))
    if formula.kind == "+":
        return set_union(SAT(S, transitions, formula.childs[0]), SAT(S, transitions, formula.childs[1]))
    if formula.kind == "EX":
        return SAT_EX(S, transitions, formula.childs[0])
    if formula.kind == "AF":
        return SAT_AF(S, transitions, formula.childs[0])
    if formula.kind == "EU":
        return SAT_EU(S, transitions, formula.childs[0], formula.childs[1])
    if formula.kind == "AX":    
        return SAT(S, transitions, CTLtree("- EX - " + str(formula.childs[0])))
    if formula.kind == "EF":    
        return SAT(S, transitions, CTLtree("EU(1)(" + str(formula.childs[0]) + ")")) 
    if formula.kind == "AU":
        f1 = formula.childs[0]
        f2 = formula.childs[1]
        return SAT(S, transitions, CTLtree("- +(EU(- "+f1+")(*(- "+f1+")(- "+f2+")))(- AF "+f2+")"))
    if formula.kind == "AG":
        return SAT(S, transitions, CTLtree("- EU(1)(- " + str(formula.childs[0]) + ")"))
    if formula.kind == "EG":
        return SAT(S, transitions, CTLtree("- AF - " + str(formula.childs[0])))
   
def SAT_EX(S, transitions, formula):
    X = SAT(S, transitions, formula)
    Y = pre_imagem_fraca(S, transitions, X)
    return Y
                     
def SAT_AF(S, transitions, formula):
    X = S
    Y = SAT(S, transitions, formula)
    while X != Y:
        X = Y
        Y = set_union(Y, pre_imagem_forte(S, transitions, Y))
    return Y

def SAT_EU(S, transitions, formula1, formula2):
    W = SAT(S, transitions, formula1)
    X = S
    Y = SAT(S, transitions, formula2)
    while X != Y:
        X = Y
        Y = set_union(Y, set_intersection(W, pre_imagem_fraca(S, transitions, Y))) 
    return Y   

S = range(int(sys.stdin.readline()))
transitions = eval(sys.stdin.readline())
global states
states = eval(sys.stdin.readline().replace("(", "[").replace(")", "]"))
formula = CTLtree(sys.stdin.readline())
k = states.index(eval(sys.stdin.readline().replace("(", "[").replace(")", "]")))

solution = SAT(S, transitions, formula)
print("Estados que satisfazem a formula: ", solution)
if k in solution:
    print("O estado de interesse satisfaz a formula!")
else:
    print("O estado de interesse NAO satisfaz a formula!")
