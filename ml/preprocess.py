import pandas as pd

# 1. Load data
df = pd.read_csv("../data/KDDTrain+.csv", header=None)

# 2. Column names
columns = [
'duration','protocol_type','service','flag','src_bytes','dst_bytes','land',
'wrong_fragment','urgent','hot','num_failed_logins','logged_in','num_compromised',
'root_shell','su_attempted','num_root','num_file_creations','num_shells',
'num_access_files','num_outbound_cmds','is_host_login','is_guest_login',
'count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate',
'same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count',
'dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate',
'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
'dst_host_serror_rate','dst_host_srv_serror_rate',
'dst_host_rerror_rate','dst_host_srv_rerror_rate',
'label','difficulty'
]
df.columns = columns

# 3. Binary label
df['label'] = df['label'].apply(lambda x: 0 if x=='normal' else 1)

# 4. Encoding
df = pd.get_dummies(df, columns=['protocol_type','service','flag'])

# 5. Save processed data
df.to_csv("../data/processed_train.csv", index=False)

print("✅ Preprocessing done, file saved!")
