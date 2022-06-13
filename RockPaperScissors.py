import random

valid_moves = ['rock', 'paper', 'scissor']

"""The Player class is the parent class for all of the Players
in this game"""
class Player():
    """TThe starter Player class always plays 'rock'."""
    def __init__(self):
        """Start the Player instance."""
        self.score = 0

    def play(self):
        """Return the player move in a string which is always rock)."""
        return valid_moves[0]

    def learn(self, last_counterpart_move):
        """Provide subclasses to save the movement made by the counterpart's movement in the last session with a string.
        This is an empty implementation as the class will noy use the information.
        Args:
            last_counterpart_move (string): counterpart's movement in the last session
        """
        pass


class RandomPlayer(Player):
    """Random player subclass choses its movement randomly."""
    def play(self):
        """Randomly return the movement of the player in a string."""
        index = random.randint(0, 2)
        return valid_moves[index]


class ReflectPlayer(Player):
    """
        Reflect player class that remembers what move the counterpart played last round, and plays that move this round. (In other words, if you play 'paper' on the first round, a ReflectPlayer will play 'paper' on the second round.)
    """
    def __init__(self):
        """Begin a ReflectPlayer instance."""
        Player.__init__(self)
        self.last_counterpart_move = None

    def play(self):
        """Return last counterpart's movement in a string (last counterpart move)."""
        if self.last_counterpart_move is None:
            return Player.play(self)
        return self.last_counterpart_move

    def learn(self, last_counterpartt_move):
        """Save the movement made by the counterpart's movement in the last session
        Args:
            last_counterpart_move (string): counterpart's movement in the last session
        """
        self.last_counterpart_move = last_counterpart_move


class CyclePlayer(Player):
    """
        Cycle player classclass that remembers what move it played last round, and cycles through the different moves. (If it played 'rock' this round, it should play 'paper' in the next round.)
    """
    def __init__(self):
        """Begin a CyclePlayer instance."""
        Player.__init__(self)
        self.last_move = None

    def play(self):
        """Return CyclePlayer movement in a string."""
        move = None
        if self.last_move is None:
            move = Player.play(self)
        else:
            index = valid_moves.index(self.last_move) + 1
            if index >= len(valid_moves):
                index = 0
            move = valid_moves[index]
        self.last_move = move
        return move


class HumanPlayer(Player):
    """HumanPlayer subclass, whose move method asks the human user what move to make."""
    def play(self):
        """Ask HumanPlayer of the movement and return it in a string."""
        player_move = input('Enter your move (' +
                            ', '.join(valid_moves) + '):\n')
        while player_move not in valid_moves:
            player_move = input('Invalid move, try again\n')
        return player_move


class Game():
    """Game class involves player playing a match or a single round of Rock, Paper or Scissor and displays the outcome of each round, and keeps score for both players.."""
    def __init__(self):
        """Initialize a Game instance."""
        self.player1 = HumanPlayer()
        self.player2 = CyclePlayer()

    def play_match(self):
        """Start a game, display message at the start of the game and display the
        final score at the end of the game."""
        input('Let\'s play Rock, Paper or Scissors!' +
              '\nPress enter to play\n')
        try:
            while True:
                self.play_round()
                print('The score is: ' + str(self.player1.score) + ' x ' +
                      str(self.player2.score) + '\n')
                input('Press enter to play again or ctrl+C to quit\n')
        except KeyboardInterrupt:
            print('\n\nThanks for playing!')
            if self.player1.score > self.player2.score:
                print('Player 1 beats Player 2!')
            elif self.player1.score > self.player2.score:
                print('Player 2 beats Player 1!')
            else:
                print('The game was a draw!')
            print('The final score was ' + str(self.player1.score) + ' x ' +
                  str(self.player2.score))

    def play_round(self):
        """Play a round, display the final score at the end of the game."""
        player1_move = self.player1.play()
        player2_move = self.player2.play()
        result = Game.check_result(player1_move, player2_move)

        self.player1.learn(player2_move)
        self.player2.learn(player1_move)

        print('Player 1 choose "' + player1_move + '" and player 2 choose "' +
              player2_move + '"')
        if result == 1:
            self.player1.score += 1
            print('=> Player 1 beats Player 2!\n')
        elif result == 2:
            self.player2.score += 1
            print('=> Player 2 beats Player 1!\n')
        else:
            print('=> Draw!\n')

    @classmethod
    def check_result(cls, move1, move2):
        """Check the result of a round.
        Args:
            move1 (string): Player 1 move.
            move2 (string): Player 2 move.
        Returns:
            1 if player 1 beats player 2, 2 if player 2 beats player 1 or 0 on a draw.
        """
        if Game.is_move_stronger(move1, move2):
            return 1
        elif Game.is_move_stronger(move2, move1):
            return 2
        else:
            return 0

    @classmethod
    def is_move_stronger(cls, move1, move2):
        """Check if the first move is stronger then the second.
        Args:
            move1 (string): Player 1 move.
            move2 (string): Player 2 move.
        Returns:
            True if move1 is stronger, False otherwise.
        """
        if (move1 == 'rock' and move2 == 'scissor'):
            return True
        elif (move1 == 'scissor' and move2 == 'paper'):
            return True
        elif (move1 == 'paper' and move2 == 'rock'):
            return True
        return False


# Ne entry: create a new Game  and start a new match.
game = Game()
game.play_match()
