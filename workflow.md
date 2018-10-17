1. train.shape
	Training data shape:  (307511, 122)
2. test.shape
	Testing data shape:  (48744, 121)
3. train['TARGET'].value_counts()
	0    282686
	1     24825
4. mis_val_percent = 100 * df.isnull().sum() / len(df)
	Your selected dataframe has 122 columns.
	There are 67 columns that have missing values.
5. train.dtypes.value_counts()
	float64    65
	int64      41
	object     16
6. train.select_dtypes('object').apply(pd.Series.nunique, axis = 0)
	NAME_CONTRACT_TYPE             2
	CODE_GENDER                    3
	FLAG_OWN_CAR                   2
7. Create a label encoder object
	3 columns were label encoded.
8. one-hot encoding of categorical variables
	Training Features shape:  (307511, 243)
	Testing Features shape:  (48744, 239)
9. app_train, app_test = app_train.align(app_test, join = 'inner', axis = 1)
	Training Features shape:  (307511, 240)
	Testing Features shape:  (48744, 239)
10. Anomalies
	train['DAYS_EMPLOYED'].describe()
	That doesn't look right! The maximum value is about 1000 years!