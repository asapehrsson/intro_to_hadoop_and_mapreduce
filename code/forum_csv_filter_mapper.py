#!/usr/bin/python
import csv
import sys

from base import get_stream, close_stream

# Content of each line is (separated by the \t character):
# id | title | tagnames | author_id | body | node_type parent_id | abs_parent_id
#    | added_at score state_string | last_edited_id | last_activity_by_id | last_activity_at
#    | active_revision_id | extra | extra_ref_id | extra_count | marked
#
# The data in at least one of the fields (the body field) can include newline
# characters, and all the fields are enclosed in double quotes.
#
# In this exercise, we are interested in the field 'body' (which is the 5th field,
# line[4]). The objective is to count the number of forum nodes where 'body' either
# contains none of the three punctuation marks: period ('.'), exclamation point ('!'),
# question mark ('?'), or else 'body' contains exactly one such punctuation mark as the
# last character. There is no need to parse the HTML inside 'body'. Also, do not pay
# special attention to newline characters.


test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"This is one sentence\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Also one sentence!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Hey!\nTwo sentences!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One. Two! Three?\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One Period. Two Sentences\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Three\nlines, one sentence\n\"\t\"\"
"""
characters = set('[!?.]+$')


def match_none_or_single_in_last_position(body):
    result = False
    if len(body) > 0:
        no = body.count('!') + body.count('?') + body.count('.')
        if no == 0:
            result = True
        elif no == 1:
            last = body.strip()[-1]
            if characters.intersection(last):
                result = True

    return result


def mapper():
    # debug by passing test_text as argument to get_stream()
    stream = get_stream()
    reader = csv.reader(stream, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) > 4:
            body = line[4]
            if match_none_or_single_in_last_position(body):
                writer.writerow(line)

    close_stream(stream)


def main():
    mapper()


if __name__ == "__main__":
    main()
