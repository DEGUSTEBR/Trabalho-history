Espada = True
Armadura = True
Cama = True

print('PROLOGO')
input('precione enter para proceguir')
print('Esta é a historia de um dos maiores cavaleiros que já ousou pisar na terra de ALGUM LUGAR DISTANTE')
input(' ')
print('Pois oa raiar do sol no seu ponto mais alto do dia GLEM (Nosso Protagonitsa) se tornara um cavaleiro, então a hora vem e ele pega')
input(' ')

print('1) Espada')
print('2) Armadura')
print('3) Cama')

res = ""

while res not in ["1", "2", "3"]:
    res = input("Escolha uma opção (1, 2 ou 3): ")

print("Opção válida escolhida:", res)

if res == '1':
    Espada = not Espada
    print('A espada? uhhh bom não é exatamente uma espada está mais para um cabo de vassoura sem a cabeça;')
    input(' ')
    print('Se bem que uma vassoura tem um formato similar' )
    input('')
    print(' não é o ideal para um grande cavaleiro mas deve servir')
    input(' ')
    print('Ahen continuando com seu ehhh ')
    input(' ')
    print('item')
    input(' ')
    print('Então ele desce as escadas para o dia em que me foi prometido ver um cavaleiro')
    input(' ')

    


elif res == '2':
    Armadura = not Armadura
    print('A armadura? Hmm, Glenn, meu querido, isso está mais para pano de chão, em comparação ')
    input(' ')
    print(' “Glenn resmunga claramente irritado com ocomentário” ')
    input(' ')
    print('Oh me desculpe, eu não queria ofender a UNICA peça de roupa que você tem disponível')
    input(' ')
    print('“Glenn, ainda mais irritado, joga a roupa no chão, demonstrando sua ira ”')
    input(' ')
    print('Está bem. Eu não falo mais sobre… uhh… isso ')
    input(' ')
    print('Então que tal descermos as escadas depois de você se trocar?')
    input('')
    print('Afinal, temos um longo dia pela frente ')
    input('')
    print('“Em concordância, ambos concordaram em descer as escadas ”')
    input('')
   

elif res == '3':
    Cama = not Cama
    print('E então ele se levanta da cama e' )
    input(' ')
    print(' ...  ')
    input(' ')
    print('e então ')
    input(' ')
    print(' ... ')
    input(' ')
    print(' Glenn?')
    input(' ')
    print(' ... ')
    input(' ')
    print(' Glenn?!')
    input(' ')
    print('...')
    input(' ')
    print(' ...suspira* Glenn já passou da hora de acordar ')
    input(' ')
    print(' ... ')
    input(' ')
    print(' levante-se Glenn temos até o meio dia para a profecia se cumprir')
    input(' ')
    print(' ... ')
    input(' ')
    print(' suspira* eu acho queninguém vai comer esta deliciosa batata doc-')
    input(' ')
    print(' "Antes do narrador terminar de falar, a cama se revira e se debate e num piscar de olhos" ')
    input(' ')
    print(' "Glenn se arrumou e desceu as escadas para a sala de jantar, derrubando tudo que estava  frente"')
    input(' ')
    print(' meu deus ')
    input(' ')
    print(' "exclama o narrador" ')
    input(' ')
    print(' bom pelo menos ele se levantou da cama agora o problema é conseguir a batata que eu menti sobre')
    input(' ')
    print('Vamos pensar sobre isso no caminho')
    input(' ')

    

else:
    print('Escolha invalida digite 1,2 ou 3')
    input(' ')

print('Descendo as escadas conseguimos ver o nosso cavaleiro')
input(' ')

if Espada == False:
    print('Funcionou')
    input(' ')

elif Armadura == False:
    print('Armadura')
    input('')

elif Cama == False:
    print('vai dormir Bruno')
    input(' ')



print('Fim do prologo')
input(' ')
    




    


