import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_charts(file_path):
    # Set the color palette
    sns.set_palette('colorblind')

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

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

    # Generate the stacked bar graph
    data = {'Date': df['Date']}
    for col in df.columns:
        if col not in ['Date', 'Deep Work Hours']:
            data[col] = df[col]
    
    plot_data = pd.DataFrame(data)

    # Filter out columns with all zero values from plot_data
    plot_data = plot_data.loc[:, (plot_data != 0).any(axis=0)]

    # Increase the size of the figure
    fig, ax = plt.subplots(figsize=(10, 10))
    
    plot_data.plot(x='Date', kind='bar', stacked=True, ax=ax)

    # Add the title to the stacked bar graph
    ax.set_title('Deep Work Daily Breakdown')

    # Rotate the dates and label the y-axis
    plt.xticks(rotation=45, ha='right')
    ax.set_ylabel('Deep Work Hours')

    # Save the stacked bar graph as an image
    plt.savefig('figures/stacked_bar_graph.png', dpi=400)

    # Generate the heat map
    heat_map_data = df.melt(id_vars='Date', value_vars=labels, var_name='Category', value_name='Hours')
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    sns.heatmap(heat_map_data.pivot(index='Date', columns='Category', values='Hours'), cmap='YlOrRd', linewidths=0.5, linecolor='lightgrey', ax=ax)
    
    ax.set_title('Deep Work Heat Map')
    
    plt.xticks(rotation=45, ha='right')
    
    # Save the heat map as an image
    plt.savefig('figures/heat_map.png', dpi=400)

    # Sum the "Deep Work Hours" column and make that the value of "Total Deep Work Hours"
    total_deep_work_hours = df['Deep Work Hours'].sum()

    # Sum the values of each column that is NOT "Date" or "Deep Work Hours"
    category_totals = []
    for col in df.columns:
        if col not in ['Date', 'Deep Work Hours']:
            category_totals.append((col, df[col].sum()))

    # Save the updated totals
    with open('monthly_summary.md', 'w') as f:
        f.write(f'Total Deep Work Hours: {total_deep_work_hours} \n')

        f.write(f'Total Deep Work Hours (by Category):\n')
        for col, total in category_totals:
            f.write(f'  - {col}: {total}\n')
    
        # Add the pie chart to the markdown file
        f.write('\n ### Deep Work Monthly Breakdown: \n')
        f.write('![Pie Chart](figures/pie_chart.png) \n')

        # Add the stacked bar graph to the markdown file
        f.write('\n ### Deep Work Daily Breakdown: \n')
        f.write('![Stacked Bar Graph](figures/stacked_bar_graph.png) \n')
        
        # Add the heat map to the markdown file
        f.write('\n ### Deep Work Heat Map: \n')
        f.write('![Heat Map](figures/heat_map.png) \n')

file_path = 'table.csv'
generate_charts(file_path)
