import tkinter as tk
import random
import collections

class Mastermind:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(parent)
        self.status = tk.Label(parent)

        #CARREGA ARQUIVOS DE IMAGEM
        #Os arquivos de imagem devem 5ser iniciados no main ou construtor
        #ou sofrem um bug especifico do Python e nao aparecem na tela
        self.orange = tk.PhotoImage(file='orange.png')
        self.red = tk.PhotoImage(file='red.png')
        self.yellow = tk.PhotoImage(file='yellow.png')
        self.green = tk.PhotoImage(file='green.png')
        self.blue = tk.PhotoImage(file='blue.png')
        self.purple = tk.PhotoImage(file='purple.png')

        self.black = tk.PhotoImage(file='black.png')
        self.white = tk.PhotoImage(file='white.png')

        self.desenhaTabuleiro()



    def desenhaTabuleiro(self, event=None):
        self.canvas.destroy() #remove canvas caso exista
        self.status.destroy()
        self.canvas = tk.Canvas(self.parent, width=1040, height=480, background='#DBD8C2')
        self.canvas.pack() #faz com que o canvas (painel) apareca
        
        tamanhoimagens = 43
        #coloca cores do lado direito do tabuleiro
        self.painel_cores = {'r':self.canvas.create_image(1000, tamanhoimagens,   image=self.red),
                    'o':self.canvas.create_image(1000, tamanhoimagens+80,  image=self.orange),
                    'y':self.canvas.create_image(1000, tamanhoimagens+80*2, image=self.yellow),
                    'g':self.canvas.create_image(1000, tamanhoimagens+80*3, image=self.green),
                    'b':self.canvas.create_image(1000, tamanhoimagens+80*4, image=self.blue),
                    'p':self.canvas.create_image(1000, tamanhoimagens+80*5, image=self.purple)
                   }

        self.ids = {valor:key for key,valor in self.painel_cores.items()}
        self.cores = {'r':self.red, 'o':self.orange, 'y':self.yellow,
                      'g':self.green, 'b':self.blue, 'p':self.purple}
        self.jogadas = ['']
        self.status = tk.Label(self.parent)
        self.status.pack()

        self.canvas.bind('<1>', self.check) #click de mouse abre funcao check
        #control + n: atalho para refazer jogo
        self.parent.bind('<Control-n>', self.desenhaTabuleiro)
        self.parent.bind('<Control-N>', self.desenhaTabuleiro)
        self.padrao = [random.choice('roygbp') for _ in range(4)]
        self.contados = collections.Counter(self.padrao)

    #parte mais IMPORTANTE a de checagem de pecas bancas e pretas
    def checa_jogada(self,resp,jog):
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

    def check(self, event=None):
        id = self.canvas.find_withtag("current")[0]
        jogada = self.ids[id]
        self.jogadas[-1] += jogada
        #carrega posicao x e y de pino no tabuleiro
        x_offset = (len(self.jogadas) - 1) * 80 + 40     #posicao inicial x
        y_offset = (len(self.jogadas[-1]) - 1) * 80 + 40 #posicao inicial y
        self.canvas.create_image(x_offset, y_offset,
                                 image=self.cores[jogada])#imprime pino
        if len(self.jogadas[-1]) < 4:
            return
        
        certos, quase = self.checa_jogada(self.padrao,self.jogadas)
        print(certos, quase)

                        #PINOS PRETOS E BRANCOS
        contadorjogada = collections.Counter(self.jogadas[-1])
        proximos = sum(min(self.contados[k], contadorjogada[k]) for k in self.contados)
        exatos = sum(a==b for a,b in zip(self.padrao, self.jogadas[-1]))
        proximos -= exatos
        cores = exatos*[self.black] + proximos*[self.white]
        coordenadas = [(x_offset-20, 340),#coluna 1
                       (x_offset-20, 380),
                       (x_offset+20, 340),#coluna 2
                       (x_offset+20, 380)]

        #imprime pretas e brancas na tela
        for cor, coord in zip(cores, coordenadas):            
            self.canvas.create_image(coord, image=cor)
     
        if exatos == 4:
            self.status.config(text='Voce Venceu! :D')
            self.canvas.unbind('<1>')
        elif len(self.jogadas) > 11:
            self.status.config(
                               text='Acabaram as tentativas. A resposta correta {}.'.format(
                                ''.join(self.padrao)))
            self.canvas.unbind('<1>')
        else:
            self.jogadas.append('')
#main        
root = tk.Tk()
root.title(string='Mastermind')
jogo = Mastermind(root)
root.mainloop()
