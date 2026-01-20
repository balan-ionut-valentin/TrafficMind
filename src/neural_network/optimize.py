import subprocess
import csv
import os
import sys

# Define experiments
experiments = [
    {
        "name": "baseline",
        "lr": 0.001,
        "batch": 32,
        "dropout": 0.5,
        "dense": 64,
        "description": "Baseline (Etapa 5 Config)"
    },
    {
        "name": "exp1_lr_low",
        "lr": 0.0001,
        "batch": 32,
        "dropout": 0.5,
        "dense": 64,
        "description": "Learning Rate 0.0001"
    },
    {
        "name": "exp2_batch_64",
        "lr": 0.001,
        "batch": 64,
        "dropout": 0.5,
        "dense": 64,
        "description": "Batch Size 64"
    },
    {
        "name": "exp3_dense_128",
        "lr": 0.001,
        "batch": 32,
        "dropout": 0.5,
        "dense": 128,
        "description": "Hidden Layer 128 units"
    },
    {
        "name": "exp4_dropout_03",
        "lr": 0.001,
        "batch": 32,
        "dropout": 0.3,
        "dense": 64,
        "description": "Dropout 0.3"
    }
]

RESULTS_FILE = "results/optimization_experiments.csv"
PYTHON_EXE = sys.executable
TRAIN_SCRIPT = "src/neural_network/train_model.py"

def run_experiments():
    results = []
    print(f"Starting {len(experiments)} experiments...")
    
    for exp in experiments:
        print(f"\n>>> Running Experiment: {exp['name']} <<<")
        cmd = [
            PYTHON_EXE, TRAIN_SCRIPT,
            "--name", exp['name'],
            "--lr", str(exp['lr']),
            "--batch", str(exp['batch']),
            "--dropout", str(exp['dropout']),
            "--dense", str(exp['dense']),
            "--epochs", "25" 
        ]
        
        try:
            # Don't capture output, let it show in console. Check=True raises error on failure.
            subprocess.run(cmd, check=True, text=True, capture_output=False)
            
            # Read metrics from CSV
            history_path = os.path.join("results", f"history_{exp['name']}.csv")
            val_acc = 0.0
            
            try:
                if os.path.exists(history_path):
                     with open(history_path, 'r') as f:
                         # Skip header
                         lines = f.readlines()
                         if len(lines) > 1:
                             # Get headers to find val_accuracy index
                             headers = lines[0].strip().split(',')
                             # Simple flexible search
                             val_acc_idx = -1
                             if 'val_accuracy' in headers:
                                 val_acc_idx = headers.index('val_accuracy')
                             elif 'accuracy' in headers: # Fallback
                                 val_acc_idx = headers.index('accuracy')
                                 
                             if val_acc_idx != -1:
                                 last_line = lines[-1].strip().split(',')
                                 if len(last_line) > val_acc_idx:
                                    val_acc = float(last_line[val_acc_idx])
            except Exception as parsing_error:
                print(f"Error parsing CSV for {exp['name']}: {parsing_error}")

            results.append({
                "Exp#": exp['name'],
                "Modificare": exp['description'],
                "Accuracy": val_acc,
                "Params": f"lr={exp['lr']}, b={exp['batch']}, dr={exp['dropout']}, d={exp['dense']}"
            })
            
        except subprocess.CalledProcessError as e:
            print(f"Error running experiment {exp['name']}: {e}")

    # Save Results
    with open(RESULTS_FILE, 'w', newline='') as csvfile:
        fieldnames = ['Exp#', 'Modificare', 'Accuracy', 'Params']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
        
    print(f"\nOptimization complete. Results saved to {RESULTS_FILE}")

if __name__ == "__main__":
    run_experiments()
