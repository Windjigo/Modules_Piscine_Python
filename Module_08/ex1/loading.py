ret = 1
try:
    import pandas as pd
    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
except ModuleNotFoundError:
    print("Error panda - No data manipulation tool available")
    ret = 0
try:
    import numpy as np
    print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
except ModuleNotFoundError:
    print("Error numpy - No numerical computation tool available")
    ret = 0
try:
    import matplotlib.pyplot as plt
    import matplotlib
    print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
except ModuleNotFoundError:
    print("Error matplotlib - No visualization tool available")
    ret = 0


def main() -> None:
    if (ret == 0):
        print("\nYou don't have all the dependencies required.")
        print("To install with pip, use:\npip \
install -r + requirements.txt emplacement")
        print("To install with poetry, use:\npoetry \
install\npoetry run python loading.py")
        return
    print("\nAnalyzing Matrix data...\nProcessing \
500 data points...\nGenerating visualization...")
    RNG = np.random.default_rng(seed=42)
    N = 500  # number of observations
    raw = RNG.standard_normal((N, 2))

    time_idx = np.linspace(0, 4 * np.pi, N)
    signal = np.sin(time_idx) + 0.3 * np.cos(3 * time_idx)
    noise = RNG.normal(0, 0.25, N)

    raw[:, 0] = time_idx                                      # time
    raw[:, 1] = signal + noise                                # noisy signal

    cols = ["time", "signal"]
    df = pd.DataFrame(raw, columns=cols)
    df["rolling_signal"] = df["signal"].rolling(window=20, center=True).mean()

    GREEN = "#00ff41"
    TEAL = "#00e5cc"
    plt.figure(figsize=(16, 10))
    plt.plot(df["time"], df["signal"], color=GREEN, lw=0.8, label="Raw signal")
    plt.plot(df["time"], df["rolling_signal"],
             color=TEAL, lw=1.8, label="Rolling mean (w=20)")
    # rolling mean = average of the last 20 points
    plt.suptitle("SIGNAL OVER TIME")
    plt.xlabel("Time (rad)")
    plt.ylabel("Amplitude")
    plt.legend(fontsize=10)
    plt.grid(True)

    out = "matrix_analysis.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    print(f"\nAnalysis complete!\nResults saved to: {out}")
    plt.close()


if __name__ == "__main__":
    main()
