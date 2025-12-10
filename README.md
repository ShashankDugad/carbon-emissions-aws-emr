# Carbon Emissions Violation Detection - AWS EMR

Air quality violation prediction using 225M records on AWS EMR + Spark.

## Infrastructure
- **Cluster:** AWS EMR 7.12.0 (ap-south-1)
- **Nodes:** 3x m5.xlarge (1 master + 2 core)
- **Stack:** Spark 3.5.6, Hadoop 3.4.1, HDFS
- **Data:** 559 MB parquet on HDFS
- **Cost:** $0.58/hr, auto-terminate after 2hr idle

## Quick Start
```bash
# SSH to cluster
ssh -i ~/bigdata-key-mumbai.pem hadoop@ec2-3-111-35-173.ap-south-1.compute.amazonaws.com

# Run notebook
spark-submit ~/notebooks/dashboard_notebook.py
```

## Team
- Shashank Dugad (sd5957)
- Anshi Shah (ans10020)
- Ronit Gehani (rg4881)

## Results
- ML Model: 99.25% AUC
- Training: 36 min on 66M records
- Violations: 612K (California 72%)
