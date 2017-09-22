hadoop fs -put /home/sonalis772/test/full_train.txt /user/sonalis772/ques1/train/
./NB_hadoop.py -r hadoop --hadoop-streaming-jar /usr/hdp/2.6.1.0-129/hadoop-mapreduce/hadoop-streaming.jar --hadoop-bin /usr/bin/hadoop --jobconf mapred.reduce.tasks=10 --jobconf mapred.map.tasks=10 hdfs:///user/sonalis772/ques1/train/full_train.txt >> /home/sonalis772/out1.txt
