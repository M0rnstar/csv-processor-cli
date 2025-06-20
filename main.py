from csv_processor import (
    parse_args,
    read_csv,
    apply_filter,
    apply_aggregation,
    print_table,
)


def main():
    args = parse_args()

    try:
        data = read_csv(args.file)
    except FileNotFoundError:
        print(f"Ошибка: файл '{args.file}' не найден.")
        return

    if args.filter:
        data = apply_filter(data, args.filter)

    if args.aggregate:
        result = apply_aggregation(data, args.aggregate)
        print(f"Агрегация ({args.aggregate}): {result}")
        return

    print_table(data)


if __name__ == "__main__":
    main()
