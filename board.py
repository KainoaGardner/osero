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
                if self.blackTurn:
                    pygame.draw.circle(screen, "Black", (TILESIZE * ((self.mosPos[0] - MARGINSIZE) // TILESIZE) + TILESIZE //2 + MARGINSIZE,TILESIZE *((self.mosPos[1] - MARGINSIZE) // TILESIZE) + TILESIZE //2 + MARGINSIZE),TILESIZE // 2 - 3)
                    screen.blit(toumei,(TILESIZE * ((self.mosPos[0] - MARGINSIZE) // TILESIZE) + MARGINSIZE,TILESIZE *((self.mosPos[1] - MARGINSIZE) // TILESIZE)  + MARGINSIZE))
                elif not self.blackTurn:
                    pygame.draw.circle(screen, "White", (TILESIZE * ((self.mosPos[0] - MARGINSIZE) // TILESIZE) + TILESIZE // 2 + MARGINSIZE,TILESIZE * ((self.mosPos[1] - MARGINSIZE) // TILESIZE) + TILESIZE // 2 + MARGINSIZE),TILESIZE // 2 - 3)
                    screen.blit(toumei, (TILESIZE * ((self.mosPos[0] - MARGINSIZE) // TILESIZE) + MARGINSIZE,TILESIZE * ((self.mosPos[1] - MARGINSIZE) // TILESIZE) + MARGINSIZE))

    def playPiece(self,pos):
        if self.board[pos[1]][pos[0]] == 0:
            if self.blackTurn:
                self.board[pos[1]][pos[0]] = 1
                self.blackTurn = not self.blackTurn
            elif not self.blackTurn:
                self.board[pos[1]][pos[0]] = 2
                self.blackTurn = not self.blackTurn


    def update(self):
        self.displayTurn()
        self.displayBoard()
        self.drawPossibleMove()
        self.drawPieces()
        self.drawLines()



board = Board()
