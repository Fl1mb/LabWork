
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_f:
        csv_reader = csv.reader(csv_f, lineterminator= '\n' ,delimiter=',')
        headers = next(csv_reader)
        data = []

        for row in csv_reader:
            row_data = {}
            for i, header in enumerate(headers):
                row_data[header] = row[i]
            data.append(row_data)
        with open(OUTPUT_FILENAME, 'w') as json_f:
            json.dump(data, json_f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
