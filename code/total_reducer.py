#!/usr/bin/python

from base import get_stream, close_stream


# Just sum everything
def reducer():
    sales_total = 0
    no_of_sales = 0

    stream = get_stream()
    for line in stream:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Skip this line.
            continue

        this_key, this_sale = data_mapped

        sales_total += float(this_sale)
        no_of_sales += 1

    print no_of_sales, "\t", sales_total

    close_stream(stream)


def main():
    reducer()


if __name__ == "__main__":
    main()
