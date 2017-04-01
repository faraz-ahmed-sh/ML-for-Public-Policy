#Machine Learning for Public Policy
#Assignment 1
#Faraz Ahmed
#March 29

import pandas as pd

filename1 = '311_Service_Requests_-_Vacant_and_Abandoned_Buildings_Reported'
filename2 = '311_Service_Requests_-_Graffiti_Removal'
filename3 = '311_Service_Requests_-_Pot_Holes_Reported'
filename4 = '311_Service_Requests_-_Sanitation_Code_Complaints'

def reading_csv():

	df1 = pd.read_csv(filename1 + '.csv', header =1, encoding = "ISO-8859-1", nrows=20)
	df2 = pd.read_csv(filename2 + '.csv', encoding = "ISO-8859-1", nrows=100)
	df3 = pd.read_csv(filename3 + '.csv', encoding = "ISO-8859-1", nrows=20)
	df4 = pd.read_csv(filename4 + '.csv', encoding = "ISO-8859-1", nrows=20)
	
	# worst neighborhoods?
	#print("VC", df2['ZIP Code'].value_counts())

	df_grouped = df2.groupby('What Type of Surface is the Graffiti on?')
	# most recurring type of graffiti
	#print(df_grouped['ZIP Code'].count())

	# by neighborhoods and graffiti types
	df_grouped_2 = df2.groupby(['What Type of Surface is the Graffiti on?', 'ZIP Code'])['ZIP Code'].count()
	#print(df_grouped_2)
	#print(df2['ZIP Code'].describe)

	# response time
	df_grouped_3 = df2.groupby(['Creation Date', 'Completion Date'])
	print(df_grouped_3['ZIP Code'].count())

	# when were different types of requests generated
	df_grouped_4 = df2.groupby(['What Type of Surface is the Graffiti on?', 'Creation Date'])
	print(df_grouped_4['ZIP Code'].count())

	df_grouped_5 = df2.groupby(['Creation Date', 'What Type of Surface is the Graffiti on?'])
	print(df_grouped_5['ZIP Code'].count())



	
	


	#v = df1.merge(df2, left_on = 'ZIP CODE', right_on = 'ZIP Code', how='inner', indicator=True)

	