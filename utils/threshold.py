import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import label_binarize
import pandas as pd

def evaluate_thresholds(y_true, y_probs):
    thresholds = np.linspace(0.1, 0.9, 50)
    
    # Binarize y_true to match the multiclass probability structure (3 classes)
    y_true_bin = label_binarize(y_true, classes=[0, 1, 2])

    results = []
    for t in thresholds:
        preds = (y_probs >= t).astype(int)

        results.append({
            "threshold": t,
            "precision": precision_score(y_true_bin, preds, average='macro', zero_division=0),
            "recall": recall_score(y_true_bin, preds, average='macro', zero_division=0),
            "f1": f1_score(y_true_bin, preds, average='macro', zero_division=0)
        })

    return results