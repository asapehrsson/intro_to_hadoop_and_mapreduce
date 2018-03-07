#!/usr/bin/python
# Combine the values that come from 2 sources

from base import get_stream, close_stream


def reducer():
    question_length = 0
    total_answers_length = 0
    no_of_answers = 0
    old_id = None
    stream = get_stream()

    for line in stream:
        data_mapped = line.strip().split("\t")

        data_len = len(data_mapped)
        if data_len != 3:
            # Skip this line.
            continue

        this_id, this_type, this_length = data_mapped

        # special case - first key
        if old_id is None:
            old_id = this_id

        if old_id != this_id:
            print_result(old_id, question_length, total_answers_length, no_of_answers)
            old_id = this_id
            question_length = 0
            total_answers_length = 0
            no_of_answers = 0

        if this_type == "answer":
            total_answers_length += float(this_length)
            no_of_answers += 1
        else:
            question_length = float(this_length)

        # special case - last key
    print_result(old_id, question_length, total_answers_length, no_of_answers)

    close_stream(stream)


def print_result(id, question_length, total_answers_length, no_of_answers):
    if question_length > 0:
        # using ternary conditional operator
        mean_answer_length = total_answers_length / no_of_answers if no_of_answers > 0 else 0

        print "{0}\t{1}\t{2}".format(id, question_length, mean_answer_length)


def main():
    reducer()


if __name__ == "__main__":
    main()
