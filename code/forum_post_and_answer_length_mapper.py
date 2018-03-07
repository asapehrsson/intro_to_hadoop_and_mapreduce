#!/usr/bin/python
"""
The ones that are the most relevant to the task are:

"id": id of the node
"title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
"tagnames": space separated list of tags
"author_id": id of the author
"body": content of the post
"node_type": type of the node, either "question", "answer" or "comment"
"parent_id": node under which the post is located, will be empty for "questions"
"abs_parent_id": top node where the post is located
"added_at": date added
"""

import csv

from base import get_stream, close_stream


def mapper():
    stream = get_stream()
    reader = csv.reader(stream, delimiter='\t')

    for line in reader:
        if len(line) > 9:
            # just pick needed elements
            post_id, title, tagnames, author_id, body, node_type, parent_id = line[:7]
            try:
                if node_type == "question":
                    print "{0}\t{1}\t{2}".format(post_id, node_type, len(body))

                elif node_type == "answer":
                    print "{0}\t{1}\t{2}".format(parent_id, node_type, len(body))

            except ValueError:
                print("Skipping line")

    close_stream(stream)


def main():
    mapper()


if __name__ == "__main__":
    main()
