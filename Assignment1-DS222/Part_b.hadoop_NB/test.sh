awk '{printf "%d\t%s\n", NR, $0}' < /home/sonalis772/test/full_devel.txt >> /home/sonalis772/test/full_devel_id.txt
hadoop fs -put /home/sonalis772/test/full_devel_id.txt /user/sonalis772/ques1/train/
hadoop fs -put /home/sonalis772/out1.txt /user/sonalis772/ques1/train/
hadoop jar /usr/hdp/2.6.1.0-129/hadoop-mapreduce/hadoop-streaming.jar \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-D stream.map.output.field.separator=' ' \
-D stream.num.map.output.key.fields=1 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-jobconf mapred.map.tasks=10 \
-jobconf mapred.reduce.tasks=10 \
-file /home/sonalis772/project/python-ngrams-master/mrjob/final1/mapper.py   -mapper /home/sonalis772/project/python-ngrams-master/mrjob/final1/mapper.py \
-file /home/sonalis772/project/python-ngrams-master/mrjob/final1/reducer-changed.py   -reducer /home/sonalis772/project/python-ngrams-master/mrjob/final1/reducer-changed.py \
-input hdfs:///user/sonalis772/ques1/train/full_devel_id.txt -input hdfs:///user/sonalis772/ques1/train/out1.txt -output hdfs:///user/sonalis772/ques1/out1

hadoop fs -cat ques1/out1/* >> /home/sonalis772/res1/out1.txt
sort  /home/sonalis772/res1/out1.txt >> /home/sonalis772/res1/out2.txt
tail -100 /home/sonalis772/res1/out2.txt >> /home/sonalis772/res1/dict1.txt
hadoop fs -put /home/sonalis772/res1/dict1.txt /user/sonalis772/ques1/train/


hadoop jar /usr/hdp/2.6.1.0-129/hadoop-mapreduce/hadoop-streaming.jar \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-D stream.map.output.field.separator=' ' \
-D stream.num.map.output.key.fields=1 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-jobconf mapred.map.tasks=10 \
-jobconf mapred.reduce.tasks=10 \
-file /home/sonalis772/project/python-ngrams-master/mrjob/final1/mapper1.py   -mapper /home/sonalis772/project/python-ngrams-master/mrjob/final1/mapper1.py \
-file /home/sonalis772/project/python-ngrams-master/mrjob/final1/reducer1.py   -reducer /home/sonalis772/project/python-ngrams-master/mrjob/final1/reducer1.py \
-input hdfs:///user/sonalis772/ques1/out1/*  -output hdfs:///user/sonalis772/ques1/out2


hadoop fs -put /home/sonalis772/dict.txt /user/sonalis772/ques1/train/

hadoop jar /usr/hdp/2.6.1.0-129/hadoop-mapreduce/hadoop-streaming.jar \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-D stream.map.output.field.separator=' ' \
-D stream.num.map.output.key.fields=1 \
-cacheFile hdfs:///user/sonalis772/ques1/train/dict1.txt#ref \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-jobconf mapred.map.tasks=10 \
-jobconf mapred.reduce.tasks=10 \
-file /home/sonalis772/project/python-ngrams-master/mrjob/final1/mapper2.py   -mapper /home/sonalis772/project/python-ngrams-master/mrjob/final1/mapper2.py \
-file /home/sonalis772/project/python-ngrams-master/mrjob/final1/reducer2.py   -reducer /home/sonalis772/project/python-ngrams-master/mrjob/final1/reducer2.py \
-input hdfs:///user/sonalis772/ques1/out2/*  -output hdfs:///user/sonalis772/ques1/out3


hadoop fs -cat ques1/out3/* >> /home/sonalis772/res1/out_final_devel.txt
