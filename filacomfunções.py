def inserirNaFila(nums):
    while True:
        num = int(input('Digite um numero inteiro'))
        nums.append(num)
        res2 = str(input('Quer continuar s/n'))
        if res2 in 'Nn':
            break
def printarNaFila (nums):
    for c, num in enumerate(nums):
        print(f'na posição {c} o numero é {num}')
def removerNaFila (nums):
    res3 = ""
    while True:
        if len(nums) <= 1:
            print('Voce n pode remover pq a lista é mt pequena')
            return nums
        else:
            nums = nums[1:]
        res3 = str(input('Voce deseja remover novamente?'))
        if res3 in 'Nn':
            return nums
def main():
    nums = []
    res2 = ""
    while True:
        res = str(input('Digite i para inserir p para printar r para remover e s para sair'))
        if res == 'i':
            inserirNaFila(nums)
        elif res == 'p':
            printarNaFila(nums)
        elif res == 'r':
            nums=removerNaFila(nums)
        elif res == 's':
            break
        else:
            print('Voce inseriu um valor invalido')
    print('Acabou')

if __name__ == "__main__":
    main()