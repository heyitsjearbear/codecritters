import pygame

class StatDisplay:
    def __init__(self, x, y, width=100, height=15):
        self.x = x
        self.y = y
        self.bar_width = width
        self.bar_height = height
        self.font = None
        self.text_color = (255, 255, 255)
        self.health_color = (50, 205, 50)  # Green
        self.hunger_color = (255, 165, 0)  # Orange
        self.energy_color = (30, 144, 255)  # Blue
        self.bar_bg = (70, 70, 70)
        
    def initialize(self):
        """Initialize fonts - call this after pygame.init()"""
        self.font = pygame.font.SysFont('Arial', 18, True)
        
    def draw(self, surface, pet):
        """Draw pet stats on the given surface"""
        if not self.font:
            self.initialize()
            
        # Name and mood display
        name_text = self.font.render(f"{pet.name} - {pet.mood.value}", True, self.text_color)
        surface.blit(name_text, (self.x, self.y))
        
        # Health bar
        self._draw_stat_bar(
            surface, 
            self.x, 
            self.y + 30, 
            pet.health, 
            "Health", 
            self.health_color
        )
        
        # Hunger bar
        self._draw_stat_bar(
            surface, 
            self.x, 
            self.y + 55, 
            pet.hunger, 
            "Hunger", 
            self.hunger_color
        )
        
        # Energy bar
        self._draw_stat_bar(
            surface, 
            self.x, 
            self.y + 80, 
            pet.energy, 
            "Energy", 
            self.energy_color
        )
    
    def _draw_stat_bar(self, surface, x, y, value, label, color):
        """Helper method to draw a single stat bar"""
        # Draw background bar
        pygame.draw.rect(surface, self.bar_bg, (x, y, self.bar_width, self.bar_height))
        
        # Draw stat value bar
        pygame.draw.rect(surface, color, (x, y, value, self.bar_height))
        
        # Draw text label
        text = self.font.render(f"{label}: {value}", True, self.text_color)
        surface.blit(text, (x + self.bar_width + 10, y))