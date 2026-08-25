"""Core configuration used in the pLM4CPP-XAI study."""

SEED = 42
MAX_LEN = 61
MAX_EPOCHS = 100
PATIENCE = 12
LEARNING_RATE = 1e-3

PLM_CONFIGS = {
    "ESM2_320": {
        "type": "esm", "loader": "esm2_t6_8M_UR50D", "layer": 6,
        "embedding_dimension": 320, "embedding_batch_size": 64,
        "classifier_batch_size": 64,
    },
    "ESM2_640": {
        "type": "esm", "loader": "esm2_t30_150M_UR50D", "layer": 30,
        "embedding_dimension": 640, "embedding_batch_size": 24,
        "classifier_batch_size": 48,
    },
    "ESM2_1280": {
        "type": "esm", "loader": "esm2_t33_650M_UR50D", "layer": 33,
        "embedding_dimension": 1280, "embedding_batch_size": 8,
        "classifier_batch_size": 32,
    },
    "ProtT5": {
        "type": "prott5", "loader": "Rostlab/prot_t5_xl_uniref50", "layer": None,
        "embedding_dimension": 1024, "embedding_batch_size": 8,
        "classifier_batch_size": 32,
    },
}
