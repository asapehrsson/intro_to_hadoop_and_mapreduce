# Hadoop and Mapreduce sample

This repository contains the code and data used when testing Hadoop and Mapreduce
It originates from the Udacity course: Intro to Hadoop and MapReduce 


## Preparing Haoop environment

Install the virtual machine as described in Lesson 3: HDFS and MapReduce, section 17 "Virtual Machine Setup"

## Running the scripts without Hadoop

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

##### Sales breakdown by store

Solved by `total_sales_per_store_mapper` and `total_per_key_reducer`
Run by
```
hs ./total_sales_per_store_mapper.py ./total_per_key_reducer.py myinput/purchases.txt output_sbbs   
```

#####  Sales breakdown by product category across all of our stores.
#####  The monetary value for the highest individual sale for each separate store.
#####  Total sales value across all the stores, and the total number of sales.