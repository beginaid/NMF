import numpy as np
import matplotlib.pyplot as plt
import sys

class NMF():
    def __init__(self, Y, M):
        self.eps = np.spacing(1)
        self.Y = Y
        self.M = M

    def init_params(self):
        self.cost_tmp = 10**6
        self.cost = np.array([self.cost_tmp])
        self.cnt_iteration = 1

    def init_matrix(self):
        self.H = np.random.uniform(low=1, high=10, size=(self.Y.shape[0], self.M)) # (L, M)
        self.U = np.random.uniform(low=1, high=10, size=(self.M, self.Y.shape[1])) # (M, N)
        self.X = self.H @ self.U # (L, N)

    def EU_divergence(self):
        self.cost_tmp = ((self.X-self.Y)**2).mean()

    def I_divergence(self):
        self.cost_tmp = (self.Y*np.log(self.Y/(self.X+self.eps)+self.eps)-self.Y+self.X).mean()

    def IS_divergence(self):
        self.cost_tmp = (self.Y/(self.X+self.eps)-np.log(self.Y/(self.X+self.eps)+self.eps)-1).mean()

    def EU_update(self):
        self.H *= (self.Y @ self.U.T) / ((self.H @ self.U) @ self.U.T + self.eps)
        self.U *= (self.Y.T @ self.H).T / ((self.H @ self.U).T @ self.H + self.eps).T

    def I_update(self):
        self.H *= ((self.Y / ((self.H @ self.U) + self.eps)) @ self.U.T)  / (self.U.sum(axis=1, keepdims=True).T + self.eps)
        self.U *= ((self.Y / ((self.H @ self.U) + self.eps)).T @ self.H).T  / (self.H.sum(axis=0, keepdims=True).T + self.eps)

    def IS_update(self):
        self.H *= np.sqrt(((self.Y / ((self.H @ self.U)**2 + self.eps)) @ self.U.T) / (self.U @ (1/((self.H @ self.U) + self.eps)).T + self.eps).T)
        self.U *= np.sqrt(((self.Y / ((self.H @ self.U)**2 + self.eps)).T @ self.H).T / (self.H.T @ (1/((self.H @ self.U) + self.eps)) + self.eps))

    def execute(self, n_iteration, divergence):
        while True:
            if (divergence=="EU"):
                self.EU_update()
                self.EU_divergence()
            elif (divergence=="I"):
                self.I_update()
                self.I_divergence()
            elif (divergence=="IS"):
                self.IS_update()
                self.IS_divergence()
            else:
                print("Please select from EU, I, or IS for the divergence.")
                sys.exit(1)

            if (self.cnt_iteration >= n_iteration or self.cost_tmp > self.cost[-1]):
                print(f"====={self.cnt_iteration}回目でcostが悪化したため終了=====")
                break
            else:
                self.X = self.H @ self.U
                self.cost = np.append(self.cost, self.cost_tmp)
                self.cnt_iteration += 1

    def visualize_cost(self):
        index = np.arange(self.cost.size-2)
        plt.figure(figsize=(16,9))
        plt.rcParams["font.size"] = 18
        plt.plot(index, self.cost[2:], color=(0.93,0.27,0.17))

    def visualize_heatmap(self):
        fig, axes = plt.subplots(1, 2, figsize=(16,9))
        fig.subplots_adjust(wspace=0.1, hspace=0.1)
        axes[0].imshow(self.Y, cmap="inferno")
        axes[0].axis("off")
        axes[1].imshow(self.X, cmap="inferno")
        axes[1].axis("off")
        plt.show()
