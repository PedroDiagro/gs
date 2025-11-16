O programa WorkBalance AI coleta informações de 5 colaboradores, armazenando cada registro em um dicionário dentro de uma lista. Os dados coletados incluem nome, departamento, horas trabalhadas, quantidade de pausas, nível de estresse (1 a 5) e tarefas concluídas.

Com base nesses dados, o sistema realiza cálculos utilizando a biblioteca NumPy, gerando a média e o desvio padrão das horas trabalhadas, além da média do nível de estresse. Ele também identifica o colaborador mais estressado, lista os colaboradores que concluíram 5 ou mais tarefas e aponta aqueles que apresentam risco de desequilíbrio (alto estresse e poucas pausas).

O programa exibe um relatório completo no console e também salva todas as informações em um arquivo chamado relatorio_workbalance.txt, incluindo a data e hora da execução. Há tratamento de erros tanto na entrada dos dados quanto na gravação do arquivo.

Por fim, o sistema gera um feedback individual para cada colaborador, baseado na combinação entre produtividade, pausas e nível de estresse.
