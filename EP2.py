###########################################
#Grupo:
#   Gustavo Rodrigues Cayres, nUSP: 8584323
#   Pedro Marcondes, nUSP: 8941168
###########################################

from pyeda.inter import *
import sys

def SAT(S, arrows, formula):
    if formula == "1":
        return S
    if formula == "0":
        return []
    if formula.match(x
                     
"""
~ ^
#restricts the existence of queens per row
def row_restrictions(T, n, queens):
    row_restriction = 1
    for i in range (0, n):
        for k in range(0, n - 1):
            temp = 1
            for j in range(k + 1, n):
                temp = temp & ~T[i][j]
            row_restriction = row_restriction & (~T[i][k] | temp)
    row_restriction = row_restriction.restrict(queens)
    for i in range (0, n):
        temp = 0
        for j in range(0, n):
            temp = temp | T[i][j]
        row_restriction = row_restriction & temp
    row_restriction = row_restriction.restrict(queens)
    return row_restriction

#restricts the existence of queens per column
def column_restrictions(T, n, queens):
    column_restriction = 1
    for j in range(0, n):
        for k in range(0, n - 1):
            temp = 1
            for i in range(k + 1, n):
                temp = temp & ~T[i][j]
            column_restriction = column_restriction & (~T[k][j] | temp)
    column_restriction = column_restriction.restrict(queens)
    for j in range(0, n):
        temp = 0
        for i in range(0, n):
            temp = temp | T[i][j]
        column_restriction = column_restriction & temp
    column_restriction = column_restriction.restrict(queens)
    return column_restriction

#restricts the existence of queens per diagonal above the main one
def diagonal_restrictions_1(T, n, queens):
    diagonal_restriction = 1
    for k in range(0, n):
        for i in range(0, n - 1 - k):
            temp = 1
            for j in range(i + 1, n - k):
                temp = temp & ~T[j][j + k]
            diagonal_restriction = diagonal_restriction & (~T[i][i + k] | temp)
    diagonal_restriction = diagonal_restriction.restrict(queens)     
    return diagonal_restriction

#restricts the existence of queens per diagonal below the main one
def diagonal_restrictions_2(T, n, queens):
    diagonal_restriction = 1
    for k in range(1, n):
        for i in range(0, n - 1 - k):
            temp = 1
            for j in range(i + 1, n - k):
                temp = temp & ~T[j + k][j]
            diagonal_restriction = diagonal_restriction & (~T[i + k][i] | temp)
    diagonal_restriction = diagonal_restriction.restrict(queens)
    return diagonal_restriction

#same as above, but for diagonals pointing SW-NE  
def diagonal_restrictions_3(T, n, queens):
    diagonal_restriction = 1
    for k in range(0, n):
        for i in range(0, n - 1 - k):
            temp = 1
            for j in range(i + 1, n - k):
                temp = temp & ~T[n - 1 - k - j][j]
            diagonal_restriction = diagonal_restriction & (~T[n - 1 - k - i][i] | temp)
    diagonal_restriction = diagonal_restriction.restrict(queens)
    return diagonal_restriction

def diagonal_restrictions_4(T, n, queens):
    diagonal_restriction = 1
    for k in range(1, n):
        for i in range(0, n - 1 - k):
            temp = 1
            for j in range(i + 1, n - k):
                temp = temp & ~T[n - 1 - j][j + k]
            diagonal_restriction = diagonal_restriction & (~T[n - 1 - i][i + k] | temp)
    diagonal_restriction = diagonal_restriction.restrict(queens)
    return diagonal_restriction

def n_queens_BDD(T, n, queens):
    expr = row_restrictions(T, n, queens) & column_restrictions(T, n, queens)
    expr = expr & diagonal_restrictions_1(T, n, queens) & diagonal_restrictions_2(T, n, queens)
    expr = expr & diagonal_restrictions_3(T, n, queens) & diagonal_restrictions_4(T, n, queens)
    return expr 
#displays the solution of a SAT BDD as a chess board
def display(solution, T, n):
    chars = list()
    for r in range(n):
        for c in range(n):
                if T[r,c] not in solution or solution[T[r,c]]: #tem q checar se essa variavel nao existe
                    chars.append("Q")
                else:
                    chars.append(".")
        if r != n-1:
            chars.append("\n")
    print("".join(chars))

data = sys.stdin.readlines()

n = int(data[0].split()[0])
T = bddvars("T", n, n)

k = int(data[0].split()[1])
queens = {}
for i in range(1, k + 1):
    x = int(data[i].split()[0])
    y = int(data[i].split()[1])
    queens[T[x][y]] = 1

bdd = n_queens_BDD(T, n, queens)

if bdd.is_zero():
    print("UNSAT")
else:
    print("SAT")
    display(bdd.satisfy_one(), T, n)
    """
