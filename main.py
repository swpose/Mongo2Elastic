from subprocess import call
import sys

string = """var source = mongodb({
  //"uri": "${MONGODB_URI}"
  "uri": 'mongodb://localhost/${}'
  "timeout": "36000s",
  // "tail": false,
  // "ssl": false,
  // "cacerts": ["/path/to/cert.pem"],
  // "wc": 1,
  // "fsync": false,
  // "bulk": false,
  // "collection_filters": "{}",
  // "read_preference": "Primary"
})

var sink = elasticsearch({
  //"uri": "${ELASTICSEARCH_URI}"
  "uri": 'http://{id}:{pw}@{your_db_address}:9200/${}'
  //"uri": 'http://{your_db_address}:9200/{your_index}'
  "timeout": "1000000s", // defaults to 30s
  // "aws_access_key": "ABCDEF", // used for signing requests to AWS Elasticsearch service
  // "aws_access_secret": "ABCDEF" // used for signing requests to AWS Elasticsearch service
  // "parent_id": "elastic_parent" // defaults to "elastic_parent" parent identifier for Elasticsearch
})

t.Config({"write_timeout":"30000s"}).Source("source",source).Save("sink",sink)
//t.Source("source", source, "/.*/").Save("sink", sink, "/.*/")
"""
string = string.replace('mongodb://localhost/${}',"mongodb://localhost/"+sys.argv[1])
string = string.replace('http://{id}:{pw}@{your_db_address}:9200${}','http://{id}:{pw}@{your_db_address}:9200/'+sys.argv[2])
with open('pipeline.js', 'w') as f:
	f.write(string)
  
call(["transporter","run","pipeline.js"])
