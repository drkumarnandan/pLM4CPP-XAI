"""Consensus XAI utilities."""

import numpy as np


def redundancy_adjusted_consensus(attention, grad_input, integrated_gradients):
    """Combine normalized residue scores while avoiding double weighting of gradient methods."""
    attention = np.asarray(attention, dtype=float)
    grad_input = np.asarray(grad_input, dtype=float)
    integrated_gradients = np.asarray(integrated_gradients, dtype=float)
    gradient_family = (grad_input + integrated_gradients) / 2.0
    return (attention + gradient_family) / 2.0


def global_plm_consensus(model_consensus_scores):
    """Average model-level consensus scores across PLMs."""
    arr = np.asarray(model_consensus_scores, dtype=float)
    return np.mean(arr, axis=0)


def jaccard(a, b):
    a, b = set(a), set(b)
    union = a | b
    return len(a & b) / len(union) if union else np.nan
