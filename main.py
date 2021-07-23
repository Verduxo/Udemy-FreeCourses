import requests
from bs4 import BeautifulSoup
from progress.bar import IncrementalBar
import math

colors={
    'V':'\033[0;40;32m',
    'X':'\u001B[0m'
}
def colorText(text):
    for color in colors:
        text = text.replace("[[" + color + "]]", colors[color])
    return text

def banner():
    banner = '''
[[V]]
    $$\   $$\ $$$$$$$\  $$$$$$$$\ $$\      $$\ $$\     $$\        $$$$$$\   $$$$$$\  
    $$ |  $$ |$$  __$$\ $$  _____|$$$\    $$$ |\$$\   $$  |      $$  __$$\ $$  __$$\ 
    $$ |  $$ |$$ |  $$ |$$ |      $$$$\  $$$$ | \$$\ $$  /       $$ /  \__|$$ /  \__|
    $$ |  $$ |$$ |  $$ |$$$$$\    $$\$$\$$ $$ |  \$$$$  /        $$$$\     $$ |      
    $$ |  $$ |$$ |  $$ |$$  __|   $$ \$$$  $$ |   \$$  /         $$  _|    $$ |      
    $$ |  $$ |$$ |  $$ |$$ |      $$ |\$  /$$ |    $$ |          $$ |      $$ |  $$\ 
    \$$$$$$  |$$$$$$$  |$$$$$$$$\ $$ | \_/ $$ |    $$ |          $$ |      \$$$$$$  |
     \______/ \_______/ \________|\__|     \__|    \__|          \__|       \______/ 
[[X]]                                                                                   

                             hecho por [[V]]verduxo[[X]], con amor
              créditos a [[V]]tt-viic[[X]] por la inspiración(su github en el read.me)
                                                                                                            
''' 

    print(colorText(banner))
banner()
f = open('resultados.txt','a',encoding='utf-8')

contador = 1
try:
    total_paginas= int(input(''' (recomiendo no poner más de 5 páginas porque los cursos no son gratis infinitamente)
                        ¿cuántas páginas desea comprobar?[default=2]      
                        > '''))

except TypeError:
    total_paginas = 2

except ValueError:
    total_paginas = 2
    


    #pb = ProgressBar("Doing stuff on collection", total_paginas)

bar1 = IncrementalBar(colorText('[[V]]Procesando:'), max=total_paginas)

while contador < total_paginas+1:
        
    url = 'https://smartybro.com/category/udemy-coupon-100-off/page/'+str(contador)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    bar1.next()    
    for a in soup.find_all('a', href=True):
        if a['href'].startswith('https://smartybro.com/2021/'):
            if  not (a.text).startswith('['):
                if not (a.text).startswith('More'):
                    f.write('\n'+a.text)
                    f.write("URL:"+ a['href']+'\n')


    contador += 1
        
        
bar1.finish()

print(colorText('[[X]]cursos guardados en el archivo [[V]]resultados.txt[[X]] satisfactoriamente :)'))



