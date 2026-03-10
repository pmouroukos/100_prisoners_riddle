import numpy as np

class RandomAgent:
    """
    Πράκτορας που επιλέγει 50 τυχαία κουτιά χωρίς να τα επαναλαμβάνει.
    Αποτελεί το Lower Bound (Ποσοστό επιτυχίας ~0%).
    """
    
    def __init__(self, num_boxes: int = 100, max_attempts: int = 50):
        self.num_boxes = num_boxes
        self.max_attempts = max_attempts
        self.current_choices = []

    def strategy(self, prisoner_id: int, attempt: int, last_opened_slip: int) -> int:
        # Στην πρώτη προσπάθεια (attempt 0), προ-επιλέγουμε 50 τυχαία και διαφορετικά κουτιά
        if attempt == 0:
            self.current_choices = np.random.choice(
                self.num_boxes, 
                size=self.max_attempts, 
                replace=False 
            )
        
        # Ανοίγει το επόμενο τυχαίο κουτί από τη λίστα του
        return self.current_choices[attempt]