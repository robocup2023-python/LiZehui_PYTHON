def calculate(*args):
    avg = sum(args) / len(args)
    above_avg = [i for i, num in enumerate(args) if num > avg]
    return avg, above_avg

result = calculate(1, 2, 3, 4, 5)
print("平均值:", result[0])
print("大于平均值的索引:", result[1])



def calculate(*args):
    avg = sum(args) / len(args)
    above_avg = [i for i, num in enumerate(args) if num > avg]
    return avg, above_avg

result = calculate(1, 2, 3, 4, 5)
print("平均值:", result[0])
print("大于平均值的索引:", result[1])




import os

def create_files():
    directory = "./img"
    os.makedirs(directory, exist_ok=True)

    for i in range(1, 101):
        filename = "X{}G{}.png".format(i // 10, i % 10)
        filepath = os.path.join(directory, filename)
        with open(filepath, "w") as file:
            file.write("This is file {}".format(i))

create_files()




import os
import random

def rename_files():
    directory = "./img"
    filenames = os.listdir(directory)
    random.shuffle(filenames)

    for i, filename in enumerate(filenames[:50]):
        new_filename = filename.split(".")[0] + ".jpg"
        filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        os.rename(filepath, new_filepath)

rename_files()
