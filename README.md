# Hadoop and Mapreduce sample

This repository contains the code and data used when testing Hadoop and Mapreduce
It originates from the Udacity course: Intro to Hadoop and MapReduce 


## Preparing Haoop environment

Install the virtual machine as described in Lesson 3: HDFS and MapReduce, section 17 "Virtual Machine Setup"

Then copy the input file to hdfs (it is used in the map job)
```
hadoop fs -put data/purchases.txt myinput
```

## Develop and debugging the Python scripts

The simplest way of testing is to prepare a small sample file.  

```
tail -200 purchases.txt > samples.txt
```
or
```
head -200 purchases.txt > samples.txt
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


## Sales data tasks

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
| Sales breakdown by store | [`sales_per_store_mapper`](code/sales_per_store_mapper.py)  | [`total_per_key_reducer`](code/total_per_key_reducer.py)  |
| Sales breakdown by product category across all stores | `sales_per_category_mapper` | `total_per_key_reducer` |
| The monetary value for the highest individual sale for each separate store | `sales_per_store_mapper` | `max_per_key_reducer` |
| Total sales value across all the stores, and the total number of sales | `sales_per_store_mapper` | `total_per_key_reducer` |

## Log data tasks
The logfile is in Common Log Format:
```
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
```
Syntax:
```
%h %l %u %t \"%r\" %>s %b
```

Where:

- %h is the IP address of the client
- %l is identity of the client, or "-" if it's unavailable
- %u is username of the client, or "-" if it's unavailable
- %t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
- %r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
- %>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
- %b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.


| Description | Mapper | Reducer |
| :--- | :---  |:---  | 
| Display the number of hits for each different file on the web site | `log_url_mapper` | `total_per_key_reducer` |
| Display the number of hits for each client ip | `log_ip_address_mapper` | `total_per_key_reducer` |

Using command line to sort output:

```
hadoop fs -cat <output>/part-0000 | sort -k2
```

## Patterns
Get testdata:

```
curl http://content.udacity-data.com/course/hadoop/forum_data.tar.gz > forum_data.tar.gz
```
