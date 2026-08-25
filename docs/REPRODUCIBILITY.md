# Reproducibility Notes

## Recorded study environment

The uploaded study notebook records the following environment:

- Python 3.12.13
- PyTorch 2.11.0 + CUDA 12.8
- TensorFlow 2.20.0
- Transformers 5.14.0
- fair-esm 2.0.0
- Captum 0.9.0
- NumPy 2.0.2
- pandas 3.0.3
- scikit-learn 1.9.0
- NVIDIA Tesla T4

## Fixed analysis settings

- Random seed: 42
- Maximum peptide length: 61 residues
- Train/validation/internal-test split: 70/15/15%
- Four PLMs: ESM2-320, ESM2-640, ESM2-1280, ProtT5
- PLM weights frozen for classifier training
- Classifier optimizer: Adam
- Initial learning rate: 1e-3
- Maximum epochs: 100
- Early-stopping patience: 12
- Main hotspot definition: upper 20th percentile of within-sequence consensus ranks
- Threshold sensitivity: 10, 15, 20, 25, and 30%
- Composition-controlled motif permutations: 2,000 per dataset
- Random perturbation repeats: 20
- Sequence-level faithfulness bootstrap resamples: 2,000

Classifier batch sizes were 64, 48, 32, and 32 for ESM2-320, ESM2-640,
ESM2-1280, and ProtT5, respectively. Embedding-generation batch sizes were
64, 24, 8, and 8.

## Reproduction order

1. Run `notebooks/01_pLM4CPP_XAI_core_pipeline.ipynb`.
2. Verify generated checkpoints and tables.
3. Run `notebooks/02_pLM4CPP_XAI_manuscript_figures.ipynb`.
4. Compare key performance and XAI summary tables with the manuscript.

Because GPU kernels, package builds, and pretrained-model backends can change,
small floating-point differences may occur even with deterministic seeds.
