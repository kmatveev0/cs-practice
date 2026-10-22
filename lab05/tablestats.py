from typing import Dict, List

def read_rows(lines: List[str]) -> List[Dict]:
    rows = []
    head = []

    for line in lines:
        row = {}
        line = line.strip()

        if not line:
            continue

        if not head:
            head = line.split(",")
            continue

        line = line.split(",")

        if len(line) != len(head):
            continue

        for i in range(len(head)):
            row[head[i]] = line[i]

        rows.append(row)

    return rows


def count_types(rows: List[Dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind] = 0
        counts[kind] += 1
    return counts


def total_minutes(rows: List[Dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row["тип"] != kind:
            continue
        try:
            total += float(row["минуты"].replace(",", "."))
        except:
            continue
    return round(total, 1)


def to_csv(counts: dict) -> str:
    lines = ["тип,количество"]
    for kind in sorted(counts):
        line = kind + "," + str(counts[kind])
        lines.append(line)
    return "\n".join(lines) + "\n"
