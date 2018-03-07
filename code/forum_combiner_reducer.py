#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

from base import get_stream, close_stream


def reducer():
    user_data = []
    forum_data = []
    old_id = None
    stream = get_stream()

    for line in stream:
        data_mapped = line.strip().split("\t")

        data_len = len(data_mapped)
        if not (data_len == 5 or data_len == 9):
            # Skip this line.
            continue
        this_id = data_mapped[0]
        this_type = data_mapped[1]

        # special case - first key
        if old_id is None:
            old_id = this_id

        if old_id != this_id:
            print_result(forum_data, user_data)
            old_id = this_id
            user_data = []
            forum_data = []

        if this_type == "A":
            forum_data.append(data_mapped)
        else:
            user_data = data_mapped

    # special case - last key
    print_result(forum_data, user_data)

    close_stream(stream)


def print_result(forum_data, user_data):
    if len(user_data) == 6:
        user_ptr_id, type_forum_user, reputation, gold, silver, bronze = user_data

        for node in forum_data:
            if len(node) == 9:
                author_id, type_forum_node, post_id, title, tagnames, node_type, parent_id, abs_parent_id, added_at = node

                print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}".format(author_id, post_id, title,
                                                                                            tagnames,
                                                                                            node_type, parent_id,
                                                                                            abs_parent_id, added_at,
                                                                                            reputation, gold, silver,
                                                                                            bronze)


def main():
    reducer()


if __name__ == "__main__":
    main()
