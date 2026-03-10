import numpy as np
from typing import Callable

class PrisonEnvironment:
    """
    Προσομοιώνει το περιβάλλον για το 100 Prisoners Riddle.
    """
    
    def __init__(self, num_prisoners: int = 100, max_attempts: int = 50):
        self.num_prisoners = num_prisoners
        self.max_attempts = max_attempts
        self.boxes = np.array([])
        
    def reset(self) -> None:
        """Ξεκινάει ένα νέο παιχνίδι, ανακατεύοντας τυχαία τα κουτιά."""
        self.boxes = np.arange(self.num_prisoners)
        np.random.shuffle(self.boxes)

    def play_prisoner(self, prisoner_id: int, strategy_func: Callable) -> bool:
        """Προσομοιώνει την προσπάθεια ΕΝΟΣ φυλακισμένου."""
        last_opened_slip = None 
        
        for attempt in range(self.max_attempts):
            # Ο φυλακισμένος (ή το AI) διαλέγει το επόμενο κουτί
            box_to_open = strategy_func(prisoner_id, attempt, last_opened_slip)
            box_to_open = box_to_open % self.num_prisoners
            
            # Βλέπει το καρτελάκι μέσα στο κουτί
            last_opened_slip = self.boxes[box_to_open]
            
            # Αν βρει τον αριθμό του, κερδίζει
            if last_opened_slip == prisoner_id:
                return True
                
        # Αν τελειώσουν οι 50 προσπάθειες, χάνει
        return False

    def play_full_game(self, strategy_func: Callable) -> bool:
        """Προσομοιώνει το παιχνίδι για ΟΛΟΥΣ τους φυλακισμένους."""
        self.reset()
        
        for prisoner_id in range(self.num_prisoners):
            success = self.play_prisoner(prisoner_id, strategy_func)
            if not success:
                # Αν χάσει έστω και ΕΝΑΣ, τελειώνει το παιχνίδι με ήττα
                return False
                
        # Όλοι βρήκαν τον αριθμό τους
        return True