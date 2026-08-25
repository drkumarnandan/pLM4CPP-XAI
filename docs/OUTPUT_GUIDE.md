# Output Guide

## Input
Use FASTA or CSV (`sequence_id,sequence`). Query sequences should contain only
the 20 standard amino acids and be no longer than 61 residues.

## Main output
- `predictions.csv`: four model probabilities/calls, mean/median ensemble
  probabilities, and CPP vote count.
- `consensus_residue_importance.csv`: per-residue four-PLM consensus rank,
  hotspot status, and PLM support.
- `<PLM>_residue_XAI.csv`: individual residue attribution outputs.
- `<sequence_id>_consensus_XAI.png`: consensus importance heatmap.

Consensus hotspots are model-derived explanations. They are not direct
experimental evidence of causal uptake determinants.
