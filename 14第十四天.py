import os
import csv
import time
import pandas as pd
import concurrent.futures

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"程序运行时间：{end_time - start_time}秒")
        return result
    return wrapper

def count_words(filename):
    word_count = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

@measure_time
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_paths = [os.path.join(current_dir, filename) for filename in os.listdir(current_dir) if filename.endswith('.txt')]
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as process_pool:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as thread_pool:
            process_results = [process_pool.submit(count_words, file_path) for file_path in file_paths]
            word_counts = [process_result.result() for process_result in process_results]
            
            
            combined_word_count = {}
            for word_count in word_counts:
                for word, count in word_count.items():
                    if word in combined_word_count:
                        combined_word_count[word] += count
                    else:
                        combined_word_count[word] = count
            
            
            csv_filename = os.path.join(current_dir, 'word_count.csv')
            with open(csv_filename, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Word', 'Count'])
                for word, count in combined_word_count.items():
                    writer.writerow([word, count])
            
            
            df = pd.read_csv(csv_filename)
            print(df)

if __name__ == '__main__':
    main()
