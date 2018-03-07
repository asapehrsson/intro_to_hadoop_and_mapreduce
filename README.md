# Hadoop and Mapreduce sample

This repository contains the code and data used when testing Hadoop and Mapreduce
It originates from the Udacity course: Intro to Hadoop and MapReduce 


## Preparing Haoop environment

Install the virtual machine as described in Lesson 3: HDFS and MapReduce, section 17 "Virtual Machine Setup"

Then copy the input file to hdfs (it is used in the map job)
```
hadoop fs -put data/purchases.txt myinput
```

Running mapreduce:

```
hadoop jar hadoop-streaming.jar -mapper mapper.py -reducer reducer.py -file base.py -file mapper.py -file reducer.py -input inputfile -output outputfolder
```

## Sales data tasks
Data file: data/purchases.txt.gz

| Description | Mapper | Reducer |
| :--- | :---  |:---  | 
| Sales breakdown by store | [`sales_per_store_mapper`](code/sales_per_store_mapper.py)  | [`total_per_key_reducer`](code/total_per_key_reducer.py)  |
| Sales breakdown by product category across all stores | [`sales_per_category_mapper.py`](code/sales_per_category_mapper.py) | [`total_per_key_reducer`](code/total_per_key_reducer.py) |
| The monetary value for the highest individual sale for each separate store | [`sales_per_store_mapper`](code/sales_per_store_mapper.py) | [`max_per_key_reducer`](code/max_per_key_reducer.py) |
| Total sales value across all the stores, and the total number of sales | [`sales_per_store_mapper`](code/sales_per_store_mapper.py) | [`total_reducer`](code/total_reducer.py) |
| Average sales value across all the stores, per weekday | [`sales_per_weekday_mapper`](code/sales_per_weekday_mapper.py) | [`total_reducer`](code/total_reducer.py) |
| Using combiner: sum of sales value across all the stores, per weekday | [`sales_per_weekday_mapper`](code/sales_per_weekday_mapper.py) | **both combiner and reducer:** [`total_reducer`](code/total_reducer.py) |

## Log data tasks
Data file access_log.gz

| Description | Mapper | Reducer |
| :--- | :---  |:---  | 
| Display the number of hits for each different file on the web site | [`log_url_mapper`](code/log_url_mapper.py) | [`total_per_key_reducer`](code/total_per_key_reducer.py) |
| Display the number of hits for each client ip | [`log_ip_address_mapper`](code/log_ip_address_mapper.py) | [`total_per_key_reducer`](code/total_per_key_reducer.py)| 


## Forum data tasks
Data file forum_data.tar.gz. Get data by:

```
curl http://content.udacity-data.com/course/hadoop/forum_data.tar.gz > forum_data.tar.gz
```

| Description | Mapper | Reducer |
| :--- | :---  |:---  | 
| Count number of nodes where 'body' either has NO [.!?] OR exact one in last position | [`forum_csv_filter_mapper`](code/forum_csv_filter_mapper.py) | N/A |
| Print out 10 lines containing longest posts, sorted in ascending order from shortest to longest | [`forum_csv_body_max_n_mapper`](code/forum_csv_body_max_n_mapper.py) | N/A |
| Create an index of all the words find in the body of a post. Show times used.  | [`forum_csv_dictionary_mapper` (what=number)](code/forum_csv_dictionary_mapper.py) | [`dictionary_index_reducer`](code/dictionary_index_reducer.py) |
| Create an index of all the words find in the body of a post. Show used by.  | [`forum_csv_dictionary_mapper` (what=source)](code/forum_csv_dictionary_mapper.py) | [`dictionary_index_reducer`](code/dictionary_index_reducer.py) |
| Combine some of the forum and user data (aka join). See details in mapper.  |[`forum_combiner_mapper`](code/forum_combiner_mapper.py) |[`forum_combiner_reducer` ](code/forum_combiner_reducer.py) |
| For each student: what is the hour during which the student has posted the most posts|[`forum_student_hour_mapper`](code/forum_student_hour_mapper.py)|[`key_per_hour_reducer` ](code/key_per_hour_reducer.py)|
| Correlation between question body length and answer length|[`forum_post_and_answer_length_mapper`](code/forum_post_and_answer_length_mapper.py)|[`forum_post_and_answer_length_reducer` ](code/forum_post_and_answer_length_reducer.py)|

## Command line stuff

Using command line to sort output:

```
hadoop fs -cat <output>/part-0000 | sort -k2
```

#### Develop and debugging the Python scripts

The simplest way of testing is to prepare a small sample file.  

```
tail -200 purchases.txt > samples.txt
```
or
```
head -200 purchases.txt > samples.txt
```

#### Testing individual script

Pipe the small sample file - or as command line argument

```
cat ../data/samples.txt | ./mapper.py 
```

or

```
./mapper.py ../data/samples.txt  
```

or just enter the input line by line (tab between arguments) and then Cmd-D
```
./mapper.py   
```

#### Testing the pipeline

Prepare a small sample file that is piped (or used as command line argument)

```
cat ../data/samples.txt | ./mapper.py | sort | ./reducer.py
```


#### Example running mapreduce and get the result:

Example, in `code` folder:

```
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper ./sales_per_store_mapper.py -reducer ./total_per_key_reducer.py -file ./base.py -file ./sales_per_store_mapper.py -file ./total_per_key_reducer.py -input myinput -output sbbs1
```

Check the result:

```
hadoop fs -cat outputfolder/part-00000
```
