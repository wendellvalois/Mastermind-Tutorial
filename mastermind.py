import random

#parte mais IMPORTANTE a de checagem de pecas bancas e pretas
def checa_jogada(resp,jog):
    resposta, jogada = list(resp), list(jog) #transforma as strings em listas
    acertos, quase_acertos = 0, 0
    # Inicia checagem por acertos - pinos pretos
    for i in range(len(jogada)):
        if resposta[i] == jogada[i]:
            acertos += 1
            resposta[i] =  None    #limpa da lista o valor correto
        # Inicia checagem por quase acertos - pinos brancos
        else:   
            for j in range(len(resposta)):
                if resposta[j] == jogada[i]:
                    quase_acertos += 1
                    resposta[j] =  None
                    break 

    return (acertos, quase_acertos)

#testa todas as saidas de combinacoes de pecas brancas e pretas
def aplica_testes(): 
    casos_testes = ((("OOBB","RRYY"), (0,0)),
              (("YYYR","OOOY"), (0,1)),
              (("RROO","OOYY"), (0,2)),
              (("RYBO","YBRY"), (0,3)),
              (("RYBO","OBYR"), (0,4)),
              (("YYYY","YRRR"), (1,0)),
              (("OOBB","OBYY"), (1,1)),
              (("OOBB","OBOY"), (1,2)),
              # Nao existe      (1,3)
              (("OYOY","OYRB"), (2,0)),
              (("OYOY","OYYR"), (2,1)),
              (("RGBO","RGOB"), (2,2)),
              (("OYOR","OYOY"), (3,0)),
              # Nao existe      (3,1) 
            #   (("RYBO","RYBO"), (4,0))),
              (("RYBO","RYBO"), (4,0)),
              # extra
              (("RYBO","RYBO"), (4,0)),
              (("BJBB","YYYB"), (1,0)),
              (("RBGP","RGBY"), (1,2)),
              (("RBGB","RBBY"), (1,2)))

    for caso_teste, esperado in casos_testes:
        print ("Input: %r Esperado %r Recebido %r" % (caso_teste, esperado, checa_jogada(*caso_teste)))


def execucao_jogo():    
    numero_pinos = 4
    #cores = 'RGBCOP' # Vermelho, Verde, Azul, Ciano, Laranja, Rosa
    cores = ['1','2','3','4','5','6'] # Tambem pode funcionar com numeros ao inves de letras
    resposta = []
    for _ in range(numero_pinos):
        resposta.append(random.choice(cores))
    # resposta = [random.choice(cores) for _ in range(numero_pinos)] #versao reduzida
    print('A resposta eh:', *resposta, 'Esta linha eh apenas para testes') #por motivos de teste
    print('As opcoes de cores sao:', *cores)
    print('Insira a sua jogada:')
    for tentativa in range(10):
        #Verificacao de codigo inserido pelo usuario
        while(True):            
            jogada = (input('Jogada: ')).upper()
            if(jogada == ''):
                print('Nenhum argumento inserido, tente novamente')
                continue
            if(len(jogada) > numero_pinos):
                print('Jogada com mais que quatro valores')
                continue
            if(len(jogada) < numero_pinos):
                print('Jogada com menos que quatro valores')
                continue
            codigo_valido = False
            for i in range(numero_pinos):
                for j in range(len(cores)):
                    if(jogada[i] == cores[j]):
                        codigo_valido = True          
                        break
                    else:
                        codigo_valido = False
                if(codigo_valido == False):
                    print('codigo invalido na posicao', i)
                    break
            if(not codigo_valido):
                continue
            if(len(jogada) == numero_pinos):
                break

        resultado_jogada = checa_jogada(resposta, jogada)
        print(resultado_jogada)
        if (resultado_jogada == (4,0)):
            print ('Voce venceu! :D')
            break
    if(tentativa == 9):
        print('Voce perdeu, tente outra vez! :(')        
    print('Jogo encerrado')
    
#O MAIN DO CODIGO
print('Aplicando series de testes na funcao de checagem')
print('Legenda: R - Red, G - Green, B - Blue, C - Ciano, O - Orange, P - Pink')
aplica_testes()
print('Iniciando Jogo ...')
print()
execucao_jogo()
