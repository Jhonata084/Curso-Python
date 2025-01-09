largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura
print('A sua parede tem a dimensão de {}x{} e sua área é de {:.1f}m²'.format(largura, altura, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {:.1f}l de tinta'.format(tinta))