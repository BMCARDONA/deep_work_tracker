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
    plt.savefig('figures/line_graph.png', dpi=600)

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

    # Create the facet plot
    g = sns.FacetGrid(df.melt(id_vars='Date', value_vars=labels, var_name='Category', value_name='Hours'), row='Category', hue='Category', sharey=False, height=2.5, aspect=4)
    g.map(sns.lineplot, 'Date', 'Hours', marker='o')
    g.set_xticklabels(rotation=45)
    g.set_titles(row_template="{row_name}")

    # Set the x-axis ticks to show all dates
    for ax in g.axes.flat:
        ax.set_xticks(range(len(df)))
        ax.set_xticklabels(df['Date'], rotation=45, ha='right')

    # Add a light grey grid to each graph
    for ax in g.axes.flat:
        ax.grid(color='lightgrey', linestyle='--', linewidth=0.5)

    # Save the facet plot as an HD image
    g.savefig('figures/facet_plot.png', dpi=600)

    # Generate the bar chart
    fig, ax = plt.subplots()
    palette = sns.color_palette('colorblind', len(labels))
    ax.bar(labels, sizes, color=palette)

    # Add the title to the bar chart
    ax.set_title('Total Deep Work Hours (by Category)')

    # Label the x and y axes
    ax.set_xlabel('Category')
    ax.set_ylabel('Total Deep Work Hours')

    # Add a light grey grid
    ax.grid(color='lightgrey', linestyle='--', linewidth=0.5)

    # Save the bar chart as an image
    plt.savefig('figures/bar_chart.png', dpi=600)


    # Save the updated totals and summary statistics
    with open('monthly_summary.md', 'w') as f:
        f.write(f'Total Deep Work Hours: {total_deep_work_hours} \n')
        f.write(f'Average Deep Work Hours per Day: {average_deep_work_hours:.2f} \n')
        f.write(f'Maximum Deep Work Hours: {max_deep_work_hours} \n')
        f.write(f'Minimum Deep Work Hours: {min_deep_work_hours} \n')

        # Add the line graph to the markdown file
        f.write('\n ### Total Deep Work Hours Over Time: \n')
        f.write('![Line Graph](figures/line_graph.png) \n')

        # Add the facet plot to the markdown file
        f.write('\n ### Deep Work Hours by Category Over Time: \n')
        f.write('![Facet Plot](figures/facet_plot.png) \n')

        f.write('\n ### Total Deep Work Hours (by Category): \n')
        f.write('![Bar Chart](figures/bar_chart.png) \n')


file_path = 'table.csv'
generate_charts(file_path)
