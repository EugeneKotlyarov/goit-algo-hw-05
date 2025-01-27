import timeit
from boyer_moore import boyer_moore
from kmp_search import kmp_search
from rabin_karp import rabin_karp


def main():
    file1_path = "03_article_1.txt"
    file2_path = "03_article_1.txt"

    with open(file1_path) as f:
        text1 = f.read()

    with open(file2_path) as f:
        text2 = f.read()

    pattern_existing = "алгоритми"
    pattern_fabricated = "неіснуючийпідрядок"

    results = {"Article 1": {}, "Article 2": {}}

    for text, article in zip([text1, text2], ["Article 1", "Article 2"]):
        for algo_name, algo in [
            ("B-M", boyer_moore),
            ("KMP", kmp_search),
            ("R-K", rabin_karp),
        ]:
            for substring_type, substring in [
                ("real", pattern_existing),
                ("fict", pattern_fabricated),
            ]:
                time_taken = timeit.timeit(lambda: algo(text, substring), number=10)
                results[article][f"{algo_name} ({substring_type})"] = time_taken

    for article, timings in results.items():
        print(f"\nResults for {article}:")
        for desc, time in timings.items():
            print(f"├── {desc}:\t{time:.6f} sec")


if __name__ == "__main__":
    main()
