import pandas as pd
df=pd.read_csv("data/cse_employability_skill_gap_dataset.csv")
df["student_id"]=df["Student_ID"].astype("string")
skills=["Programming","Databases","Problem_Solving","Communication","Cloud_Computing","Teamwork","Aptitude"]
for c in skills: df[c]=df[c].fillna(df[c].median())
df["skill_gap_encoded"]=df["Skill_Gap_Category"].map({"Low":0,"Medium":1,"High":2}).astype("int64")
df["average_skill"]=(df[skills].sum(axis=1)/7).astype("float32")
df["industry_readiness"]=df["Industry_Readiness_Percent"].astype("float32")
rename={"Programming":"programming","Databases":"databases","Problem_Solving":"problem_solving","Communication":"communication","Cloud_Computing":"cloud_computing","Teamwork":"teamwork","Aptitude":"aptitude"}
for a,b in rename.items(): df[b]=df[a].astype("int64")
df["skill_gap_category"]=df["Skill_Gap_Category"].astype("string")
base_time=pd.Timestamp("2026-01-01",tz="UTC")
df["event_timestamp"]=base_time+pd.to_timedelta(df["student_id"].str[1:].astype(int),unit="s")
df["created_timestamp"]=df["event_timestamp"]+pd.Timedelta(seconds=1)
feature_df=df[["student_id","event_timestamp","created_timestamp"]+list(rename.values())]
feature_df.to_parquet("data/cse_employability_features.parquet",index=False)
