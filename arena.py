from agents.mcts import Node

class Arena(object):

    def __init__(self, game, champion, challenger):
        self.champion = champion
        self.challenger = challenger
        self.game = game

    def fight(self, n_games):
        wins = 0
        losses = 0

        for i in range(n_games):
            game_clone = self.game.clone()
            is_done = False
            winner = 0
            root = Node()

            while not is_done:
                if i % 2 == 0:  # champion playes as X, challenger player as 0
                    if game_clone.current_player == 1:
                        best_child = self.champion.search(game, root, temperature=0.0001) # very little exploration
                    else:
                        best_child = self.challenger.search(game, root, temperature=0.0001) # very little exploration
                else:           # challenger playes as X, champion player as 0
                    if game_clone.current_player == 1:
                        best_child = self.challenger.search(game, root, temperature=0.0001) # very little exploration
                    else:
                        best_child = self.champion.search(game, root, temperature=0.0001) # very little exploration


                action = best_child.action
                _, _, is_done = game.step(action)


                # best_child is now a root
                best_child.parent = None
                root = best_child

            winner = game.winner
            if i % 2 == 0:
                if winner == -1:
                    wins += 1
                elif winner == 1:
                    losses += 1
            else:
                if winner == 1:
                    wins += 1
                elif winner == -1:
                    losses += 1


        print('Wins:', wins, 'Losses:', losses)
        return wins / n_games
