# pLM4CPP-XAI

**pLM4CPP-XAI: An Explainable Protein Language Model Framework for Cell-Penetrating Peptide Prediction and Interpretation**

pLM4CPP-XAI predicts cell-penetrating peptides (CPPs) with four pretrained protein
language models and provides residue-level consensus explanations.

**Nandan Kumar and Yonghui Li**  
Department of Grain and Food Science, Kansas State University

[![Open QuickStart in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/drkumarnandan/pLM4CPP-XAI/blob/main/notebooks/00_QUICKSTART_Predict_New_Sequences.ipynb)

## Use pLM4CPP-XAI on your own sequences

**No retraining is required.**

1. Click **Open QuickStart in Colab** above.
2. Select a **T4 GPU** in Colab.
3. Click **Run all**.
4. Upload FASTA or CSV.
5. Download the generated results ZIP.

Example CSV:

```csv
sequence_id,sequence
pep_1,RQIKIWFQNRRMKWKK
pep_2,KFWKKFWKKFWK
```

Input sequences should contain only the 20 standard amino acids and be **≤61
residues**, matching the modeled sequence-length range used in the study.

## What the user receives

- ESM2-320 CPP probability and classification
- ESM2-640 CPP probability and classification
- ESM2-1280 CPP probability and classification
- ProtT5 CPP probability and classification
- mean and median four-model ensemble probabilities
- Attention residue scores
- Gradient × Input residue scores
- Integrated Gradients residue scores
- redundancy-adjusted four-PLM consensus residue importance
- top-20% consensus hotspots
- number of PLMs independently supporting each hotspot
- residue-level XAI heatmaps

The result ZIP contains:

```text
predictions.csv
consensus_residue_importance.csv
ESM2_320_residue_XAI.csv
ESM2_640_residue_XAI.csv
ESM2_1280_residue_XAI.csv
ProtT5_residue_XAI.csv
<sequence_id>_consensus_XAI.png
```

## Trained classifiers included

The exact classifier heads used in the study are bundled in [`models/`](models/).

| Model | Validation-selected MCC threshold |
|---|---:|
| ESM2-320 | 0.830 |
| ESM2-640 | 0.925 |
| ESM2-1280 | 0.615 |
| ProtT5 | 0.765 |

The pretrained ESM2 and ProtT5 backbone weights are downloaded from their
original public providers at runtime.

## Classifier architecture

```text
Residue embeddings
      ↓
Layer normalization
      ↓
Dense(128, GELU)
      ↓
Dropout(0.20)
      ↓
Masked attention pooling
      ↓
Dense(128, GELU) → Dropout(0.30)
      ↓
Dense(32, GELU) → Dropout(0.20)
      ↓
Sigmoid CPP probability
```

## Repository structure

```text
pLM4CPP-XAI/
├── notebooks/
│   ├── 00_QUICKSTART_Predict_New_Sequences.ipynb
│   ├── 10_Reproduce_Study_Pipeline.ipynb
│   ├── 11_Reproduce_Manuscript_Figures.ipynb
│   └── 99_Full_Analysis_Notebook_Sanitized.ipynb
├── models/
├── src/plm4cpp_xai/
├── examples/
├── docs/
├── data/
├── scripts/
├── requirements_inference.txt
├── requirements.txt
├── CITATION.cff
└── README.md
```

## Reproduce the study

Use `10_Reproduce_Study_Pipeline.ipynb` for the full training/XAI workflow and
`11_Reproduce_Manuscript_Figures.ipynb` for manuscript-oriented visualizations.

The source datasets are not automatically redistributed. See `data/README.md`.

## Citation

Please cite the associated pLM4CPP-XAI manuscript when using this framework.
`CITATION.cff`
