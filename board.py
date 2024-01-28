from settings import *


class Board():
    def __init__(self):
        self.board =   [[0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 2, 1, 0, 0, 0],
                        [0, 0, 0, 1, 2, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0]]
        self.blackTurn = True
        self.mosPos = pygame.mouse.get_pos()
        self.flipPiece = []
        self.count = 0

    def displayBoard(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                pygame.draw.rect(screen,"#27ae60",pygame.Rect(MARGINSIZE + TILESIZE * c,MARGINSIZE + TILESIZE * r,TILESIZE,TILESIZE))
                # pygame.draw.rect(screen, "#6ab04c",pygame.Rect(MARGINSIZE + TILESIZE * c, MARGINSIZE + TILESIZE * r, TILESIZE, TILESIZE))

    def drawPieces(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 1:
                    pygame.draw.circle(screen,"Black",(MARGINSIZE + TILESIZE * c + TILESIZE // 2, MARGINSIZE + TILESIZE * r + TILESIZE // 2),TILESIZE // 2 - 3)
                elif self.board[r][c] == 2:
                    pygame.draw.circle(screen,"White",(MARGINSIZE + TILESIZE * c + TILESIZE // 2, MARGINSIZE + TILESIZE * r + TILESIZE // 2),TILESIZE // 2 - 3)

    # 6ab04c "#27ae60"
    def drawLines(self):
        for i in range(9):
            if i % 8 == 0:
                pygame.draw.line(screen, "Black", (MARGINSIZE + TILESIZE * i, MARGINSIZE),
                                 (MARGINSIZE + TILESIZE * i, HEIGHT - MARGINSIZE), 15)
                pygame.draw.line(screen, "Black", (MARGINSIZE, MARGINSIZE + TILESIZE * i),
                                 (WIDTH - MARGINSIZE, MARGINSIZE + TILESIZE * i), 15)
            else:
                pygame.draw.line(screen,"Black",(MARGINSIZE + TILESIZE * i,MARGINSIZE),(MARGINSIZE + TILESIZE * i,HEIGHT - MARGINSIZE),5)
                pygame.draw.line(screen, "Black", (MARGINSIZE, MARGINSIZE + TILESIZE * i),(WIDTH - MARGINSIZE, MARGINSIZE + TILESIZE * i),5)

    def displayTurn(self):
        if self.blackTurn:
            turnFont = font.render("Black Turn", True, "Black")
            turnFontRect = turnFont.get_rect()
            turnFontRect.center = (WIDTH // 2, HEIGHT - TILESIZE //2)
            screen.blit(turnFont,turnFontRect)
        elif not self.blackTurn:
            turnFont = font.render("White Turn", True, "White")
            turnFontRect = turnFont.get_rect()
            turnFontRect.center = (WIDTH // 2, HEIGHT - TILESIZE // 2)
            screen.blit(turnFont, turnFontRect)

    def drawPossibleMove(self):
        self.mosPos = pygame.mouse.get_pos()
        if MARGINSIZE < self.mosPos[0] < WIDTH - MARGINSIZE and MARGINSIZE < self.mosPos[1] < HEIGHT - MARGINSIZE:
            if self.board[(self.mosPos[1] - MARGINSIZE) // TILESIZE][(self.mosPos[0] - MARGINSIZE) // TILESIZE] == 0:
                if self.blackTurn and self.checkValidMove((((self.mosPos[0] - MARGINSIZE) // TILESIZE),(self.mosPos[1] - MARGINSIZE) // TILESIZE),1):
                    pygame.draw.circle(screen, "Black", (TILESIZE * ((self.mosPos[0] - MARGINSIZE) // TILESIZE) + TILESIZE //2 + MARGINSIZE,TILESIZE *((self.mosPos[1] - MARGINSIZE) // TILESIZE) + TILESIZE //2 + MARGINSIZE),TILESIZE // 2 - 3)
                    screen.blit(toumei,(TILESIZE * ((self.mosPos[0] - MARGINSIZE) // TILESIZE) + MARGINSIZE,TILESIZE *((self.mosPos[1] - MARGINSIZE) // TILESIZE)  + MARGINSIZE))
                elif not self.blackTurn and self.checkValidMove((((self.mosPos[0] - MARGINSIZE) // TILESIZE),(self.mosPos[1] - MARGINSIZE) // TILESIZE),2):
                    pygame.draw.circle(screen, "White", (TILESIZE * ((self.mosPos[0] - MARGINSIZE) // TILESIZE) + TILESIZE // 2 + MARGINSIZE,TILESIZE * ((self.mosPos[1] - MARGINSIZE) // TILESIZE) + TILESIZE // 2 + MARGINSIZE),TILESIZE // 2 - 3)
                    screen.blit(toumei, (TILESIZE * ((self.mosPos[0] - MARGINSIZE) // TILESIZE) + MARGINSIZE,TILESIZE * ((self.mosPos[1] - MARGINSIZE) // TILESIZE) + MARGINSIZE))

    def playPiece(self,pos):
        if self.board[pos[1]][pos[0]] == 0:
            if self.blackTurn and self.checkValidMove((((self.mosPos[0] - MARGINSIZE) // TILESIZE),(self.mosPos[1] - MARGINSIZE) // TILESIZE),1):
                self.board[pos[1]][pos[0]] = 1
                self.flipPieces(pos,1)
                self.blackTurn = not self.blackTurn
            elif not self.blackTurn and self.checkValidMove((((self.mosPos[0] - MARGINSIZE) // TILESIZE),(self.mosPos[1] - MARGINSIZE) // TILESIZE),2):
                self.board[pos[1]][pos[0]] = 2
                self.flipPieces(pos, 2)
                self.blackTurn = not self.blackTurn

    def flipPieces(self,pos,turn):

        if turn == 1:
            opponent = 2
        else:
            opponent = 1

        self.flipPiece.clear()

        for i in range(1,(pos[1] + 1)):     #DOWN
            if self.board[pos[1] - i][pos[0]] == 0:
                break
            elif self.board[pos[1] - i][pos[0]] == opponent:
                self.flipPiece.append((pos[1] - i,pos[0]))
            elif self.board[pos[1] - i][pos[0]] == turn:
                for piece in self.flipPiece:
                    self.board[piece[0]][piece[1]] = turn
                break
        self.flipPiece.clear()

        for i in range(1,(8 - pos[1])):      #UP
            if self.board[pos[1] + i][pos[0]] == 0:
                break
            elif self.board[pos[1] + i][pos[0]] == opponent:
                self.flipPiece.append((pos[1] + i,pos[0]))
            elif self.board[pos[1] + i][pos[0]] == turn:
                for piece in self.flipPiece:
                    self.board[piece[0]][piece[1]] = turn
                break
        self.flipPiece.clear()

        for i in range(1,(pos[0] + 1)):     #LEFT
            if self.board[pos[1]][pos[0] - i] == 0:
                break
            elif self.board[pos[1]][pos[0] - i] == opponent:
                self.flipPiece.append((pos[1],pos[0] - i))
            elif self.board[pos[1]][pos[0] - i] == turn:
                for piece in self.flipPiece:
                    self.board[piece[0]][piece[1]] = turn
                break
        self.flipPiece.clear()

        for i in range(1,(8 - pos[0])):   #RIGHT
            if self.board[pos[1]][pos[0] + i] == 0:

                break
            elif self.board[pos[1]][pos[0] + i] == opponent:
                self.flipPiece.append((pos[1],pos[0] + i))
            elif self.board[pos[1]][pos[0] + i] == turn:
                for piece in self.flipPiece:
                    self.board[piece[0]][piece[1]] = turn
                break
        self.flipPiece.clear()

        for i in range(1,min((8 - pos[1]),(8 - pos[0]))):   #UPRIGHT
            if self.board[pos[1] + i][pos[0] + i] == 0:
                break
            elif self.board[pos[1] + i][pos[0] + i] == opponent:
                self.flipPiece.append((pos[1] + i,pos[0] + i))
            elif self.board[pos[1] + i][pos[0] + i] == turn:
                for piece in self.flipPiece:
                    self.board[piece[0]][piece[1]] = turn
                self.flipPiece.clear()
                break
        self.flipPiece.clear()

        for i in range(1,min((8 - pos[1]),(pos[0] + 1))):   #UPLEFT
            if self.board[pos[1] + i][pos[0] - i] == 0:
                break
            elif self.board[pos[1] + i][pos[0] - i] == opponent:
                self.flipPiece.append((pos[1] + i,pos[0] - i))
            elif self.board[pos[1] + i][pos[0] - i] == turn:
                for piece in self.flipPiece:
                    self.board[piece[0]][piece[1]] = turn
                break
        self.flipPiece.clear()

        for i in range(1,min((pos[1] + 1),(pos[0] + 1))):   #DOWNRIGHT
            if self.board[pos[1] - i][pos[0] - i] == 0:
                break
            elif self.board[pos[1] - i][pos[0] - i] == opponent:
                self.flipPiece.append((pos[1] - i,pos[0] - i))
            elif self.board[pos[1] - i][pos[0] - i] == turn:
                for piece in self.flipPiece:
                    self.board[piece[0]][piece[1]] = turn
                break
        self.flipPiece.clear()

        for i in range(1,min((pos[1] + 1),(8 - pos[0]))):   #DOWNLEFT
            if self.board[pos[1] - i][pos[0] + i] == 0:
                break
            elif self.board[pos[1] - i][pos[0] + i] == opponent:
                self.flipPiece.append((pos[1] - i,pos[0] + i))
            elif self.board[pos[1] - i][pos[0] + i] == turn:
                for piece in self.flipPiece:
                    self.board[piece[0]][piece[1]] = turn
                break
        self.flipPiece.clear()

    def checkValidMove(self,pos,turn):
        if turn == 1:
            opponent = 2
        else:
            opponent = 1

        self.count = 0

        for i in range(1, (pos[1] + 1)):  # DOWN
            if self.board[pos[1] - i][pos[0]] == 0:
                break
            elif self.board[pos[1] - i][pos[0]] == opponent:
                self.count += 1
            elif self.board[pos[1] - i][pos[0]] == turn:
                if self.count > 0:
                    return True
                elif self.count == 0:
                    break
        self.count = 0

        for i in range(1, (8 - pos[1])):  # UP
            if self.board[pos[1] + i][pos[0]] == 0:
                break
            elif self.board[pos[1] + i][pos[0]] == opponent:
                self.count += 1
            elif self.board[pos[1] + i][pos[0]] == turn:
                if self.count > 0:
                    return True
                elif self.count == 0:
                    break
        self.count = 0

        for i in range(1, (pos[0] + 1)):  # LEFT
            if self.board[pos[1]][pos[0] - i] == 0:
                break
            elif self.board[pos[1]][pos[0] - i] == opponent:
                self.count += 1
            elif self.board[pos[1]][pos[0] - i] == turn:
                if self.count > 0:
                    return True
                elif self.count == 0:
                    break
        self.count = 0


        for i in range(1, (8 - pos[0])):  # RIGHT
            if self.board[pos[1]][pos[0] + i] == 0:
                break
            elif self.board[pos[1]][pos[0] + i] == opponent:
                self.count += 1
            elif self.board[pos[1]][pos[0] + i] == turn:
                if self.count > 0:
                    return True
                elif self.count == 0:
                    break
        self.count = 0

        for i in range(1, min((8 - pos[1]), (8 - pos[0]))):  # UPRIGHT
            if self.board[pos[1] + i][pos[0] + i] == 0:
                break
            elif self.board[pos[1] + i][pos[0] + i] == opponent:
                self.count += 1
            elif self.board[pos[1] + i][pos[0] + i] == turn:
                if self.count > 0:
                    return True
                elif self.count == 0:
                    break
        self.count = 0

        for i in range(1, min((8 - pos[1]), (pos[0] + 1))):  # UPLEFT
            if self.board[pos[1] + i][pos[0] - i] == 0:
                break
            elif self.board[pos[1] + i][pos[0] - i] == opponent:
                self.count += 1
            elif self.board[pos[1] + i][pos[0] - i] == turn:
                if self.count > 0:
                    return True
                elif self.count == 0:
                    break
        self.count = 0

        for i in range(1, min((pos[1] + 1), (pos[0] + 1))):  # DOWNRIGHT
            if self.board[pos[1] - i][pos[0] - i] == 0:
                break
            elif self.board[pos[1] - i][pos[0] - i] == opponent:
                self.count += 1
            elif self.board[pos[1] - i][pos[0] - i] == turn:
                if self.count > 0:
                    return True
                elif self.count == 0:
                    break
        self.count = 0

        for i in range(1, min((pos[1] + 1), (8 - pos[0]))):  # DOWNLEFT
            if self.board[pos[1] - i][pos[0] + i] == 0:
                break
            elif self.board[pos[1] - i][pos[0] + i] == opponent:
                self.count += 1
            elif self.board[pos[1] - i][pos[0] + i] == turn:
                if self.count > 0:
                    return True
                elif self.count == 0:
                    break
        self.count = 0

        return False

    def update(self):
        self.displayTurn()
        self.displayBoard()
        self.drawPossibleMove()
        self.drawPieces()
        self.drawLines()



board = Board()
