# Use the file name words_short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
fl_val = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    line_val = line[line.find(":")+1:].strip()
    fl_val = fl_val + float(line_val)
# print(line)
print("Average spam confidence:", fl_val/count)
