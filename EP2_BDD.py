###########################################
#Grupo:
#   Gustavo Rodrigues Cayres, nUSP: 8584323
#   Pedro Marcondes, nUSP: 8941168
###########################################

from pyeda.inter import *
import sys
from parser import CTLtree
"""
def pre_imagem_fraca(X):    
    future_X = 0
    for i in X:
        future_X = future_X 
    solution = future_X & transitions
    variables = transitions.inputs
    for variable in variables if str(variables)[0] != x:
        solution = solution.restrict({variable:1}) | solution.restrict({variable:0})
        
    
    """
def pre_imagem_forte(X):
    return S & ~(pre_imagem_fraca(S & ~X))

def SAT(formula): #var. globais: S, transitions
    if formula.kind == "1":
        return S
    if formula.kind == "0":
        return 0
    if formula.kind[0] == "x":
        return eval(formula.kind) & S.restrict({eval(formula.kind):1})
    if formula.kind == "-":
        return S & ~(SAT(formula.childs[0]))
    if formula.kind == "*":
        return SAT(formula.childs[0]) & SAT(formula.childs[1])
    if formula.kind == "+":
        return SAT(formula.childs[0]) | SAT(formula.childs[1])
    if formula.kind == "EX":
        return SAT_EX(formula.childs[0])
    if formula.kind == "AF":
        return SAT_AF(formula.childs[0])
    if formula.kind == "EU":
        return SAT_EU(formula.childs[0], formula.childs[1])
    if formula.kind == "AX":    
        return SAT(CTLtree("- EX - " + str(formula.childs[0])))
    if formula.kind == "EF":    
        return SAT(CTLtree("EU(1)(" + str(formula.childs[0]) + ")")) 
    if formula.kind == "AU":
        f1 = formula.childs[0]
        f2 = formula.childs[1]
        return SAT(CTLtree("- +(EU(- "+f1+")(*(- "+f1+")(- "+f2+")))(- AF "+f2+")"))
    if formula.kind == "AG":
        return SAT(CTLtree("- EU(1)(- " + str(formula.childs[0]) + ")"))
    if formula.kind == "EG":
        return SAT(CTLtree("- AF - " + str(formula.childs[0])))
   
def SAT_EX(formula):
    X = SAT(formula)
    Y = pre_imagem_fraca(X)
    return Y
                     
def SAT_AF(formula):
    X = S
    Y = SAT(formula)
    while X != Y:
        X = Y
        Y = Y | pre_imagem_forte(Y))
    return Y

def SAT_EU(formula1, formula2):
    W = SAT(formula1)
    X = S
    Y = SAT(formula2)
    while X != Y:
        X = Y
        Y = Y | (W & pre_imagem_fraca(Y)) 
    return Y
"""
S = range(int(sys.stdin.readline()))
transitions = eval(sys.stdin.readline())
global states
states = eval(sys.stdin.readline().replace("(", "[").replace(")", "]"))
#nao esta pronto! cada elemento deve ser um BDD
formula = CTLtree(sys.stdin.readline())
k = states.index(eval(sys.stdin.readline().replace("(", "[").replace(")", "]")))

solution = SAT(S, transitions, formula)
print("Estados que satisfazem a formula: ", solution)
if k in solution:
    print("O estado de interesse satisfaz a formula!")
else:
    print("O estado de interesse NAO satisfaz a formula!")
"""
