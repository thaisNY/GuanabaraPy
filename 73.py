campeoes = ('Palmeiras','Cruzeiro','Grêmio','Santos','Corintias','Flamengo','Atlético Mineiro','Atlético Paranaense',
            'Internacional','Chapecoense','Botafogo','São Paulo','Fluminense','Vasco da Gama','Bahia',
            'Sport','Vitória','Ponta Preta','America','Coritiba')
print(campeoes[: 5])
print(campeoes[16:])
print(sorted(campeoes))
pos = campeoes.index('Chapecoense')
print(f'A posição do Chapecoense foi {pos + 1} lugar')