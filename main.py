from environment.prison_env import PrisonEnvironment
from agents.random_agent import RandomAgent
from agents.optimal_agent import OptimalAgent
from agents.genetic_agent import GeneticAgent
import time

def run_simulation(agent, num_games=10000, num_prisoners=100):
    env = PrisonEnvironment(num_prisoners=num_prisoners, max_attempts=num_prisoners // 2)
    wins = 0
    for _ in range(num_games):
        if env.play_full_game(agent.strategy):
            wins += 1
    return (wins / num_games) * 100

if __name__ == "__main__":
    print("🎯 Ξεκινάει η προσομοίωση για το 100 Prisoners Riddle...\n")
    num_simulations = 10000
    
    # --- 1. Δοκιμή: Τυχαίος Πράκτορας ---
    print(f"🎲 Τρέχουμε {num_simulations} παιχνίδια με τον Τυχαίο Πράκτορα...")
    random_agent = RandomAgent()
    print(f"   Ποσοστό επιβίωσης : {run_simulation(random_agent, num_simulations):.4f}%\n")
    
    # --- 2. Δοκιμή: Βέλτιστος Πράκτορας ---
    print(f"🧠 Τρέχουμε {num_simulations} παιχνίδια με τον Βέλτιστο Πράκτορα (Upper Bound)...")
    optimal_agent = OptimalAgent()
    print(f"   Ποσοστό επιβίωσης : {run_simulation(optimal_agent, num_simulations):.2f}%\n")
    
    # --- 3. FINAL BOSS: Γενετικός Αλγόριθμος (AI) με 100 φυλακισμένους ---
    print("-" * 50)
    print("🚀 Ξεκινάει η εκπαίδευση του AI (100 φυλακισμένοι)...")
    
    N = 100
    env_for_training = PrisonEnvironment(num_prisoners=N, max_attempts=N // 2)
    ai_agent = GeneticAgent(num_prisoners=N, population_size=200)
    
    # Εκπαίδευση και λήψη ιστορικού
    history = ai_agent.evolve(env_for_training, generations=150, games_per_eval=30) 
    
    # Αποθήκευση ιστορικού για το γράφημα (Visualizer)
    with open("evolution_history.csv", "w") as f:
        f.write("generation,score\n")
        for i, score in enumerate(history):
            f.write(f"{i+1},{score}\n")
    
    print(f"\n📊 Το ιστορικό εκπαίδευσης αποθηκεύτηκε στο 'evolution_history.csv'")
    print("-" * 50)

    # Τελική δοκιμή του εκπαιδευμένου AI
    print(f"🤖 Τρέχουμε {num_simulations} τελικά παιχνίδια με το εκπαιδευμένο AI...")
    start_time = time.time()
    ai_win_rate = run_simulation(ai_agent, num_games=num_simulations, num_prisoners=N)
    
    print(f"   Ποσοστό επιβίωσης AI : {ai_win_rate:.2f}%")
    print(f"   Χρόνος Δοκιμής AI    : {time.time() - start_time:.2f} δευτερόλεπτα\n")
    
    if ai_win_rate > 30:
        print("🏆 ΕΠΙΤΥΧΙΑ! Το AI έμαθε τη βέλτιστη στρατηγική!")
    else:
        print("⚠️ Το AI δεν έφτασε στο βέλτιστο επίπεδο ακόμα. Ίσως χρειάζεται περισσότερες γενιές.")