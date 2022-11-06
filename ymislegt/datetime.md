## Datetime (module) - Dagsetningar og tími í python 
- [How to properly use datetime in your Python code](https://medium.com/better-programming/demystifying-python-datetime-module-with-examples-352e6cc72efc)
- [Python Datetime Tutorial: Manipulate Times, Dates, and Time Spans](https://www.dataquest.io/blog/python-datetime-tutorial/)

---

### Dæmi um lausn 

`'timestampApis': '2021-02-04T22:50:15.468'  # Timestamp format: yy-MM-dd HH:mm:ss,SSS`

1. get date (string) from JSON data (Api)
2. String to Datetime Object with datetime.strptime()
3. Convert Python Datetime to a String, datetime_string = datetime_object.strftime(format_string)

_Það væri einnig hægt að nota strengjavinnslu og regex til að fá íslenska dagsetningu_
