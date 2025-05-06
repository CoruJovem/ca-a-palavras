import random

emoções = ["feliz", "triste", "bravo", "surpreso", "medo", "nojo"]
emoção_secreta = random.choice(emoções)
tentativas = 3

print("=== Jogo de Adivinhar Emoções ===")
print("Emoções possíveis:", ", ".join(emoções))
print(f"Você tem {tentativas} tentativas para adivinhar!")

while tentativas > 0:
    palpite = input("Qual é a emoção? ").strip().lower()
    
    if palpite == emoção_secreta:
        print("Parabéns! Você acertou! 😊")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Errado! Tente novamente. Tentativas restantes: {tentativas}")
        else:
            print(f"Você perdeu! A emoção era: {emoção_secreta}")

print("Fim do jogo!")