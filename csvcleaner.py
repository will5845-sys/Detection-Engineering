import csv
 
def escape_quotes(in_path: str, out_path: str) -> None:
    with open(in_path, newline="", encoding="utf-8") as src, \
         open(out_path, "w", newline="", encoding="utf-8") as dst:
 
        reader = csv.reader(src)
        writer = csv.writer(dst, quoting=csv.QUOTE_ALL, escapechar="\\")
        for row in reader:
            # Double any internal double‑quote characters
            new_row = [cell.replace('"', '""') for cell in row]
            writer.writerow(new_row)
 
escape_quotes("nodes_Description.csv", "nodes_Description.cleaned.csv")

