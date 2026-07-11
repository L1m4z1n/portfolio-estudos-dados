pop_A = 80000
pop_B = 200000
tempo = 0
while pop_A < pop_B:
    pop_A *= 1.03
    pop_B *= 1.015
    tempo += 1

print(f"Será necessário {tempo} anos, para a população A igualar a população B")