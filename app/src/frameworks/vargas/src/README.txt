#######################################################################

	README: métricas de Novidade e Diversidade

Ref: Vargas	
Autor: Nicollas Silva
Modificado: Diego Carvalho
#######################################################################

#Compilar
	
	make clean
	make
	
#Executar:

	./getMetrics

#Parâmetros:

	-b <trainFile>
	-p <predictionsFile>
	-o <outFile> 
	-l <testFile>
	-t <numThreads>
	-n <numPredictions>

#Formatos de Entrada e Saída:

	- Predições feitas por um recomendador qualquer:
		userId itemId:rating itemId:rating ...

	- Conjunto Treino:
		userId itemId rating
		userId itemId rating
		...

	- Conjunto Teste:
		userId itemId rating
		userId itemId rating
		...	


#codigo linux para ver quantos nucleos tem o processador
grep -c cpu[0-9] /proc/stat
