VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:

    stripped = line.strip()
    if not stripped:
        raise ValueError("Пустая строка")

    parts = stripped.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Недостаточно элементов в строке")

    time, level, message = parts
    if level not in VALID_LEVELS:
        raise ValueError(f"Неизвестный уровень логирования: {level}")

    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:

    counts = {level: 0 for level in VALID_LEVELS}
    counts["BROKEN"] = 0

    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1

    return counts


def top_errors(lines, n: int) -> list[list]:

    error_counts = {}

    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue


    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))


    return [[msg, count] for msg, count in sorted_errors[:n]]


def format_report(counts: dict, errors: list[list]) -> str:

    report_lines = ["Отчёт по журналу", ""]

    for level in sorted(counts.keys()):
        report_lines.append(f"{level}: {counts[level]}")

    report_lines.append("")
    report_lines.append("Частые ошибки:")

    for msg, count in errors:
        report_lines.append(f"- {msg} — {count}")

    return "\n".join(report_lines) + "\n"