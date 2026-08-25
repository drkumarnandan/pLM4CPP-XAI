# Data

Raw datasets are **not bundled in this repository**.

The Colab pipeline expects the following four source files:

1. `pLM4CPPs_dataset_CPP.xlsx`
2. `pLM4CPPs_dataset_Non-CPP.xlsx`
3. `kelm_dataset_CPP.csv`
4. `kelm_dataset_Non-CPP.csv`

Place them in the project `01_data_original/` directory, or allow the notebook to
prompt for upload when they are missing.

The pipeline performs sequence cleaning, nonstandard-residue exclusion, duplicate
and conflicting-label checks, exact internal/KELM overlap checks, and fixed
stratified splitting using random seed 42.

If the source datasets have distribution or licensing restrictions, provide their
original citations/URLs in the public repository rather than redistributing them.
