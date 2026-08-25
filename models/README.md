# Published trained classifiers

This directory contains the exact four trained classifier heads used in the
pLM4CPP-XAI study.

| Model | Validation-selected MCC threshold |
|---|---:|
| ESM2-320 | 0.830 |
| ESM2-640 | 0.925 |
| ESM2-1280 | 0.615 |
| ProtT5 | 0.765 |

Each directory contains `final_attention_classifier.keras` and
`selected_threshold.json`. `model_manifest.json` records SHA256 checksums.

The pretrained ESM2/ProtT5 backbone weights are downloaded from their original
public providers when the inference notebook runs.
