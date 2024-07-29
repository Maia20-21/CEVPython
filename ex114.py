import urllib
import urllib.request

print(f'{' MEU GITHUB ':-^45}')
try:
    site = urllib.request.urlopen('https://github.com/Maia20-21')
except:
    print('''O site não está acessível no momento.
Tente novamente mais tarde.''')
else:
    print(f'''O site está acessível no momento.
Que tal dar uma olhada nos meus outros projetos no GitHub?''')