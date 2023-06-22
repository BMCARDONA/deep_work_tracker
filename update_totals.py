import re
import matplotlib.pyplot as plt

def update_totals(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract the categories
    categories = re.findall(r'-\s(.+?):\s\d+', content)
    
    # Initialize the totals
    total_hours = 0
    category_hours = {category: 0 for category in categories}
    
    # Find all the deep work hours
    deep_work_hours = re.findall(r'-\sHour\s\d:\s(.+)', content)
    
    # Update the totals
    for hour in deep_work_hours:
        total_hours += 1
        category_hours[hour] += 1
    
    # Update the content
    content = re.sub(r'(Total Deep Work Hours \(Total\):\s)\d+', r'\g<1>' + str(total_hours), content)
    for category, hours in category_hours.items():
        content = re.sub(r'(' + category + ':\s)\d+', r'\g<1>' + str(hours), content)
    
    # Remove the date line from the content
    content = re.sub(r'#### Date:.*', '', content)
    
    # Write the updated content to the file
    with open(file_path, 'w') as f:
        f.write(content)
    
    # Generate and save the pie chart
    fig, ax = plt.subplots()
    ax.pie([category_hours[category] for category in categories], labels=categories, autopct='%1.1f%%')
    ax.set_title('Total Deep Work Hours (By Category)')
    plt.savefig('pie_chart.png')
    
    # Update the markdown file to include a link to the pie chart
    with open(file_path, 'r') as f:
        content = f.read()
    
    content = content.replace('[Insert Pie Chart]', '![Pie Chart](pie_chart.png)')
    
    with open(file_path, 'w') as f:
        f.write(content)

# Example usage
update_totals('deep_work_log.md')
