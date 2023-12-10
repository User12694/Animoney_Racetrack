class SHOP:
    def __init__(self):
        pygame.init()
        self.shoprunning = True
        self.xSCREEN, self.ySCREEN = 1280, 720
        self.SCREEN = pygame.display.set_mode((self.xSCREEN, self.ySCREEN))
        # image
        self.bgshop = pygame.image.load("image/shop/bgshop1.png")
        self.note1 = pygame.image.load("image/shop/note1.png")
        self.note2 = pygame.image.load("image/shop/note2.png")
        self.note3 = pygame.image.load("image/shop/note3.png")
        self.ball = pygame.image.load("image/shop/ball1.png")
        self.hand1 = pygame.image.load("image/shop/hand1.png")
        self.hand2 = pygame.image.load("image/shop/hand2.png")
        self.hand3 = pygame.image.load("image/shop/hand3.png")
        self.hand4 = pygame.image.load("image/shop/hand4.png")
        self.hand5 = pygame.image.load("image/shop/hand5.png")
        self.sold = pygame.image.load("image/shop/sold1.png")
        # tien
        self.file = open('money/player_money.txt', 'r')
        self.money = int(self.file.readline().split('=')[0])
        self.file.close()
        self.moneyplus = 0
        # vi tri
        self.dx, self.dy = 10, 10
        self.xnote, self.ynote = 0, 150
        self.xMoney, self.yMoney = 10, 40
        self.r = 150
        self.xI, self.yI = 770, 350
        self.x1 = self.xI
        self.y1 = self.yI - self.r
        self.x2 = self.xI + self.r * math.sin(math.pi / 5 * 2)
        self.y2 = self.yI - self.r * math.cos(math.pi / 5 * 2)
        self.x3 = self.xI + self.r * math.sin(math.pi / 5)
        self.y3 = self.yI + self.r * math.cos(math.pi / 5)
        self.x4 = self.xI - self.r * math.sin(math.pi / 5)
        self.y4 = self.yI + self.r * math.cos(math.pi / 5)
        self.x5 = self.xI - self.r * math.sin(math.pi / 5 * 2)
        self.y5 = self.yI - self.r * math.cos(math.pi / 5 * 2)
        # cac bien kiem tra
        self.k = 1
        self.s = 0
        # phim
        self.K_LEFT = self.K_RIGHT = self.K_SPACE = self.K_DONE = False        
        # bua
        self.num = 0
        self.num_bua1 = 0
        self.num_bua2 = 0
        self.num_bua3 = 0
        self.num_bua4 = 0
        # delay
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def show_note(self, s):
        if s == 0:
            self.SCREEN.blit(self.note1, (self.xnote, self.ynote))
        if s >= 1:
            self.SCREEN.blit(self.note2, (self.xnote, self.ynote))
            self.show_money(600, 620, "ENTER TO CONTINUE", 40)

    def show_money(self, x, y, money, size):
        font = pygame.font.Font("font/minigame.ttf", size)
        money = font.render(str(money), True, (255, 255, 255))
        self.SCREEN.blit(money, (x, y))

    def move_hand(self, k):
        if k == 1:
            self.SCREEN.blit(self.hand1, (self.xI + self.dx, self.yI - self.dy))
        if k == 2:
            self.SCREEN.blit(self.hand2, (self.xI + self.dx, self.yI - self.dy))
        if k == 3:
            self.SCREEN.blit(self.hand3, (self.xI + self.dx, self.yI - self.dy))
        if k == 4:
            self.SCREEN.blit(self.hand4, (self.xI + self.dx, self.yI - self.dy))
        if k == 5:
            self.SCREEN.blit(self.hand5, (self.xI + self.dx, self.yI - self.dy))

    def sold_ball(self, k, s):
        if s == 2:
            if k == 1:
                self.SCREEN.blit(self.sold, (self.x1, self.y1))
            if k == 2:
                self.SCREEN.blit(self.sold, (self.x2, self.y2))
            if k == 3:
                self.SCREEN.blit(self.sold, (self.x3, self.y3))
            if k == 4:
                self.SCREEN.blit(self.sold, (self.x4, self.y4))
            if k == 5:
                self.SCREEN.blit(self.sold, (self.x5, self.y5))

    def num_bua(self, num):
        if num == 1:
            self.num_bua1 = self.num_bua1 + 1
        if num == 2:
            self.num_bua2 = self.num_bua2 + 1
        if num == 3:
            self.num_bua3 = self.num_bua3 + 1
        if num == 4:
            self.num_bua4 = self.num_bua4 + 1

    def run(self):
        global lock_shop, MONEY
        while self.shoprunning and lock_shop == False:
            self.clock.tick(self.FPS)
            # insert image
            self.SCREEN.blit(self.bgshop, (0, 0))
            self.show_money(self.xMoney, self.yMoney, "Money: {}".format(self.money), 32)
            self.show_money(self.x1 + 50, self.y1 - 30, "100", 20)
            self.show_money(self.x2 + 50, self.y2 - 30, "100", 20)
            self.show_money(self.x3 + 50, self.y3 - 30, "100", 20)
            self.show_money(self.x4 + 50, self.y4 - 30, "100", 20)
            self.show_money(self.x5 + 50, self.y5 - 30, "100", 20)
            self.SCREEN.blit(self.ball, (self.x1, self.y1))
            self.SCREEN.blit(self.ball, (self.x2, self.y2))
            self.SCREEN.blit(self.ball, (self.x3, self.y3))
            self.SCREEN.blit(self.ball, (self.x4, self.y4))
            self.SCREEN.blit(self.ball, (self.x5, self.y5))
            self.move_hand(self.k)
            self.show_note(self.s)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # su kien nhan thoat
                    self.file.close()
                    self.shoprunning = False
                    pygame.quit()
                    sys.exit()  # thoat chuong trinh

                if event.type == pygame.KEYDOWN:  # su kien co phim nhan xuong
                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = True
                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = True
                    if event.key == pygame.K_SPACE:
                        self.K_SPACE = True
                        pygame.mixer.init()
                        pygame.mixer.music.load('sounds/sold.mp3')
                        pygame.mixer.music.play()

                    if event.key == pygame.K_RETURN:
                        self.K_DONE = True

                if event.type == pygame.KEYUP:  # su kien tha phm
                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = False
                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = False
                    if event.key == pygame.K_SPACE:
                        self.K_SPACE = False
                    if event.key == pygame.K_RETURN:
                        self.K_DONE = False

            if self.K_LEFT and self.s == 0:
                self.k = self.k - 1
                if self.k < 1:
                    self.k = self.k + 5
                if self.k > 5:
                    self.k = self.k - 5
                self.K_LEFT = False
            if self.K_RIGHT and self.s == 0:
                self.k = self.k + 1
                if self.k < 1:
                    self.k = self.k + 5
                if self.k > 5:
                    self.k = self.k - 5
                self.K_RIGHT = False
            if self.K_SPACE and self.s == 0:
                self.file = open('sounds/battat.txt','r')
                self.file.seek(0)
                self.sound = str(self.file.readline())
                # if self.sound == 'On':
                    # pygame.mixer.init()
                    # pygame.mixer.music.load('sounds/sold.mp3')
                    # pygame.mixer.music.play()

                self.s = self.s + 1
                self.K_SPACE = False

            if self.s == 1 and self.money >= 100:
                self.moneyplus = self.moneyplus - 100
                self.num = random.randint(1, 4)
                self.file = open('money/player_money.txt', 'w')
                self.money = self.money + self.moneyplus
                self.file.write(str(self.money))
                self.file.seek(0)
                self.file.close()
                self.s = self.s + 1

            self.num_bua(self.num)
            self.sold_ball(self.k, self.s)
            MONEY = self.money

            if self.s == 1 and self.money <= 99:
                self.SCREEN.blit(self.note3, (self.xnote, self.ynote))

            if self.K_DONE and self.s >= 1:
                lock_shop = True
                self.file = open('sounds/battat.txt','r')
                self.file.seek(0)
                self.sound = str(self.file.readline())
                if self.sound == 'On':
                    if numMap == 1:
                        pygame.mixer.music.load('sounds/cheering1.mp3')
                        pygame.mixer.music.play()
                    if numMap == 2:
                        pygame.mixer.music.load('sounds/cheering2.mp3')
                        pygame.mixer.music.play()
                    if numMap == 3:
                        pygame.mixer.music.load('sounds/cheering3.mp3')
                        pygame.mixer.music.play()
                    if numMap == 4:
                        pygame.mixer.music.load('sounds/cheering4.mp3')
                        pygame.mixer.music.play()
                    if numMap == 5:
                        pygame.mixer.music.load('sounds/cheering5.mp3')
                        pygame.mixer.music.play()
                self.K_DONE = False
            pygame.display.update()