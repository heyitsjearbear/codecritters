from enum import Enum

class Mood(Enum):
    TIRED = "tired"
    HANGRY = "hangry"
    HAPPY = "happy"

class Pet:
    HUNGER_RATE = 1
    ENERGY_DECAY = 1
    STARVATION_DAMAGE = 5
    EXHAUSTION_DAMAGE = 5
    
    def __init__(self, name: str, health: int = 100, hunger: int = 0, energy: int = 100):
        """
        Initialize the pet with default or configurable attributes.
        """
        self.name = name
        self.health = health
        self.hunger = hunger
        self.energy = energy
    
    @property
    def mood(self) -> str:
        """
        Determine the pet's mood based on its attributes.
        Returns a Mood enum value.
        """
        # Define mood conditions in a dictionary
        mood_conditions = {
            Mood.TIRED: self.energy < 20,
            Mood.HANGRY: self.hunger > 80,
            Mood.HAPPY: True,  # Default mood if no other conditions are met
        }

        # Iterate through conditions and return the first matching mood
        for mood_enum, condition in mood_conditions.items():
            if condition:
                return  mood_enum
    
    def feed(self, food_type: str):
        # Define food effects in a dictionary
        food_effects = {
            "fruit": {"hunger": -10, "energy": 5},
            "meat": {"hunger": -20, "energy": 10},
            "kibble": {"hunger": -15, "energy": 0},
        }

        # Check if the food type exists in the dictionary
        if food_type in food_effects:
            effects = food_effects[food_type]
            self.hunger += effects["hunger"]
            self.energy += effects["energy"]
            print(f"{self.name} ate {food_type}. Hunger is now {self.hunger}, energy is now {self.energy}.")
        else:
            print(f"{food_type} is not a valid food!")
    
    def play(self, activity: str):
        """
        Allows the pet to play different activities, affecting its attributes.
        """
        # Define activity effects in a dictionary
        activity_effects = {
            "fetch": {"energy": -20, "hunger": 10, "mood_boost": "excited"},
            "tug_of_war": {"energy": -30, "hunger": 15, "mood_boost": "happy"},
            "chase": {"energy": -25, "hunger": 20, "mood_boost": "playful"},
        }

        # Check if the activity exists in the dictionary
        if activity in activity_effects:
            effects = activity_effects[activity]
            self.energy = max(self.energy + effects["energy"], 0)  # Prevent energy from going below 0
            self.hunger = min(self.hunger + effects["hunger"], 100)  # Prevent hunger from exceeding 100
            mood_boost = effects["mood_boost"]

            print(f"{self.name} played {activity}. Energy is now {self.energy}, hunger is now {self.hunger}. Mood is {mood_boost}.")
        else:
            print(f"{activity} is not a valid activity!")
    
    def update_status(self):
        """
        Simulates time passing: decay stats, apply penalties, and clamp values."
        """
        # Apply decay
        self.hunger += self.HUNGER_RATE
        self.energy -= self.ENERGY_DECAY

        # Apply health penalties
        if self.hunger >= 100:
            self.health -= self.STARVATION_DAMAGE
        if self.energy <= 0:
            self.health -= self.EXHAUSTION_DAMAGE

        # Clamp stats to valid range
        self.hunger = min(max(self.hunger, 0), 100)
        self.energy = min(max(self.energy, 0), 100)
        self.health = min(max(self.health, 0), 100)
        # ✅ Call stat-based event hooks (after clamping)
        if self.hunger > 80:
            self.on_hunger_high()
        if self.energy < 20:
            self.on_energy_low()
        if self.health < 30:
            self.on_health_critical()

    """
    The following methods are internal hook methods that will for now
    print messages, but can eventually trigger animations later,
    log to flask api (POST /log)
    """

    def on_hunger_high(self):
        print(f"{self.name} is getting very hungry!")

    def on_energy_low(self):
        print(f"{self.name} is running out of energy!")

    def on_health_critical(self):
        print(f"{self.name}'s health is in danger!")

