import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

    #=========================== FACET PLOT ===========================

    # Set the color palette
    palette = sns.color_palette('colorblind', len(nonzero_labels) + 1)

    # Create the facet plot
    g = sns.FacetGrid(df.melt(id_vars='Date', value_vars=nonzero_labels + ['Deep Work Hours'], var_name='Category', value_name='Hours'), row='Category', hue='Category', sharey=False, height=2.5, aspect=4)
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
    g.savefig('figures/daily_breakdown.png', dpi=600)

    #=========================== BAR CHART ===========================

    # Calculate the total deep work hours
    total_deep_work_hours = df['Deep Work Hours'].sum()

    # Generate the bar chart for total deep work hours by category
    fig, ax = plt.subplots()
    palette = sns.color_palette('colorblind', len(nonzero_labels) + 1)
    bars = ax.bar(nonzero_labels + ['Total'], nonzero_sizes + [total_deep_work_hours], color=palette)

    # Add the value to each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, f"{height:.0f}", ha='center', va='bottom')

    # Add the title to the bar chart
    ax.set_title('Monthly Breakdown')

    # Label the y-axis
    ax.set_ylabel('Total Deep Work Hours')

    # Save the bar chart as an image
    plt.savefig('figures/monthly_breakdown.png', dpi=600)

    #=========================== MARKDOWN ===========================

    # Save the updated totals and summary statistics
    with open('monthly_summary.md', 'w') as f:

        # Add the bar chart to the markdown file
        f.write('\n ### Monthly Breakdown: \n')
        f.write('![Bar Chart](figures/monthly_breakdown.png) \n')

        # Add the facet plot to the markdown file
        f.write('\n ### Daily Breakdown: \n')
        f.write('![Facet Plot](figures/daily_breakdown.png) \n')


file_path = 'table.csv'
generate_charts(file_path)
