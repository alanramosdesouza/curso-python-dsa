print('-' * 70)
print('--- Jogo Pedra, papel e tesoura (2 jogadores) ---')
print('*' * 70)

print('Bem vindos! Cada jogador deve escolher uma das opcçoes.')
print('*' * 70)

jogador1 = input('Jogador 1 escolha uma opção: ').strip().lower()
jogador2 = input('Jogador 2 escolha uma opção: ').strip().lower()

print('-' * 70)

# mapeamento do que vence o quê
vence = {
    'pedra': 'tesoura',
    'papel': 'pedra',
    'tesoura': 'papel'
}

if jogador1 == jogador2:
    print('Empate')
elif vence.get(jogador1) == jogador2:
    print(f'Vitória do jogador 1 que escolheu {jogador1}.')
elif vence.get(jogador2) == jogador1:
    print(f'Vitória do jogador 2 que escolheu {jogador2}.')
else:
    print('Entrada inválida')

print('-' * 70)