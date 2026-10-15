def read_rows(lines):
    rows = []
    head = None
    for line in lines:
        row = {}
        line = line.strip().split(",")
        if len(line) != 3:
            continue
        if head is None:
            head = line
            continue
        for i in range(len(head)):
            row[head[i]] = line[i]
        rows.append(row)
    return rows

def count_types(rows):
    counts = {}
    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind] = 0;
        counts[kind] += 1;
    return counts

def total_minutes(rows, kind):
    total = 0.0
    for row in rows:
        if row["тип"] != kind:
            continue
        total += float(row["минуты"])
    return total

def to_csv(counts):
    lines = ["тип,количество"]
    for kind in sorted(counts):
        line = kind + "," + str(counts[kind])
        lines.append(line)
    return "\n".join(lines) + "\n"
