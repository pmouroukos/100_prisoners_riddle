# AI Solves the 100 Prisoners Riddle 🧬

This project uses a **Genetic Algorithm (GA)** to discover the optimal strategy for the famous 100 Prisoners Riddle.

## The Challenge
The 100 prisoners riddle is a classic problem in probability theory. With a random strategy, the survival probability is practically **0%**. However, using the "Cycle-Following" strategy, the probability jumps to over **31%**.

## How the AI Learns
The AI agent evolves through generations using:
* **Genetic Evolution**: Crossover, Mutation, and Tournament Selection.
* **Custom Fitness Function**: Based on the rule "Everyone wins or Everyone loses," encouraging group survival over individual gain.
* **Fair Evaluation**: All agents in a generation are tested on the same set of randomized boxes to eliminate "luck" and focus on strategy.

## Results
The trained AI consistently achieves a **~31.2% success rate**, matching the mathematical upper bound.

![Learning Curve](learning_curve.png)

## How to Run
1. Install dependencies: `pip install -r requirements.txt` or `py -m pip install -r requirements.txt`
2. Run training: `python main.py` or `py main.py`
3. Visualize results: `python visualizer.py` or `py visualizer.py`
