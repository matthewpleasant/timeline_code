import csv

file = open('GUNS 2012 - Sheet2 (1).csv')
csv_file = csv.reader(file) #creates CSV object that's parsed

time_line = open(r'/Users/matthewpleasant/desktop/csv_timeline.txt', 'a')

for row in csv_file:
    number = 1
    panel1 = "\n<!-- panel -->\n<div class=\"panel\">\n<div class=\"panel_content\">\n    <h2><p>" + \
    row[0] + "</p></h2>\n        <a href=\"#answer" + \
        str(number) + "\" onclick=\"return showAnswer('answer" + str(number) + \
        "');\"><img class=\"thumb\" src=\"images/" + row[3] + "\" alt=\"" + row[0] + " (victim)\"></a>\n        <h2><p>" + \
        row[1] + "</p></h2>\n    <div class=\"label\">" + row[2] + "</div>\n        <div class=\"clear_both\"></div>\n    </div>\n</div>\n<!--panel-->\n"
    time_line.write(panel1)
    number += 1
    
file.close()