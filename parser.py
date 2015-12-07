# Classe CTLtree com a estrutura em árvore de fórmulas CTL

# A variável "kind" é o a operação da fórmula, podendo ser "+", "*", "-", 
# "AU","EU","AG","EG","AX","EX","AF","EF", "xN" (onde N é um natural), "0", ou "1"
# No caso de "kind" ser uma operação, "childs" é uma lista ordenada com as subárvores 
# correspondentes as operandos, por exemplo +(f1)(f2) se torna uma CTLtree com kind = "+"
# e childs= [CTLtree(f1),CTLtree(f2)]

class CTLtree():
	def __init__(self,str):
		kind, childs = CTLtree.parse(str)
		self.kind = kind
		self.childs = childs
	
	def __str__(self):
		answer = "CTL_Tree: " + self.kind
		for c in self.childs:
			answer += "(" + str(c)+ ")"
		return answer
			

	def bemFormada(formula):
		parenteses = 0
		for c in formula:
			if c == '(':
				parenteses +=1
			if c == ')':
				parenteses -=1
			if parenteses <0:
				return False
		return parenteses == 0

	def separa(formula):
		parenteses = 0
		for i in range(len(formula)):
			if formula[i] == '(':
				parenteses +=1
			if formula[i] == ')':
				parenteses -=1
			if parenteses == 0:
				return i+1
		return -1

	
# Esse é a função que recebe uma fórmula CTL e converte na estrutura de árvore
	def parse(formula):
		if not CTLtree.bemFormada(formula):
			print("Formula mal formada para parse:",formula)
		formula = formula.strip()
		c = formula[0]
		l=1
		if c == "A" or c == "E":
			c += formula[1]
			l=2	

		if c == "+" or c == "*" or c == "AU" or c == "EU":
			kind = c
			if formula[l] != "(":
				print("Operador Binario sem parenteses")
			quebra = CTLtree.separa(formula[l:])

			c1 = CTLtree(formula[l+1:quebra])
			c2 = CTLtree(formula[quebra+2:-1])
			return kind,[c1,c2]

		if c == "-" or c == "EX" or c == "AX" or c == "EF" or c == "AF" or c == "EG" or c =="AG":
			kind = c
			c1 = CTLtree(formula[l:])
			return kind,[c1]

		if c == "0" or c == "1":
			return c,[]

		return formula,[]

#Função exemplo de teste para a classe CTLtree
def test():
	print("Testando parser CTL:")
	print("Arvore CTL para a expressão:-x1     " + str(CTLtree("-x1")))
	print("Arvore CTL para a expressão:AX1     " + str(CTLtree("AX1")))
	print("Arvore CTL para a expressão:+(AX EG x1)( - +(x1)(AG x2) )     " + str(CTLtree("+(AX EG x1)( - +(x1)(AG x2) )")))

if __name__=='__main__':
	test()