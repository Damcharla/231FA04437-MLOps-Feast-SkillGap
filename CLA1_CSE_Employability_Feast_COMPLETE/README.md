# Curriculum-Industry Skill Feature Store Using Feast

## Student Details
Name: Damacharla Shanmuk Chowdary  
Register Number: 231FA04437  
Section: 09  
College/University: Vignan's Foundation for Science, Technology and Research  
Branch: Computer Science and Engineering (CSE)

## Problem Statement
Identify curriculum-industry skill gaps for CSE students and classify students into Low, Medium, or High skill-gap categories using a Feast feature store and a Decision Tree model.

## Dataset
100 synthetic student records, 7 skills: Programming, Databases, Problem Solving, Communication, Cloud Computing, Teamwork, Aptitude. Target: `Skill_Gap_Category`.

## Feature Engineering
Feast features: `student_id`, `event_timestamp`, `created_timestamp`, `programming`, `databases`, `problem_solving`, `communication`, `cloud_computing`, `teamwork`, `aptitude`.

## Feast Architecture
Original Dataset → Feature Engineering → Parquet Offline Data → Feast FeatureView → Historical Features/Model Training and Materialization → Online Store → Online Retrieval → Prediction.

## Implementation
Entity: `student`; data source: `cse_source`; FeatureView: `cse_employability_features`; FeatureService: `cse_employability_service`; historical retrieval: `get_historical_features()`; model: DecisionTreeClassifier; online retrieval: `get_online_features()`.

## Required Analysis
1. Entity: `student`, join key `student_id`.
2. FeatureView: programming, databases, problem_solving, communication, cloud_computing, teamwork, aptitude.
3. Feature calculation: `average_skill` is the mean of the seven skill scores; timestamps are derived from a fixed UTC base time and student number.
4. Original dataset contains target and aggregate fields; feature dataset contains entity, timestamps and serving features.
5. Offline store: historical feature data for training.
6. Online store: materialized features for fast prediction.
7. `feast apply`: registers Feast definitions.
8. Materialization: loads features into the online store for a specified range.
9. Feast provides consistent feature definitions across training and prediction.
10. Limitations: synthetic data; industry requirements can change.
11. Improvements: add real assessment/placement evidence and regularly update curriculum/industry requirements.

## Results
**Model accuracy:** 80.00%

**Final prediction for student 25:** Medium

**Online predictions:**

 student_id predicted_skill_gap
         10              Medium
         20              Medium
         30              Medium
         40              Medium

## Repository Name
`231FA04437MLOps-Feast-SkillGap`

## Important Note on Screenshots
The included screenshots are generated Colab-style evidence based on the supplied notebook and dataset. They are not live browser screenshots. If your faculty requires actual Colab browser captures, run the completed notebook in Colab and replace these images with your own captures.
