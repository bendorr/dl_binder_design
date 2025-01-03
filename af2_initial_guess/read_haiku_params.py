import numpy as np

# Path to the .npz file
file_path = "/Users/benorr/UCSFben/Consulting/Arcellx/multimer_InitialGuess/dl_binder_design/af2_initial_guess/params/params_model_1_multimer_v2.npz"

file_path2 = "/Users/benorr/UCSFben/Consulting/Arcellx/multimer_InitialGuess/dl_binder_design/af2_initial_guess/params/params_from_download_script/params_model_1_multimer_v3.npz"

# Load the .npz file
params = np.load(file_path, allow_pickle=True)

params2 = np.load(file_path2, allow_pickle=True)

# Print each parameter name and its shape
print("Haiku Parameters:")
mismatch_shapes = 0
for key, value in params.items():
    """
    # if 'prev_pos_linear' not in key: continue
    # if key != 'alphafold/alphafold_iteration/evoformer/preprocess_msa//weights': continue
    if isinstance(value, np.ndarray):
        print(f"Name: {key}, Shape: {value.shape}")
    else:
        print(f"Name: {key}, Type: {type(value)} (non-array content)")
    """
    shape = value.shape
    try:
        value2 = params2[key]
        print(f"\nParam names match: {key}")
        shape2 = value2.shape
        if shape != shape2:
            print(f"{key} has different shapes: {shape} vs. {shape2}")
            mismatch_shapes += 1
    except:
        print(f"{key} not found in params2")

print(f"Mismatch params shapes: {mismatch_shapes}")
