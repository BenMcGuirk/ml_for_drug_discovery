# Import ESOL data (solubility data)

import deepchem as dc

def load_esol():
    """
    Loads the ESOL (Delaney) dataset from DeepChem's MoleculeNet module.
    Returns:
        tasks: list of target names
        datasets: tuple of (train_dataset, valid_dataset, test_dataset)
        transformers: list of transformers applied to the data
    """
    tasks, datasets, transformers = dc.molnet.load_delaney()
    train_dataset, valid_dataset, test_dataset = datasets
    return tasks, train_dataset, valid_dataset, test_dataset, transformers


if __name__ == "__main__":
    tasks, train, valid, test, transformers = load_esol()
    print(f"Tasks: {tasks}")
    print(f"Number of training samples: {len(train)}")
    print(f"Number of validation samples: {len(valid)}")
    print(f"Number of test samples: {len(test)}")