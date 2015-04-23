After running getasin.py, you will have a long list of data. Format the data for Excel with the following command which replaces the comma with a new line and creates a new file called results2.txt:

	tr , '\n' < results.txt >> results2.txt
