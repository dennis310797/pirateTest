import random
import qryUf as qr

list_uf = ['RO','AC','AM','RR','PA','AP','TO','MA','PI','CE','RN','PB','PE','AL','SE','BA','MG','ES','RJ','SP','PR','SC','RS','MS','MT','GO','DF']
size_uf=len(list_uf)
random.shuffle(list_uf)

repeat=True
while repeat:
    number_uf=int(input("Digite a quantidade de estados que deseja consultar: "))
    if number_uf > size_uf:
        print("VALOR INVALIDO! DIGITE UM VALOR EXISTENTE! \nDIGITE UM VALOR MENOR OU IGUAL A 27\n\n")
    else:
        print(f"Você escolheu {number_uf}")
        repeat=False
        
for i in range(0, number_uf):
    item=list_uf[i]
    resp=qr.finder(item)
    print(resp)
    
    #print(f'minha lista {list_uf[i]}')