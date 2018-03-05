# Hadoop and Mapreduce sample

This repository contains the code and data used when testing Hadoop and Mapreduce
It originates from the Udacity course: Intro to Hadoop and MapReduce 


## Preparing Haoop environment

Install the virtual machine as described in Lesson 3: HDFS and MapReduce, section 17 "Virtual Machine Setup"

Then copy the input file to hdfs (it is used in the map job)
```
hadoop fs -mv data/purchases.txt myinput
```

## Develop and debugging the Python scripts

The simplest way of testing is to prepare a small sample file.  

```
tail -200 purchases.txt > samples.txt
```

### Testing individual script

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

### Testing the pipeline

Prepare a small sample file that is piped (or used as command line argument)

```
cat ../data/samples.txt | ./mapper.py | sort | ./reducer.py
```


## Tasks

Syntax:

```
hadoop jar hadoop-streaming.jar -mapper mapper.py -reducer reducer.py -file base.py -file mapper.py -file reducer.py -input inputfile -output outputfolder
```

Example, in `code` folder:

```
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper ./sales_per_store_mapper.py -reducer ./total_per_key_reducer.py -file ./base.py -file ./sales_per_store_mapper.py -file ./total_per_key_reducer.py -input myinput -output sbbs1
```

Check the result:

```
hadoop fs -cat outputfolder/part-00000
```


| Description | Mapper | Reducer |
| :--- | :---  |:---  | 
| Sales breakdown by store | `sales_per_store_mapper` | `total_per_key_reducer` |
| Sales breakdown by product category across all stores | `sales_per_category_mapper` | `total_per_key_reducer` |
| The monetary value for the highest individual sale for each separate store | `sales_per_store_mapper` | `highest_per_key_reducer` |
| Total sales value across all the stores, and the total number of sales | `sales_per_store_mapper` | `total_reducer` |


