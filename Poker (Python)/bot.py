import random
from player import Player

class Bot(Player):

    def make_move(self, current_max, player_action):
    
        # Avaliando a mão do bot
        ranks = [card.rank for card in self.hand]
        if len(ranks) != len(set(ranks)):
            hand_strength = 2  # par ou melhor
        else:
            hand_strength = 0  # nada

        # Ajusta chance de blefe dependendo da ação do jogador
        bluff_chance = 0.0
        if hand_strength == 0:
            if player_action == "check":
                bluff_chance = 0.3  # mais chance de blefar se jogador passou
            elif player_action == "raise":
                bluff_chance = 0.1  # menos chance de blefar se jogador apostou
        elif hand_strength == 2:
            bluff_chance = 0.05  # quase não blefa com mão boa

        # Decide ação
        if hand_strength >= 2:
            # mão boa → aposta agressiva
            action = random.choices(["call", "raise"], weights=[0.3, 0.7])[0]
        else:
            # mão fraca → decide blefe
            if random.random() < bluff_chance:
                action = "raise"
            else:
                # se tem aposta alta, pode foldar ou dar call
                if current_max > self.current_bet:
                    action = random.choices(["call", "fold"], weights=[0.5, 0.5])[0]
                else:
                    action = "check"

        # Executa ação
        if action == "check":
            print(f"{self.name} deu check")
            return 0, action

        elif action == "call":
            amount = current_max - self.current_bet
            if amount > self.balance:
                amount = self.balance
            self.balance -= amount
            self.current_bet += amount
            print(f"{self.name} deu call de R${amount}")
            return amount, action

        elif action == "raise":
            raise_amount = random.randint(1, self.balance)
            total = (current_max - self.current_bet) + raise_amount
            if total > self.balance:
                total = self.balance
            self.balance -= total
            self.current_bet += total
            print(f"{self.name} deu raise de R${total} (pode estar blefando!)")
            return total, action

        elif action == "fold":
            print(f"{self.name} desistiu da rodada")
            return 0, action