import pygame
import sys

class GameSelection:
    def __init__(self):
        pygame.init()

        self.screen_width = 800
        self.screen_height = 600

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Game Selection")

        self.clock = pygame.time.Clock()

        # Mảng lưu thông tin về map và nhân vật
        self.maps_and_characters = {
            1: {"map": "Map 1", "characters": ["Character 1", "Character 2", "Character 3", "Character 4", "Character 5"]},
            2: {"map": "Map 2", "characters": ["Character 6", "Character 7", "Character 8", "Character 9", "Character 10"]},
            3: {"map": "Map 3", "characters": ["Character 11", "Character 12", "Character 13", "Character 14", "Character 15"]},
            4: {"map": "Map 4", "characters": ["Character 16", "Character 17", "Character 18", "Character 19", "Character 20"]},
            5: {"map": "Map 5", "characters": ["Character 21", "Character 22", "Character 23", "Character 24", "Character 25"]},
        }

        self.selected_map = None
        self.selected_character = None

    def display_maps_and_characters(self):
        print("Choose a map:")
        for key, value in self.maps_and_characters.items():
            print(f"{key}: {value['map']}")

    def display_selected_options(self):
        if self.selected_map is not None and self.selected_character is not None:
            print(f"Selected Map: {self.maps_and_characters[self.selected_map]['map']}")
            print(f"Selected Character: {self.selected_character}")
            print("Press 'Enter' to start the game.")
        else:
            print("Please select a map and a character.")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                        self.selected_map = event.key - pygame.K_0  # Convert key code to map number
                        self.display_maps_and_characters()

                    elif event.key in [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t]:
                        if self.selected_map is not None:
                            character_index = event.key - pygame.K_q  # Convert key code to character index
                            self.selected_character = self.maps_and_characters[self.selected_map]['characters'][character_index]
                            self.display_selected_options()

                    elif event.key == pygame.K_RETURN:
                        if self.selected_map is not None and self.selected_character is not None:
                            print("Starting the game...")
                            # Add code to start the game with the selected map and character
                            pygame.quit()
                            sys.exit()

            pygame.display.flip()
            self.clock.tick(30)

if __name__ == "__main__":
    game = GameSelection()
    game.run()
