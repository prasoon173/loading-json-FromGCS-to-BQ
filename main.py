def load_table_uri_json(table_id):

    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    
    table_id = "uob-bucket.trusted_layer.demo"
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("name", "STRING"),
            bigquery.SchemaField("location", "STRING")
        ],
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    )
    uri = "gs://crc-test-bucket-98765/test.json"

    load_job = client.load_table_from_uri(
        uri,
        table_id,
        location="US",  # Must match the destination dataset location.
        job_config=job_config,
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))
    # [END bigquery_load_table_gcs_json]


    
