#!/usr/bin/python
"""
Your goal for this task is to write mapper and reducer code
that will combine some of the forum and user data.
In relational algebra, this is known as a join operation.
At the moment, this is not an auto-gradable exercise, but instructions below are given on how to test your code on your machine.

The goal is to have the output from the reducer with the following fields for each forum post:
"id"  "title"  "tagnames"  "author_id"  "node_type"  "parent_id"  "abs_parent_id"  "added_at"
"score"  "reputation"  "gold"  "silver"  "bronze"

Note that for each post we have taken some of the information describing the post,
and joined it with user information. The body of the post is not included in the final output.
The reason is that it is difficult to handle a multiline body, as it might be split on separate
lines during the intermediate steps Hadoop performs - shuffle and sort.

Your mapper code should take in records from both forum_node and forum_users.
It needs to keep, for each record, those fields that are needed for the final output given above.
In addition, mapper needs to add some text (e.g. "A" and "B") to mark where each output comes from
(user information vs forum post information). Example output from mapper is:

"12345"  "A"  "11"  "3"  "4"  "1"
"12345"  "B"   "6336" "Unit 1: Same Value Q"  "cs101 value same"  "question"  "\N"  "\N"  "2012-02-25 08:09:06.787181+00"  "1"

The first line originally comes from the forum_users input. It is from a student with user id: 12345 - the mapper key.
The next field is the marker A specifying that the record comes from forum_users.
What follows is the remaining information user information.

The second line originally comes from the forum_node input.
It also starts with the student id (mapper key) followed by a marker B and the information about the forum post.

The mapper key for both types of records is the student ID:
"user_ptr_id" from "forum_users" or  "author_id" from "forum_nodes" file.
Remember that during the sort and shuffle phases records will be grouped based on the student ID (12345 in our example).
You can use that to process and join the records appropriately in the reduce phase.
"""

import csv

from base import get_stream, close_stream


def mapper():
    type_forum_user = "A"
    type_forum_node = "B"

    stream = get_stream()
    reader = csv.reader(stream, delimiter='\t')

    for line in reader:
        if len(line) == 5:
            user_ptr_id, reputation, gold, silver, bronze = line
            try:
                int(user_ptr_id)
                print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(user_ptr_id, type_forum_user, reputation, gold, silver,
                                                            bronze)
            except ValueError:
                print("Skipping line")
        elif len(line) > 9:
            # just pick the first 10 elements
            post_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at = line[:9]
            try:
                int(post_id)
                print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(author_id, type_forum_node, post_id, title,
                                                                           tagnames,
                                                                           node_type, parent_id, abs_parent_id,
                                                                           added_at)
            except ValueError:
                print("Skipping line")

    close_stream(stream)


def main():
    mapper()


if __name__ == "__main__":
    main()
