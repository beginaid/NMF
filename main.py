import numpy as np
import fire
import NMF

def createData(L, N):
    """Create .
    Args:
        None.
    Returns:
        Y (numpy ndarray): Input data whose size is (, ).
    """
    return np.random.randint(1, 10, (L, N))

def main(L, M, N, n_iteration, divergence):
    """Execute NMF.
    Args:
        M (int):
        divergence (string): "", "", or "".
    Returns:
        None.
    """
    Y = createData(L, N)
    model = NMF(Y, M)
    while True:
        model.init_matrix()
        model.init_params()
        model.execute(n_iteration, divergence)
        if model.cnt_iteration == n_iteration:
            break
    model.visualize_cost()
    model.visualize_heatmap()

if __name__ == "__main__":
    fire.Fire(main)
