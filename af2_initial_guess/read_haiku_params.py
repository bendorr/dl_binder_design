import numpy as np

# Path to the .npz file
file_path = "/Users/benorr/UCSFben/Consulting/Arcellx/multimer_InitialGuess/dl_binder_design/af2_initial_guess/params/params_model_1_multimer_v3.npz"

# Load the .npz file
params = np.load(file_path, allow_pickle=True)

# Print each parameter name and its shape
print("Haiku Parameters:")
for key, value in params.items():
    if 'left_single' not in key: continue
    # if key != 'alphafold/alphafold_iteration/evoformer/preprocess_msa//weights': continue
    if isinstance(value, np.ndarray):
        print(f"Name: {key}, Shape: {value.shape}")
    else:
        print(f"Name: {key}, Type: {type(value)} (non-array content)")

