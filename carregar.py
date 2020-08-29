import time
import sys
def barra(x,tamanho):
    tam = tamanho

    # setup toolbar
    sys.stdout.write("")
    sys.stdout.flush()

    for i in range(tam):
        time.sleep(0.1) # do real work here
        # update the bar
        sys.stdout.write(x)
        sys.stdout.flush()

    sys.stdout.write("") # this ends the progress bar
arq=open('desenho.txt','r')
texto=arq.read()+'\n@stefan.luks'
for i in texto:
    barra(i,1)
