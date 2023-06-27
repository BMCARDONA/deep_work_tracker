import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def generate_charts(file_path):
    # Set the color palette
    sns.set_palette('colorblind')

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Calculate the "Deep Work Hours" column as the sum of the other columns
    df['Deep Work Hours'] = df.drop('Date', axis=1).sum(axis=1)

    # Sum the values of each column that is NOT "Date" or "Deep Work Hours"
    labels = []
    sizes = []
    for col in df.columns:
        if col not in ['Date', 'Deep Work Hours']:
            labels.append(col)
            sizes.append(df[col].sum())

    # Filter out sizes and labels with a zero size
    nonzero_sizes = [size for size in sizes if size > 0]
    nonzero_labels = [label for label, size in zip(labels, sizes) if size > 0]

    # Define a custom function to format the percentage labels
    def format_autopct(pct):
        return f"{pct:.1f}%" if pct > 0 else ""

    # Generate the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(nonzero_sizes, labels=nonzero_labels, autopct=format_autopct, startangle=90)
    ax1.axis('equal')

    # Add the title to the pie chart
    plt.title('Deep Work Monthly Breakdown')

    # Save the pie chart as an image
    plt.savefig('figures/pie_chart.png', dpi=400)

    # Generate the heat map
    heat_map_data = df.melt(id_vars='Date', value_vars=labels, var_name='Category', value_name='Hours')
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    sns.heatmap(heat_map_data.pivot(index='Date', columns='Category', values='Hours'), cmap='GnBu', linewidths=0.5, linecolor='lightgrey', ax=ax)
    
    ax.set_title('Deep Work Heat Map')

    plt.xticks(rotation=45, ha='right')
    
    # Save the heat map as an image
    plt.savefig('figures/heat_map.png', dpi=400)

    # Generate the line graph
    fig, ax = plt.subplots(figsize=(10, 6))

    df.plot(x='Date', y='Deep Work Hours', marker='o', color='orange', ax=ax)

    # Add the title to the line graph
    ax.set_title('Total Deep Work Hours Over Time')

    # Set the x-axis ticks to show all dates
    ax.set_xticks(range(len(df)))
    ax.set_xticklabels(df['Date'], rotation=45, ha='right')

    # Add a light grey grid
    ax.grid(color='lightgrey', linestyle='--', linewidth=0.5)

    # Label the y-axis
    ax.set_ylabel('Deep Work Hours')

    # Adjust the margins around the plot
    plt.subplots_adjust(bottom=0.2)

    # Save the line graph as an image
    plt.savefig('figures/line_graph.png', dpi=400)

    # Sum the "Deep Work Hours" column and make that the value of "Total Deep Work Hours"
    total_deep_work_hours = df['Deep Work Hours'].sum()

    # Calculate the average deep work hours per day
    average_deep_work_hours = total_deep_work_hours / len(df)

    # Find the maximum and minimum deep work hours
    max_deep_work_hours = df['Deep Work Hours'].max()
    min_deep_work_hours = df['Deep Work Hours'].min()

    # Sum the values of each column that is NOT "Date" or "Deep Work Hours"
    category_totals = []
    for col in df.columns:
        if col not in ['Date', 'Deep Work Hours']:
            category_totals.append((col, df[col].sum()))

    # Save the updated totals and summary statistics
    with open('monthly_summary.md', 'w') as f:
        f.write(f'Total Deep Work Hours: {total_deep_work_hours} \n')
        f.write(f'Average Deep Work Hours per Day: {average_deep_work_hours:.2f} \n')
        f.write(f'Maximum Deep Work Hours: {max_deep_work_hours} \n')
        f.write(f'Minimum Deep Work Hours: {min_deep_work_hours} \n')

        f.write(f'\nTotal Deep Work Hours (by Category):\n')
        for col, total in category_totals:
            f.write(f'  - {col}: {total}\n')
    
        # Add the pie chart to the markdown file
        f.write('\n ### Deep Work Monthly Breakdown: \n')
        f.write('![Pie Chart](figures/pie_chart.png) \n')

        # Add the heat map to the markdown file
        f.write('\n ### Deep Work Heat Map: \n')
        f.write('![Heat Map](figures/heat_map.png) \n')

        # Add the line graph to the markdown file
        f.write('\n ### Total Deep Work Hours Over Time: \n')
        f.write('![Line Graph](figures/line_graph.png) \n')


file_path = 'table.csv'
generate_charts(file_path)
