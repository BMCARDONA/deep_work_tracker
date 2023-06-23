# Deep Work Log

Deep work is defined by Cal Newport as a state of peak concentration that lets one learn hard things and create quality work quickly. The goal of this repository is to allow one to log the accomplishments one has made by incorporating the deep work philosophy. To create charts, one need only update a CSV file and run a Python script.

## Installation

You can install this project by cloning the repository, forking the repository, or downloading the zip files.

To **clone** the repository, open a terminal and run the following command:

```sh
git clone https://github.com/your-username/deep-work-log.git
```

Make sure to replace `your-username` with your GitHub username.

To **fork** the repository, click on the `Fork` button in the top-right corner of this page. This will create a copy of the repository in your GitHub account.

To **download** the zip files, click on the `Code` button in the top-right corner of this page and then click on `Download ZIP`. Extract the zip files to a directory of your choice

## Dependencies

- pandas
- matplotlib

## Usage

1. Install the dependencies using pip:

```
pip install pandas matplotlib
```

2. Add rows to the `table.csv` file with the following format:

```
Date,Deep Work Hours,Reading,Writing,Coding,Mathematics
2023-06-12,10,1,2,3,4
2023-06-13,8,1,1,2,4
2023-06-14,8,2,3,1,2
2023-06-17,8,2,3,2,1
2023-06-18,10,3,2,1,4
2023-06-19,8,2,1,1,4
2023-06-20,7,1,3,3,0
2023-06-21,7,0,3,0,4
```

  Notes about the .csv file:
  - Only column names of the categories (e.g., "Reading", "Writing", "Coding", and "Mathematics") should be added/deleted. 
  - A date in the “Date” column should be in the format `YYYY-MM-DD`. 
  - A value in the “Deep Work Hours” column represents the total deep work hours for a given day. Hence, it should be the sum of the category values that come after it. 

3. Run the script:

```
python update_table.py
```

4. The following files will be generated:

- updated_totals.md
- pie_chart.png
- stacked_bar_graph.png

For this example, pie_chart.png will look like this:

![Sample Pie Chart](deep_work_log_june_2023/pie_chart.png)

And stacked_bar_graph.png will look like this:

![Sample Stacked Bar Graph](deep_work_log_june_2023/stacked_bar_graph.png)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)












