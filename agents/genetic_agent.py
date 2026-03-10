import numpy as np

class GeneticAgent:
    """
    AI Πράκτορας που χρησιμοποιεί Γενετικό Αλγόριθμο για να ανακαλύψει τη βέλτιστη στρατηγική.
    """
    
    def __init__(self, num_prisoners: int = 100, population_size: int = 200):
        self.num_prisoners = num_prisoners
        self.population_size = population_size
        
        # Αρχικοποίηση: 
        # 1. Βάζουμε έναν "έξυπνο" πράκτορα (Identity Map) που είναι η βάση των κύκλων
        identity_strategy = np.arange(num_prisoners)
        
        # 2. Οι υπόλοιποι είναι τυχαίες μεταθέσεις
        self.population = [np.random.permutation(num_prisoners) for _ in range(population_size - 1)]
        self.population.append(identity_strategy) # "Φυτεύουμε" τον έξυπνο σπόρο
        
        self.best_strategy = identity_strategy # Ξεκινάμε με τον σπόρο ως καλύτερο

    def strategy(self, prisoner_id: int, attempt: int, last_opened_slip: int) -> int:
        """Πώς παίζει ο πράκτορας στο παιχνίδι"""
        if attempt == 0:
            return prisoner_id
        
        # Χρησιμοποιεί την καλύτερη στρατηγική που έχει βρει μέχρι τώρα
        return self.best_strategy[last_opened_slip]

    def evolve(self, env, generations: int = 50, games_per_eval: int = 30):
        print(f"\n🧬 Εκπαίδευση με Δίκαιη Αξιολόγηση για {generations} γενιές...")
        history = []
        
        for generation in range(generations):
            fitness_scores = []
            
            # --- 1. ΔΙΚΑΙΗ ΑΞΙΟΛΟΓΗΣΗ ---
            # Δημιουργούμε σταθερά "δωμάτια" για όλη τη γενιά
            fixed_games = [np.random.permutation(self.num_prisoners) for _ in range(games_per_eval)]
            
            for strategy_array in self.population:
                total_score = 0
                for boxes in fixed_games:
                    saved_in_game = 0
                    for p_id in range(self.num_prisoners):
                        current_box = p_id
                        found = False
                        for attempt in range(self.num_prisoners // 2):
                            slip = boxes[current_box]
                            if slip == p_id:
                                found = True
                                break
                            current_box = strategy_array[slip]
                        if found:
                            saved_in_game += 1
                    
                    # Ο κανόνας ομαδικότητας: Όλοι ή Κανείς
                    if saved_in_game == self.num_prisoners:
                        total_score += saved_in_game + 1000
                    else:
                        total_score += saved_in_game
                
                fitness_scores.append(total_score / games_per_eval)
            
            # Καταγραφή του καλύτερου σκορ
            best_idx = int(np.argmax(fitness_scores))
            current_best_score = fitness_scores[best_idx]
            self.best_strategy = self.population[best_idx].copy()
            history.append(current_best_score)
            
            if (generation + 1) % 5 == 0 or current_best_score > 100:
                print(f"Γενιά {generation + 1}/{generations} | Max Score: {current_best_score:.1f}")
            
            # --- 2. ΑΝΑΠΑΡΑΓΩΓΗ (Επόμενη Γενιά) ---
            new_population = []
            
            # Elitism: Κρατάμε τους 10 καλύτερους χωρίς αλλαγές
            sorted_indices = np.argsort(fitness_scores)[::-1]
            for i in range(10):
                new_population.append(self.population[sorted_indices[i]])
            
            while len(new_population) < self.population_size:
                # Tournament Selection: Διαλέγουμε 2 τυχαίους και κερδίζει ο καλύτερος
                def select_parent():
                    i, j = np.random.choice(len(self.population), 2)
                    return self.population[i] if fitness_scores[i] > fitness_scores[j] else self.population[j]
                
                p1 = select_parent()
                p2 = select_parent()
                
                # Crossover (Διασταύρωση)
                split = np.random.randint(1, self.num_prisoners - 1)
                child = np.concatenate([p1[:split], [x for x in p2 if x not in p1[:split]]])
                
                # Mutation (Μετάλλαξη - Το "Σοκ")
                if np.random.rand() < 0.2: # 20% πιθανότητα
                    for _ in range(3): # Κάνουμε 3 ανταλλαγές
                        idx1, idx2 = np.random.choice(self.num_prisoners, 2, replace=False)
                        child[idx1], child[idx2] = child[idx2], child[idx1]
                
                new_population.append(child)
            
            self.population = new_population
            
        print("\n✅ Η εκπαίδευση ολοκληρώθηκε!")
        return history