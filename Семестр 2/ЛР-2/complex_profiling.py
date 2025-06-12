import random
import timeit
import matplotlib.pyplot as plt
from pathlib import Path
from recursive import gen_bin_tree as recursive_gen
from nonrecursive import gen_bin_tree as nonrecursive_gen

def save_plot(fig, filename):
    results_dir = Path(__file__).parent.parent / "results"
    results_dir.mkdir(exist_ok=True)
    fig.savefig(results_dir / filename)
    plt.close(fig)

def setup_data(n, seed=42):
    random.seed(seed)
    return [(random.randint(1, 100), random.randint(1, 15)) for _ in range(n)]

def run_profiling():
    sizes = range(10, 51, 10)  # Уменьшен диапазон
    n_runs = 20  # Уменьшено количество прогонов
    test_data = {size: setup_data(size) for size in sizes}
    
    rec_times = []
    it_times = []
    
    for size in sizes:
        data = test_data[size]
        
        # Прогрев
        recursive_gen(*data[0])
        nonrecursive_gen(*data[0])
        
        rec_time = timeit.timeit(
            lambda: [recursive_gen(r, h) for r, h in data],
            number=n_runs
        )
        
        it_time = timeit.timeit(
            lambda: [nonrecursive_gen(r, h) for r, h in data],
            number=n_runs
        )
        
        rec_times.append(rec_time)
        it_times.append(it_time)
    
    # Построение графика
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(sizes, rec_times, 'o-', label='Рекурсивная')
    ax.plot(sizes, it_times, 's-', label='Нерекурсивная')
    ax.set_title("Сравнение времени выполнения (20 прогонов)")
    ax.set_xlabel("Количество тестовых случаев")
    ax.set_ylabel("Время (с)")
    ax.legend()
    ax.grid(True)
    save_plot(fig, "profiling_results.png")

if __name__ == "__main__":
    run_profiling()