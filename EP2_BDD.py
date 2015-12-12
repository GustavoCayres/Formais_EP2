###########################################
#Grupo:
#   Gustavo Rodrigues Cayres, nUSP: 8584323
#   Pedro Marcondes, nUSP: 8941168
###########################################

from pyeda.inter import *
import sys
from parser import CTLtree

def pre_imagem_fraca(X):
    Y = expr2bdd(expr(str(bdd2expr(X)).replace("x", "y")))
    solution = Y & transitions
    variables = transitions.inputs
    for variable in variables:
        if str(variables)[0] == "y":
            solution = solution.restrict({variable:1}) | solution.restrict({variable:0})
    return solution

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
        f1 = str(formula.childs[0])
        f2 = str(formula.childs[1])
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
        Y = Y | pre_imagem_forte(Y)
    return Y

def SAT_EU(formula1, formula2):
    W = SAT(formula1)
    X = S
    Y = SAT(formula2)
    while X != Y:
        X = Y
        Y = Y | (W & pre_imagem_fraca(Y))
    return Y

def SAT_states(states, solution):
    sat_states = []
    sol = solution
    for i in range(len(states)):
        if sol.restrict(states[i].satisfy_one()) == 1
            sat_states.append(states[i])
    #descobrir como checar os estados, me sinto estupido =[ 

    return sat_states



sys.stdin.readline()
arrows = eval(sys.stdin.readline())

state_variables = eval(sys.stdin.readline().replace("(", "[").replace(")", "]"))
variable_indexes = []
for variable_list in state_variables:
    for variable in variable_list:
        variable_indexes.append(int(variable.strip("x")))
global variable_indexes
variable_indexes = set(variable_indexes)
formula = CTLtree(sys.stdin.readline())
k = state_variables.index(eval(sys.stdin.readline().replace("(", "[").replace(")", "]")))
x = bddvars(x, len(variable_indexes))
y = bddvars(y, len(variable_indexes)) # x'
S = 0
states = []
for i in range(len(state_variables)):
    state = 1 #AQUI NAO DEVERIA SER i?
    for index in variable_indexes:
        if "x"+index in state_variables[i]:
            state = state & eval("x"+index)
        else:
            state = state & eval("~x"+index)
    S = S | state
    states.append(state)
global S
S = S
transitions = 0
for arrow in arrows:
    transition = 1
    for index in variable_indexes:
        if "x"+index in state_variables[arrows[0]]:
            transition = transition & eval("x"+index)
        else:
            transition = transition & eval("~x"+index)
        if "x"+index in state_variables[arrows[1]]:
            transition = transition & eval("y"+index)
        else:
            transition = transition & eval("~y"+index)
    transitions = transitions | transition
global transitions
transitions = transitions

solution = SAT(formula)
print("Estados que satisfazem a formula: ", solution)
if k in solution:
    print("O estado de interesse satisfaz a formula!")
else:
    print("O estado de interesse NAO satisfaz a formula!")

