# Deep Work Tracker

Deep work is a state of peak concentration that lets one learn hard things and create quality work quickly. The goal of this repository is to allow you to track the accomplishments you've made by incorporating deep work into your workflow. To add a daily entry to a monthly log, you need only update a CSV file and run a Python script.

## Installation

You can install this project by cloning the repository, forking the repository, or downloading the zip files.

To **clone** the repository, open a terminal and run the following command:

```sh
git clone git@github.com:your-username/deep_work_tracker.git
```

Make sure to replace `your-username` with your GitHub username.

To **fork** the repository, click on the `Fork` button in the top-right corner of this page. This will create a copy of the repository in your GitHub account.

To **download** the zip files, click on the `Code` button in the top-right corner of this page and then click on `Download ZIP`. Extract the zip files to a directory of your choice

## Dependencies

- Pandas
- Matplotlib
- Seaborn 

## Usage

1. Install the dependencies using pip:

```
pip install pandas matplotlib seaborn
```

2. Add rows to the `table.csv` file located in the `MONTH_YEAR` directory to track the hours you've spent per day in each category:

```
Date,Reading,Writing,Coding,Mathematics
06-01-2023,1,0,2,1
06-02-2023,0,1,2,1
06-03-2023,0,0,2,1
06-04-2023,1,3,0,0
...
```

For the `MONTH_YEAR` directory, make sure to replace `MONTH_YEAR` with the month and year for which you want to track your deep work hours. Add as many of these directories as you'd like. 

Notes about the `table.csv` file:
- Replace the category columns (in this case, the "Reading", "Writing", "Coding", and "Mathematics" columns) with columns of your own. (You should have at least one of these columns in the table, but you can add as many as you'd like.)
- A date in the “Date” column should be in the format `MM-DD-YYYY`. 

3. Run the script:

```
python update_monthly_summary.py
```

4. The following files will be generated:

- `monthly_summary.md`
- `figures/monthly_breakdown.png`
- `figures/daily_breakdown.png`

For the `june_2023` example (see the directory above), `monthly_summary.md` will contain `monthly_breakdown.png`, which will look like this:

![Bar Chart](june_2023/figures/monthly_breakdown.png)

And `daily_breakdown.png`, which will look like this:

![Facet Plot](june_2023/figures/daily_breakdown.png)


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)