from tkinter import *
import tkinter  as tk
from tkinter import ttk
from datetime import datetime
from time import gmtime
from time import *
import pygame
pygame.mixer.init()
import pyglet
pyglet.font.add_file("digital-7.ttf")

# ____________-> |Cores| <-____________

cor0= "#363636" #Grey/Black
cor1= "#F5FFFA" #MintCream/Quase Branco
cor2= "#00BFFF" #DeepSkyBlue
cor3= "#48D1CC" #MediumTurquoise
cor4= "#32CD32" #LimeGreen
cor5= "#FFFF00" #Yellow

corFundo=cor0
corBase=cor1
# _____________->Base<-________________
t=0
select=0

class baseApp():
    def __init__ (self, win):

        self.tempoRelogio1= tk.Label(win, text="", font=("digital-7 18"), bg=corFundo, fg=cor2)
        self.tempoRelogio1.place(x=380,y=250)

        self.hojeData= tk.Label(win, text="", font=("Arial 10"), bg=corFundo, fg=cor3)
        self.hojeData.place(x=380, y=275)

        self.msn1= tk.Label(text="CONVERTER C.PRIME EM TEMPO!!!", font=("Arial 20"), bg=corFundo, fg=corBase)
        self.msn1.grid(row=0, column=0, sticky=NW, padx=15)

        self.qCarne= tk.Label(text="QUANTAS CARNES: ", font=("Arial 12 bold"), bg=corFundo, fg=cor3)
        self.qCarne.place(x=20, y=50)
        self.entreQCarne= tk.Entry(font=("Arial 12 bold"), fg=cor0)
        self.entreQCarne.place(x=197, y=50)

        self.labelCombobox=tk.Label(text="SELECIONE O DINO: ", font=("Arial 12 bold"), bg=corFundo, fg=cor3)
        self.labelCombobox.place(x=20,y=100)
        self.comboBoxLista=("Managarmr","Gigantossauro","Deinonychos")
        self.comboBox=ttk.Combobox(win, font=("Arial 12 bold"), values=self.comboBoxLista)
        self.comboBox.place(x=197, y=100)

        self.temporestante= tk.Label(win, text="TIME:",font=("digital-7 30 bold"), bg=corFundo, fg=cor5)
        self.temporestante.place(x=20, y=160)

        self.contado= tk.Label(win, text="",font=("digital-7 40"), bg=corFundo, fg=cor5)
        self.contado.place(x=110, y=160)

        self.btStart= tk.Button(win, text="GO!", font=("digital-7 20 bold"), bg=cor1, fg=cor0, command= self.selectDino)
        self.btStart.configure(state=NORMAL, bg= cor4, fg=corBase)
        self.btStart.place(x=320,y=160)

        self.btReset= tk.Button(win, text="STOP!", font=("digital-7 20 bold"), bg=cor1, fg=cor0, command=self.stopAlarme)
        self.btReset.place(x=380,y=160)

        self.relogio()

    def relogio(self):
        tempo= datetime.now()
        hora= tempo.strftime("%H:%M:%S")
        dia_semana= tempo.strftime("%A")
        dia=tempo.day
        mes=tempo.month
        ano=tempo.year

        self.tempoRelogio1.config(text=hora)
        self.tempoRelogio1.after(500, self.relogio)
        self.hojeData.config(text=dia_semana + ": " + str(dia) + "/" + str(mes) + "/" + str(ano))


    def selectDino(self):
        global select
        select=(self.comboBox.get())
        try:
            if select == "Managarmr":
                self.selecao= 41
            elif select == "Gigantossauro":
                self.selecao = 25
            elif select == "Deinonychos":
                self.selecao = 60

        except AttributeError:
            self.tela2= Toplevel()
            self.tela2.title("!!!ERROR!!!")
            self.tela2.geometry('725x100')
            self.tela2.configure(bg=corFundo)
            self.tela2.resizable(width=FALSE, height=FALSE)
            self.tela2.transient(tela)
            self.tela2.focus_force()
            self.tela2.grab_set()
            errorForme= tk.Label(self.tela2,text="### OS DADOS INFORMADOS SÃO INVALIDOS. FAVOR VERIFICAR DAODS INFORMADOS. ### \n {QUANTAS CARNES}: DEVE SER INFORMADO APENAS EM NUMEROS INTEIROS(SEM PONTO OU VIRGULA.) \n {SELECIONE O DINO}: DEVE-SE ESCOLHER UMA DAS OPIÇÕES DISPONIVEIS.", font=("Arial 10 bold"), bg=corFundo , fg=corBase)
            errorForme.grid(row=0, column=0, sticky=NW, padx=15)

            pygame.mixer.music.stop()
        
        except ValueError:
            self.tela2= Toplevel()
            self.tela2.title("!!!ERROR!!!")
            self.tela2.geometry('725x100')
            self.tela2.configure(bg=corFundo)
            self.tela2.resizable(width=FALSE, height=FALSE)
            self.tela2.transient(tela)
            self.tela2.focus_force()
            self.tela2.grab_set()
            errorForme= tk.Label(self.tela2 ,text="### OS DADOS INFORMADOS SÃO INVALIDOS. FAVOR VERIFICAR DAODS INFORMADOS. ### \n {QUANTAS CARNES}: DEVE SER INFORMADO APENAS EM NUMEROS INTEIROS(SEM PONTO OU VIRGULA.) \n {SELECIONE O DINO}: DEVE-SE ESCOLHER UMA DAS OPIÇÕES DISPONIVEIS.", font=("Arial 10 bold"), bg=corFundo , fg=corBase)
            errorForme.grid(row=0, column=0, sticky=NW, padx=15)

            pygame.mixer.music.stop()

        except Exception as erro:
            print('Ocorreu um erro1', erro.__cause__)
            
        else:    
            self.contadoRegressivo()
            
        
    def contadoRegressivo(self):
        try:
            self.stopAlarme()
            self.temposTP=str(self.entreQCarne.get())
            self.segundos=int(self.temposTP)*(self.selecao)
        except Exception:
            self.tela2= Toplevel()
            self.tela2.title("!!!ERROR!!!")
            self.tela2.geometry('725x100')
            self.tela2.configure(bg=corFundo)
            self.tela2.resizable(width=FALSE, height=FALSE)
            self.tela2.transient(tela)
            self.tela2.focus_force()
            self.tela2.grab_set()
            errorForme= tk.Label(self.tela2 ,text="### OS DADOS INFORMADOS SÃO INVALIDOS. FAVOR VERIFICAR DAODS INFORMADOS. ### \n {QUANTAS CARNES}: DEVE SER INFORMADO APENAS EM NUMEROS INTEIROS(SEM PONTO OU VIRGULA.) \n {SELECIONE O DINO}: DEVE-SE ESCOLHER UMA DAS OPIÇÕES DISPONIVEIS.", font=("Arial 10 bold"), bg=corFundo , fg=corBase)
            errorForme.grid(row=0, column=0, sticky=NW, padx=15)

            pygame.mixer.music.stop()
        else:
            global t
            t= int(self.segundos)
            self.regressiva()
            self.btStart.configure(state=DISABLED, bg= cor4, fg=corFundo)
            return t
        
    def regressiva(self):
        global t
        if t>0:
            HMS= strftime("%H:%M:%S", gmtime(t))
            self.contado.config(text=HMS)
            t=t-1
            self.contado.after(1005,self.regressiva)
        elif t==0:
            self.contado.config(text="00:00:00")
            self.alarmeLoad= pygame.mixer.music.load('AlarmeMP3.mp3')
            self.alarmePlay= pygame.mixer.music.play(3)
        elif t== -1:
            print("STOP!")


    def resetTime(self):
        global t
        t=-1
        self.contado.config(text="00:00:00")
        self.stopPlay= pygame.mixer.music.stop()
        self.btStart.configure(state=NORMAL, bg= cor4, fg=corBase)

    def stopAlarme(self):
        self.stopPlay= pygame.mixer.music.stop()
        self.resetTime()

# ____________->Tela.App<-_______________

tela= tk.Tk()
tela.title("TEMPORIZADOR DE COMIDA")
tela.geometry('500x300')
tela.configure(bg=corFundo)
tela.resizable(width=FALSE, height=FALSE)
pricipal= baseApp(tela)

tela.mainloop()
pygame.mixer.music.stop()
# _______________________________________

