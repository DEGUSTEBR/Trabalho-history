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

res = input('escolha uma resposta: ')

res = ""

while res not in ["1", "2", "3"]:
    res = input("Escolha uma opção (1, 2 ou 3): ")

print("Opção válida escolhida:", res)

if res == '1':
    Espada = not Espada
    print('A espada? uhhh bom não é exatamente uma espada está mais para um cabo de vassoura sem a cabeça;')
    input(' ')
    print('Se bem que uma vassoura tem um formato similar, não é o ideal para um grande cavaleiro mas deve servir')
    input(' ')
    print('Ahen continuando com sua ehhh ')
    input(' ')
    print('SEU item ele desse as escadas para o dia em que me foi prometido ver um cavaleiro')
    input(' ')
    print('Descendo as escadas conseguimos ver o nosso cavaleiro')
    input(' ')
    print(' Se preparando para o grande dia em que ele se tornara um cavaleiro ')
    input(' ')
    print('E para isso ele deverá completar a ultima tarefa designadapelo campo de treinamento para cavaleiros iniciantes ')
    input(' ')
    print('e com tudoarrumado lá se vai ele até o centro do mercado onde o seu destino ')
    input(' ')
    print('E para mostrar ao mundo a sua grandiosa história de como ele se tornou um cavaleiro')
    input(' ')
    


elif res == '2':
    Armadura = not Armadura
    print('A armadura? hmm Glenn meu querido isso está mais para pano de chão em comparação ')
    input(' ')
    print(' “Glenn resmunga claramente irritado com ocomentário” ')
    input(' ')
    print('oh perdão eu não queria ofender a UNICA peça de roupa que você tem disponível')
    input(' ')
    print('“Glenn ainda mais irritado joga a roupa no chãodemonstrando sua ira”')
    input(' ')
    print('está bem está bem eu não falo mais sobre uhh isso')
    input(' ')
    print('Então que tal descermos as escadas depois de você se trocar?')
    input('')
    print('temos um longo dia pela frente afinal ')
    input('')
    print('“em concordância os dois dessem asescadas”')
    input('')
   

elif res == '3':
    Cama = not Cama
    print('E então ele se levanta da cama e, ... , e , ... , Glenn? , ... , Glenn?! , ...suspira* Glenn já passou da hora de acordar, ... , levante-se Glenn temosaté o meio dia para a profecia se cumprir, ... , suspira* eu acho queninguém vai comer esta deliciosa batata doc-, “Antes do narradorterminar de falar a cama se revira e se debate e num piscar de olhos  Glenn se arrumou e desceu as escadas para a sala de jantar derrubandotudo pela frente” , meu deus , “exclama o narrador” , bom pelo menosele levantou da cama agora o problema é conseguir a batata que eumenti sobre;')
    input(' ')
    print('Descendo as escadas conseguimos ver o nosso cavaleiro')
    input(' ')
    print('futuro cavaleiro?, ... , Glenn cadê você? , ... BAM, oh não esse barulho veio da cozinha ele ainda está achando que eu tinha preparado uma batata doce para ele, “o narrador começa a andar em círculos” , e agora e agora como eu pude mentir para ele sobre a comida favorita dele, “e então com um estalar de dedos” , é isso como eu não percebi isso antes OH GLENN !!, “ao som do chamado, Glenn aparece igual a um cachorro procurando por comida” , Glenn infelismente a batata não está aqui , “desapontado ele vai para as escada com o intuito de voltar paracama” , MAS ESPERE eu não menti para você , certamente ela não estáaqui porem ela vai está no centro do mercado e nos temos queconquistar o que é seu por destino, “animado pela batata ele sai embusca do item” , espere por mim, “vai o narrador atras de Glenn”;')
    

else:
    print('Escolha invalida digite 1,2 ou 3')

print('Descendo as escadas conseguimos ver o nosso cavaleiro')

if Espada == False:
    print('Funcionou')

elif Armadura == False:
    print('Armadura')
    input('')

elif Cama == False:
    print('vai dormir')
    input('')



print('Fim do prologo')
    




    


