import duckdb
from dotenv import load_dotenv
import os

load_dotenv()

region = os.environ.get("AWS_REGION")
s3_bucket = os.environ.get("AWS_S3_BUCKET")

aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")


con = duckdb.connect(database=':memory:')

# Install and load the httpfs extension (run once)
install_httpfs_query = 'INSTALL httpfs;'
load_httpfs_query = 'LOAD httpfs;'
con.execute(install_httpfs_query)
con.execute(load_httpfs_query)

# Set up S3 credentials and region
s3_region_query = f'SET s3_region=\'{region}\';'
s3_access_key_id_query = f'SET s3_access_key_id=\'{aws_access_key_id}\';'
s3_secret_access_key_query = f'SET s3_secret_access_key=\'{aws_secret_access_key}\';'
con.execute(s3_region_query)
con.execute(s3_access_key_id_query)
con.execute(s3_secret_access_key_query)

# Create a view for all of the parquet files in the bucket
view_query = f"CREATE VIEW data AS SELECT * FROM read_parquet('s3://{s3_bucket}/*.parquet');"
con.execute(view_query)

# Query the data
query = 'SELECT COUNT(*) FROM data;'
result = con.execute(query).fetchall()
print(result)