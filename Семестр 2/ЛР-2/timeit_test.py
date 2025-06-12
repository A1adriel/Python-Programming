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

def run_timeit():
    test_cases = [(5,3), (10,5), (15,7), (20,10)]
    number = 500  # Уменьшено для скорости
    
    print("Timeit тестирование (мс):")
    print(f"{'Параметры':<15} {'Рекурсивная':<15} {'Нерекурсивная':<15}")
    
    rec_times = []
    it_times = []
    
    for root, height in test_cases:
        # Предварительный прогрев
        recursive_gen(root, height)
        nonrecursive_gen(root, height)
        
        rec_time = timeit.timeit(
            lambda: recursive_gen(root, height),
            number=number
        ) * 1000
        
        it_time = timeit.timeit(
            lambda: nonrecursive_gen(root, height),
            number=number
        ) * 1000
        
        rec_times.append(rec_time)
        it_times.append(it_time)
        print(f"({root},{height}): {rec_time:>10.3f} {it_time:>10.3f}")
    
    # Построение графика
    fig, ax = plt.subplots(figsize=(10, 5))
    x = [f"({r},{h})" for r, h in test_cases]
    ax.bar(x, rec_times, width=0.4, label='Рекурсивная')
    ax.bar(x, it_times, width=0.4, label='Нерекурсивная', alpha=0.7)
    ax.set_title("Сравнение времени выполнения (500 прогонов)")
    ax.set_ylabel("Время (мс)")
    ax.legend()
    save_plot(fig, "timeit_results.png")

if __name__ == "__main__":
    run_timeit()