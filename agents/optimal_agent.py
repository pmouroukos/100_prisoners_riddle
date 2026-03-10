class OptimalAgent:
    """
    Πράκτορας που ακολουθεί τη στρατηγική των κύκλων (Pointer Strategy).
    Αποτελεί το Upper Bound (Ποσοστό επιτυχίας ~31.18%).
    """
    
    def strategy(self, prisoner_id: int, attempt: int, last_opened_slip: int) -> int:
        # Στην πρώτη προσπάθεια, πάει ΠΑΝΤΑ στο κουτί με τον δικό του αριθμό
        if attempt == 0:
            return prisoner_id
        
        # Στις επόμενες προσπάθειες, πάει στο κουτί που του "έδειξε" το προηγούμενο καρτελάκι
        return last_opened_slip