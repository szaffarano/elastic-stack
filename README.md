# ELK Proof of concept 

Some tests with Elasticsearch, Kibana and Logstash.

## Usage

Install docker-compose and run

```sh
$ docker-compose up -d es1 es2 kibana logstash
```

Wait a while and Kibana will be listening on http://localhost:5601

## Generate some data

The POC is configured to use three logstash pipelines.  The first one look at `logs/access_log` folder, but this file doesn't exist in the repo.  Move the sample file to get some apache logs input data:

```sh
$ mv logs/access_log.example logs/access_log
```

Or better, generate a big apache log file duplicating N times this file but changing the date:

```sh
# generate an access_log file 50 times bigger than access_log.example
$ bin/generator.py logs/access_log.example 50 logs/access_log
```
The second pipeline reads `*.csv` files, so rename ./logs/test.csv.example to `./logs/test.csv` and logstash will read it.

The third pipeline just listens for filebeat events and print out them to stdout, so, you can use `./bin/filebeat.sh` to test it.  See `./config/filebeat/filebeat.yml` for details about how filebeat is configured.
