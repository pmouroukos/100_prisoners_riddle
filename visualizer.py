import matplotlib.pyplot as plt
import pandas as pd

def plot_learning_curve():
    try:
        # Φόρτωση των δεδομένων
        data = pd.read_csv('evolution_history.csv')
        
        plt.figure(figsize=(10, 6))
        
        # Σχεδιασμός της καμπύλης
        plt.plot(data['generation'], data['score'], color='#2ca02c', linewidth=2, label='Best Score (Fitness)')
        
        # Προσθήκη ορίων (Baseline και Bonus)
        plt.axhline(y=365, color='r', linestyle='--', label='Theoretical Optimum (~31%)')
        plt.axhline(y=42, color='gray', linestyle=':', label='Random Strategy (~0%)')

        # Formatting
        plt.title('AI Learning Curve: 100 Prisoners Riddle', fontsize=14, pad=20)
        plt.xlabel('Generation (Epoch)', fontsize=12)
        plt.ylabel('Fitness Score (Saved Prisoners + Bonus)', fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Αποθήκευση και εμφάνιση
        plt.savefig('learning_curve.png')
        print("✨ Το γράφημα δημιουργήθηκε: learning_curve.png")
        plt.show()
        
    except FileNotFoundError:
        print("❌ Σφάλμα: Δεν βρέθηκε το αρχείο evolution_history.csv. Τρέξε πρώτα το main.py!")

if __name__ == "__main__":
    plot_learning_curve()