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
    return list(set(a) & set(b))

def set_union(X, Y):
    return list(set(a) | set(b))

#nao utiliza simbolos como no enunciado, devera ser consertado logo
def pre_imagem_fraca(S, transitions, X):
    index_of_states_in_X = []
    pre_imagem_fraca = []
    for state in X:
        index_of_states_in_X.append(S.index(state))
    for arrow in transitions if arrow[1] in index_of_states_in_X:
        pre_imagem_fraca.append(S[arrow[0]])
    return pre_imagem_fraca    
    
def pre_imagem_forte(S, transitions, X):
    return set_subtraction(S, pre_imagem_fraca(S, transitions, set_subtraction(S, X)))

def SAT(S, transitions, formula):
    if formula.kind == "1":
        return S
    if formula.kind == "0":
        return []
    if formula.kind[0] == "x":
        #TODO
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
        #TODO
    if formula.kind == "EF":    
        #TODO
    if formula.kind == "AU":    
        #TODO
    if formula.kind == "AG":
        #TODO
    if formula.kind == "EG":
        #TODO
   
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

S = int(sys.stdin.readline())
transitions = eval(sys.stdin.readline())
states = eval(sys.stdin.readline())
formula = CTLtree(sys.stdin.readline())
k = int(sys.stdin.readline())


