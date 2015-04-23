### Step-1 finds and lists the ASIN Amazon bar codes from any top 100 best sellers list on Amazon.

After running getasin.py, you will have a long list of data. Format the data for Excel with the following command which replaces the comma with a new line and creates a new file called results2.txt:

	tr , '\n' < results.txt >> results2.txt
