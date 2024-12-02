import csv
import html

# Set the path to the uploaded CSV file
csv_file = '/mnt/data/Bret_Clements_Bath_Invitational_Mens_5000_Meters_J.V.csv'

# Open the CSV file and extract the data
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# Extract meet information based on provided indices
meet_name = data[0][0]  # Cell A1 - Meet Name
meet_date = data[1][0]  # Cell A2 - Meet Date
team_results_link = data[2][0]  # Cell A3 - hyperlink for the team-results section
race_comments = " ".join(data[3][0:5])   # Row 4 - race-comments section
race_comments = html.escape(race_comments)  # Escape any special HTML characters

# Extract team results starting from row 6 (index 5), assuming columns A, B, and C
team_results = []
for row in data[5:10]:  # Selecting first 5 rows of team results as requested
    if len(row) >= 3:
        place, team, score = row[0], row[1], row[2]
        team_results.append({
            'place': place,
            'team': team,
            'score': score
        })

# Athlete details: Assuming they're further down, add more rows as needed for full dataset
athlete_results = []
indices = [46, 66, 73, 84, 100]  # Use actual indices if provided
for i in indices:
    if i < len(data):
        row = data[i]
        if len(row) >= 8:
            athlete_results.append({
                'place': row[0],
                'grade': row[1],
                'name': row[2],
                'athlete_link': row[3],
                'time': row[4],
                'team': row[5],
                'team_link': row[6],
                'profile_pic': row[7]
            })

# Build HTML content
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel="stylesheet" href="css/reset.css">
   <link rel="stylesheet" href="css/style.css">
   <title>{meet_name} Country Meet</title>
</head>
<body>

<header>
   <nav>
      <ul>
         <li><a href="index.html">Home</a></li>
         <li><a href="#athlete-results">Athlete Results</a></li>
         <li><a href="#team-results">Team Results</a></li>
         <li><a href="#overall-comments">Overall Comments</a></li>
         <li><a href="#photo-gallery">Photo Gallery</a></li>
      </ul>
   </nav>
   
   <h1>{meet_name}</h1>
   <h2>{meet_date}</h2>
</header>

<section id="athlete-results">
   <h2>Athlete Results</h2>
   <table>
      <tr>
         <th>Name</th>
         <th>Grade</th>
         <th>Time</th>
         <th>Place</th>
         <th>Team</th>
         <th>Profile Picture</th>
      </tr>'''

for athlete in athlete_results:
    html_content += f'''
      <tr>
         <td><a href="{athlete['athlete_link']}">{athlete['name']}</a></td>
         <td>{athlete['grade']}</td>
         <td>{athlete['time']}</td>
         <td>{athlete['place']}</td>
         <td><a href="{athlete['team_link']}">{athlete['team']}</a></td>
         <td><img src="Client-Data-Files/images/AthleteImages/{athlete['profile_pic']}" alt="{athlete['name']}'s picture" width="60" height="80"></td>
      </tr>'''

html_content += f'''
   </table>
</section>

<section id="team-results">
   <h2>Team Results</h2>
   <a href="{team_results_link}">View Full Team Results</a>
   <table>
      <tr>
         <th>Place</th>
         <th>Team</th>
         <th>Score</th>
      </tr>'''

for result in team_results:
    html_content += f'''
      <tr>
         <td>{result['place']}</td>
         <td>{result['team']}</td>
         <td>{result['score']}</td>
      </tr>'''

html_content += f'''
   </table>
</section>

<section id="overall-comments">
   <h2>Overall Comments</h2>
   <p>{race_comments}</p>
</section>

<section id="photo-gallery">
   <h2>Photo Gallery</h2>
   <div>'''
for i in range(9096, 9101):
    html_content += f'''
      <img src="Client-Data-Files/images/bath/IMG_{i}.jpg" alt="IMG_{i}" width="150" height="150" />'''
html_content += '</div><div>'
for i in range(9102, 9107):
    html_content += f'''
      <img src="Client-Data-Files/images/bath/IMG_{i}.jpg" alt="IMG_{i}" width="150" height="150" />'''
html_content += '</div></section>'

html_content += f'''
<footer>
   <p>&copy; {meet_name}. All Rights Reserved.</p>
</footer>

</body>
</html>'''

# Save the updated HTML content to a file
output_html_file_path = '/mnt/data/meet_results_Bath_Men.html'
with open(output_html_file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

output_html_file_path

