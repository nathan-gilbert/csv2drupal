import csv
import string

# <td style="text-align: left;">HD-${District}</td>
tr = string.Template("""
<tr>
  <td style="text-align: left;"></td>
  <td style="text-align: left;">${Representative}</td>
  <td style="text-align: right;">${PercentGrade}</td>
  <td style="text-align: center;">${LetterGrade}</td>
</tr>
""")

header_template = string.Template("""
<tr>
    <th class="zui-sticky-col" scope="col">Representative</th>
    <th class="zui-sticky-col" scope="col">Party</th>
    <th class="zui-sticky-col" scope="col">District</th>
    ${data}
</tr>
""")

header_bill_template = string.Template("""
    <th scope="col">${data}</th>
""")

full_template = string.Template("""
<tr>
    <td class="zui-sticky-col">${name}</td>
    ${data}
</tr>
""")

bill_template = string.Template("""
  <td>${data}</td>
""")


def read_header(full_data_header):
    bill_list = []
    for bill in full_data_header[2:]:
        bill_list.append(header_bill_template.substitute(data=bill.strip()))
    full_header = header_template.substitute(data=''.join(bill_list))
    print(full_header)


def all_bills(reader):
    # title = "Representative"
    title = "Senator"

    for row in reader:
        bill_list = []
        for col in row:
            if col != title:
                bill_list.append(bill_template.substitute(data=row[col].strip()))
        pol_name = row[title]
        full_t = full_template.substitute(name=pol_name, data=''.join(bill_list))
        print(full_t)


def full_data(f):
    with open(f, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        # header_row = reader.fieldnames
        # read_header(header_row)
        all_bills(reader)


def summary_data(f):
    # title = "Representative"
    title = "Senator"

    with open(f) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # print(str(row) + "\n")
            try:
                rep_name_tokens = row[title].split(", ")
                rep_name = rep_name_tokens[1].strip() + " " + rep_name_tokens[0]
            except:
                rep_name = row[title]

            v = {
                # 'District': row['District '],
                # 'Representative': row['Representative'],
                'Representative': rep_name,
                'PercentGrade': row['Percent Grade'],
                'LetterGrade': row['Letter Grade']
            }
            print(tr.substitute(v))


if __name__ == "__main__":
    # in_file = "house_full.csv"
    # in_file = "senate.csv"
    in_file = "senate_full.csv"
    # summary_data(in_file)
    full_data(in_file)
