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

class MessageDisplay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = None
        self.text_color = (255, 255, 255)
        self.bg_color = (0, 0, 0, 128)  # Semi-transparent black
        self.message = ""
        self.timer = 0
        
    def initialize(self):
        """Initialize fonts - call this after pygame.init()"""
        self.font = pygame.font.SysFont('Arial', 24, True)
    
    def set_message(self, text, duration=120):
        """Set a message to display for the specified duration (in frames)"""
        self.message = text
        self.timer = duration
    
    def update(self):
        """Update message timer - call this every frame"""
        if self.timer > 0:
            self.timer -= 1
            
    def draw(self, surface):
        """Draw message if timer is active"""
        if self.timer <= 0 or not self.message:
            return
            
        if not self.font:
            self.initialize()
        
        # Create message surface
        message_surf = self.font.render(self.message, True, self.text_color)
        message_rect = message_surf.get_rect(center=(self.width//2, self.height - 50))
        
        # Draw background
        bg_rect = message_rect.inflate(20, 10)
        bg_surf = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
        bg_surf.fill(self.bg_color)
        surface.blit(bg_surf, bg_rect.topleft)
        
        # Draw message
        surface.blit(message_surf, message_rect)

class ControlsWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.is_visible = False
        self.font = None
        self.title_font = None
        self.text_color = (255, 255, 255)
        self.bg_color = (0, 0, 0, 200)  # Semi-transparent black
        self.controls = [
            {"key": "F", "action": "Feed pet"},
            {"key": "R", "action": "Rest pet"},
            {"key": "P", "action": "Play with pet"},
            {"key": "U", "action": "Update pet status"},
            {"key": "Mouse", "action": "Drag pet"},
            {"key": "H", "action": "Show/hide controls"}
        ]
        
    def initialize(self):
        """Initialize fonts - call this after pygame.init()"""
        self.font = pygame.font.SysFont('Arial', 16)
        self.title_font = pygame.font.SysFont('Arial', 24, True)
        
    def toggle(self):
        """Toggle visibility of the controls window"""
        self.is_visible = not self.is_visible
        
    def draw(self, surface):
        """Draw controls window if visible"""
        if not self.is_visible:
            return
            
        if not self.font:
            self.initialize()
            
        # Calculate dimensions
        window_width = 300
        window_height = 50 + (len(self.controls) * 30)
        x = (self.width - window_width) // 2
        y = (self.height - window_height) // 2
        
        # Draw background
        bg_surf = pygame.Surface((window_width, window_height), pygame.SRCALPHA)
        bg_surf.fill(self.bg_color)
        surface.blit(bg_surf, (x, y))
        
        # Draw border
        pygame.draw.rect(surface, self.text_color, (x, y, window_width, window_height), 2)
        
        # Draw title
        title_surf = self.title_font.render("Game Controls", True, self.text_color)
        title_rect = title_surf.get_rect(center=(x + window_width//2, y + 25))
        surface.blit(title_surf, title_rect)
        
        # Draw controls list
        for i, control in enumerate(self.controls):
            # Key box
            key_box = pygame.Rect(x + 20, y + 60 + (i * 30), 30, 22)
            pygame.draw.rect(surface, self.text_color, key_box, 1)
            
            # Key text
            key_surf = self.font.render(control["key"], True, self.text_color)
            key_rect = key_surf.get_rect(center=key_box.center)
            surface.blit(key_surf, key_rect)
            
            # Action text
            action_surf = self.font.render(control["action"], True, self.text_color)
            surface.blit(action_surf, (x + 70, y + 60 + (i * 30)))