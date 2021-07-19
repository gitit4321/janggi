# Janggi

This program is a python implementaion of the board game Janggi, otherwise known as Korean chess. The game engine, which originally utilized a command line based interface, was built as a portfolio project for CS162 at Oregon State University. I then chose to build out a graphic user interface in order to provide an easier way for users to interact with the project. 

## Rules
The pieces are octagonal in shape, vary in size, are placed on the intersections of lines, and are arranged symmetrically. Each side of the board has a nine-point fortress, marked by an “X” of diagonal lines. The General (or King) begins in the center of the fortress. 

The two sides (Red and Blue) alternate, moving one piece in each turn, in an attempt to force the capture of the enemy General (King), just as in other forms of chess. When a General is left with no option but to be captured in the next move, they are in checkmate, and have lost the game.

All pieces capture by landing on a point occupied by an enemy piece, using their normal movement (discussed below) to arrive at that location. The enemy piece is removed from play for the rest of the game.

## Piece Movement
A brief description of each pieces movement can be found below.

### General (King)
The general must stay within the nine-point fortess. It moves one point along any printed line in the fortress. Note that it moves diagonally only along the printed lines.
![general movement](https://ancientchess.com/graphics-rules/janggi_korean_chess_king_general-move.jpg)

### Counselor (Queen)
Moves exactly the same as the General, and is also confined to the fortress.
![Counselor movement](https://ancientchess.com/graphics-rules/janggi_korean_chess_queen_guard-move.jpg)

### Horse (Knight)
May move one point forward, backward, left or right plus one point outward diagonally, as shown in the image below. This is similar to the western knight, but the Korean knight can be blocked. Note that in the image the knight cannot move to the red marked points, because it is blocked by the pawn on its right. (It is not blocked by the pawn on his left.)
![horse movement](https://ancientchess.com/graphics-rules/janggi_korean_chess_knight_horse-move.jpg)

### Elephant (Bishop)
Note that this piece has a very unusual move found only in Korean chess. It starts one point forward, backward, left or right, and then moves two points outward diagonally, like an extended knight’s move. It can be blocked anywhere along this path, as it is in the diagram by the green cannon, and by the red chariot.

![elephant movement](https://ancientchess.com/graphics-rules/janggi_korean_chess_bishop_elephant-move.jpg)

### Chariot (Rook)
This piece may move as many points as it wishes, in a straight line, along the lines of the board. This is the same move as the western rook, but note that the Korean rook can also move along the diagonal lines in the fortress, if it is already on one of these points. It can not jump over pieces (such as the red counselor in the diagram), and it captures as it moves (and so, can capture the green piece at his right).

![chariot movement](https://ancientchess.com/graphics-rules/janggi_korean_chess_chariot_rook-move.jpg)

### Soldier (Pawn)
This piece may more one point either forward or sideways as seen below.![soldier movement](https://ancientchess.com/graphics-rules/janggi_korean_chess_pawn-move.jpg)

However, within the fortress, the pawn may also move forward along the printed diagonal lines. The image shows the green pawn, with its increased power of move, approaching the enemy general.
![soldier movement](https://ancientchess.com/graphics-rules/janggi_korean_chess_pawn2-move.jpg)

### A general note about piece movement:
While playing the game, upon clicking a game piece you will see what moves are available to you, represented by small green circles. This is an aid to assist with piece movement. 
