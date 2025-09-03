## **1. Molecular Property Prediction (QSAR 2.0)**

**Goal:** Predict chemical properties (e.g., solubility, toxicity, logP).

- **Dataset:** MoleculeNet → ESOL, Tox21, FreeSolv.
- **ML angle:** Compare Random Forests on fingerprints vs. Graph Neural Networks (PyTorch Geometric / DeepChem).
- **Impact:** Classic but still relevant. Great for showcasing how deep learning can outperform traditional chemoinformatics.
- **Stretch goal:** Interpretability — visualize which substructures drive predictions.