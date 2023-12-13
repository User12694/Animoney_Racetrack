import pygame, sys

result = ['Win',""]
class Congratulations:
    def __init__(self):
        global 
        self.result_image = pygame.image.load('')
        
    #Vẽ các thuộc tính lên màn hình
    def draw(self, mouse_pos):
        


    # Cập nhật các trạng thái của thuộc tính
    def update(self, event):
        global MenuSound, gameSound, InitGame
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Back_To_Menu = Pause_Game()
                if Back_To_Menu:
                    InitGame = False
                    # return MenuClass()
        if event.type == pygame.MOUSEBUTTONDOWN:
            
        # pos = pygame.mouse.get_pos()
        # if self.CONTINUE_BUTTON.CheckClick(pos):
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         pass
        #     if event.type == pygame.MOUSEMOTION:
        #         pass # Chuyen mau vang cho nut
        return self
current_class = 