import pandas as pd
from src.data_quality import data_quality_preprocessing
df=data_quality_preprocessing()

def numerical_stats():
    stats = {}

    num_cols = df.select_dtypes(include=['int64','float64']).columns
    
    for col in num_cols:
        
        stats[col] = {
            "mean": df[col].mean(),
            "median": df[col].median(),
            "std": df[col].std(),
            'max':df[col].max(),
            'min':df[col].min(),
            "25%": df[col].quantile(0.25),
            "75%": df[col].quantile(0.75),
            "skew": df[col].skew(),
            "kurtosis": df[col].kurt()
        }

    return pd.DataFrame(stats).T