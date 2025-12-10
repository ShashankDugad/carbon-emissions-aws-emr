# Session 12: ML Training Complete

## Results
- Model: Random Forest (20 trees, depth 8)
- Validation AUC: 99.39%
- Test AUC: 99.40%
- Training time: 10.5 min
- Test data: 17.4M rows (2023-2024)

## Infrastructure
- AWS EMR 7.12.0 (ap-south-1)
- 3x m5.xlarge (8 cores, 24 GB RAM)
- Spark 3.5.6: 4 cores/executor, 4GB memory
- Data: 559 MB parquet on HDFS

## Files
- Model: hdfs:///user/hadoop/models/rf_model_timesplit
- Script: train_baseline_timesplit.py
