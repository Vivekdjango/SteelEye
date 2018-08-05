
Data Ingestion/Python Engineer Assessment Test

Files Description:

requirements.txt:  To install relevant packages for the assignment 

E.g: pip install -r requirements.txt

SteelEye_Assignment.py: The Python script to read the excel file and perform the requested action
	a)I have used Python Data Analysis library called Pandas to read the Excel file
	b)I filtered the data and used panda dataframe to JSON converter to store as a JSON file
	c)Then I uploaded the file to S3 bucket using boto3 module successfully
