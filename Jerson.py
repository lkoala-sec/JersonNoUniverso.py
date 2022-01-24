from random import *

name = 'Jerson'

# name = input(
    
#     '\n Digite o Nick desejado \033[36m[Digite 1 para o Nick default]: '
#     )

# if name == '1':

#     name = default_name

#     print(
#         '|'
#         )

#     print(
#     f'\033[32m Seu Nick foi definido para "{name}"'
#     )

# else:
    
#     print(
#         '|'
#         )
    
#     print(
#     f'\033[32m Seu Nick foi definido para "{name}"'
#     )


print(
    f'''
    
    \033[36mSeja bem vindo ao nosso universo {name}! Neste universo nós temos 5 galáxias que você pode escolher viver já que você é apenas um Humano \n
    temos as seguintes galáxias:
    
    \033[32m[1] Via láctea -- ก(^≗ω≗^)ค

    \033[32m[2] Andromeda -- ก₍⸍⸌̣ʷ̣̫⸍̣⸌₎ค

    \033[33m[3] Gazorpian -- /ᐠ ̥  ̮  ̥ ᐟ\ฅ

    \033[33m[4] Valerian -- ฅ/ᐠ. ̫ .ᐟ\ฅ

    \033[31m[5] Hypoklis -- ฅ/ᐠ•ω•ᐟ\ฅ

    \033[36m
    Cada galáxia tem um nível de dificuldade para Seres Humano como você

    \033[32mAs galáxias com a cor verde são as mais fáceis
    \033[33mAs de coloração amarela são de dificuldade mediana
    \033[31mAs de vermelho são as mais difíceis!

    \033[36m
    A galáxia que você escolher, o respectivo gato ao lado do nome lhe apresentará detalhe por detalhe!
    
    ''')

choice1 = int(
    
    input('Digite o número da galáxia que você deseja viver: ')
    
    )

while choice1 not in range(1, 6):

    print('''
    
    \033[31m Desculpe, não entendi sua escolha!
    
    ''')

    choice1 = int(
        
        input('Digite o número da galáxia que você deseja viver: ')
        
        )

else:

   if choice1 == 1:
    
        home = 'Via láctea'

        cat = 'ก(^≗ω≗^)ค'

        print(
        
        f'''\n\n\033[32mVocê escolheu a galáxia {home}, ótima escolha!

        \033[36m
        O gato que o acompanhara nesta jornada será este --> \033[32m{cat} !!!

        ''')

   elif choice1 == 2:

        home = 'Andromeda'

        cat = 'ก₍⸍⸌̣ʷ̣̫⸍̣⸌₎ค'

        print(
        
        f'''\n\n\033[32mVocê escolheu a galáxia {home}, ótima escolha!

        \033[36m
        O gato que o acompanhara nesta jornada será este --> \033[32m{cat} !!!

        ''')

   elif choice1 == 3:

        home = 'Gazorpian'

        cat = '/ᐠ ̥  ̮  ̥ ᐟ\ฅ'

        print(
        
        f'''\n\n\033[32mVocê escolheu a galáxia \033[33m{home}\033[32m, ótima escolha!

        \033[36m
        O gato que o acompanhara nesta jornada será este --> \033[33m{cat} !!!

        ''')

   elif choice1 == 4:

        home = 'Valerian'

        cat = 'ฅ/ᐠ. ̫ .ᐟ\ฅ'

        print(
        
        f'''\n\n\033[32mVocê escolheu a galáxia \033[33m{home}\033[32m, ótima escolha!

        \033[36m
        O gato que o acompanhara nesta jornada será este --> \033[33m{cat} !!!

        ''')

   elif choice1 == 5:


    home = 'Hypoklis'

    cat = 'ฅ/ᐠ•ω•ᐟ\ฅ'

    print(
        
        f'''\n\n\033[32mVocê escolheu a galáxia \033[31m{home}\033[32m, ótima escolha!

        \033[36m
        O gato que o acompanhara nesta jornada será este --> \033[31m{cat} !!!

        ''')
