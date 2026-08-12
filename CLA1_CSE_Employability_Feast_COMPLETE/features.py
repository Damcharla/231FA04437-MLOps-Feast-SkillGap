from datetime import timedelta
from feast import Entity, FeatureView, FeatureService, Field, FileSource
from feast.types import Int64
student=Entity(name="student",join_keys=["student_id"],description="CSE student")
cse_source=FileSource(name="cse_source",path="data/cse_employability_features.parquet",timestamp_field="event_timestamp",created_timestamp_column="created_timestamp")
cse_feature_view=FeatureView(name="cse_employability_features",entities=[student],ttl=timedelta(days=50000),schema=[Field(name="programming",dtype=Int64),Field(name="databases",dtype=Int64),Field(name="problem_solving",dtype=Int64),Field(name="communication",dtype=Int64),Field(name="cloud_computing",dtype=Int64),Field(name="teamwork",dtype=Int64),Field(name="aptitude",dtype=Int64)],source=cse_source,online=True)
cse_feature_service=FeatureService(name="cse_employability_service",features=[cse_feature_view])
