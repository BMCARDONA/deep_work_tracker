import pandas as pd
import matplotlib.pyplot as plt

def generate_charts(file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Sum the values of each column that is NOT "Date" or "Deep Work Hours"
    labels = []
    sizes = []
    for col in df.columns:
        if col not in ['Date', 'Deep Work Hours']:
            labels.append(col)
            sizes.append(df[col].sum())

    # Generate the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    # Add the title to the pie chart
    plt.title('Deep Work Monthly Breakdown')

    # Save the pie chart as an image
    plt.savefig('pie_chart.png')

    # Generate the stacked bar graph
    data = {'Date': df['Date']}
    for col in df.columns:
        if col not in ['Date', 'Deep Work Hours']:
            data[col] = df[col]
    plot_data = pd.DataFrame(data)

    # Increase the size of the figure
    fig, ax = plt.subplots(figsize=(10, 10))
    plot_data.plot(x='Date', kind='bar', stacked=True, ax=ax)

    # Add the title to the stacked bar graph
    ax.set_title('Deep Work Daily Breakdown')

    # Rotate the dates and label the y-axis
    plt.xticks(rotation=45, ha='right')
    ax.set_ylabel('Deep Work Hours')

    # Save the stacked bar graph as an image
    plt.savefig('stacked_bar_graph.png')

    # Sum the "Deep Work Hours" column and make that the value of "Total Deep Work Hours"
    total_deep_work_hours = df['Deep Work Hours'].sum()

    # Sum the values of each column that is NOT "Date" or "Deep Work Hours"
    category_totals = []
    for col in df.columns:
        if col not in ['Date', 'Deep Work Hours']:
            category_totals.append((col, df[col].sum()))

    # Save the updated totals
    with open('updated_totals.md', 'w') as f:
        f.write(f'Total Deep Work Hours: {total_deep_work_hours}\n')
        f.write(f'Total Deep Work Hours (by Category):\n')
        for col, total in category_totals:
            f.write(f'  - {col}: {total}\n')

file_path = 'table.csv'
generate_charts(file_path)
