from tablestats import *

with open(input().strip(), "r", encoding="utf-8") as f:
    lines = f.readlines()
    rows = read_rows(lines)
    print(len(rows))
    counts = count_types(rows)
    print(len(counts))
    total = total_minutes(rows,"ошибка")
    print(total)

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(counts))
