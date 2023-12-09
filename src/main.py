import os
import numpy as np
import fire
import NMF


def create_data(L, N):
    """Create a matrix to apply the NMF.
    Args:
        L (int): Rows of observation matrix.
        N (int): Columns of observation matrix.
    Returns:
        Y (numpy ndarray): Input data whose size is (L, N).
    Note:
        The range of values for each element of matrix Y is [1,10].
    """
    return np.random.randint(1, 10, (L, N))


def main(L, M, N, n_iteration, divergence):
    """Execute NMF.
    Args:
        M (int): Rows of basis matrix.
        divergence (string): "EU", "I", or "IS".
    Returns:
        None.
    Note:
        The output is a result of plotting with matplotlib.
    """
    if not os.path.isdir("results"):
        os.makedirs("results")
    Y = create_data(L, N)
    model = NMF.NMF(Y, M)
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
