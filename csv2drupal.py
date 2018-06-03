
import sys
import csv
import string

tr = string.Template("""
<tr>
  <td style="text-align: left;">HD-${District}</td>
  <td style="text-align: left;">${Representative}</td>
  <td style="text-align: right;">${PercentGrade}</td>
  <td style="text-align: center;">${LetterGrade}</td>
</tr>
""")

if __name__ == "__main__":
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(str(row) + "\n")
            try:
                rep_name_tokens = row['Representative'].split(", ")
                rep_name = rep_name_tokens[1].strip() + " " + rep_name_tokens[0]
            except:
                rep_name = row['Representative']

            v = {
                'District': row['District '],
                #'Representative' : row['Representative'],
                'Representative' : rep_name,
                'PercentGrade' : row['Percent Grade'],
                'LetterGrade': row['Letter Grade']
            }
            print(tr.substitute(v))
