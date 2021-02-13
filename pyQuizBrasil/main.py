from turtle import Screen, bgpic
from state import States, Score

screen = Screen()
screen.setup(width=574, height=582)
screen.title('Quiz: Brazil States')
screen.tracer(0)
bgpic('brazil.gif')

player = States()
score = Score()

while score.life > 0:
    if player.asking():
        score.increase_score()
    else:
        score.decrease_life()
    score.update()
    # Checking if you won the game.
    if score.score == 270:
        score.you_won()

player.show_errors()
score.game_over()
screen.exitonclick()
