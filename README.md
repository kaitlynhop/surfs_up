# Surfs_up
## Overview
In this project, SQLalchemy was used to query SQLite database file in Jupyter Notebook. Flask was then used to develop web framework to hold query data in JSON format. Database was queried for the information:
1. Precipitation data was extracted and filtered for dates between 8-23-16 and 8-23-17.
2. Station data was extracted, for unique station identifiers.
3. Tempurature statistical data (min, max, and average) was calculated for the most active station between 8-23-16 and 8-23-17.
4. Tempurature statistical data (min, max, and average) was calculated and included in a function to allow for user input of date ranges.
5. Tempurature statistical date (count, min, max, avg, std, and quartiles) were calculated for months June and December, to compare.

### Resources
**Data Source:** [SQLite DataBase File](/Resources/hawaii.sqlite)
**Exploratory Analysis:** [Exploratory Notebooks](/Exploratory_Analysis/)
**Flask file:** [app.py](/app.py)

**Tools:** SQLite, SQLalchemy, FLASK, Python, VScode, Jupyter Notebook, PANDAS, Matplotlib, Numpy, Datetime, Jsonify
<br>
