import os
import re
import sys
import pandas as pd
import pdfplumber
import argparse
import time
from datetime import datetime

def line_to_column(line_text):
    pattern = re.compile(
        r"^(?P<Date>\d{2}\.\d{2}\.\d{2})\s+"
        r"(?P<Counterparty>.+?)\s+"
        r"(?P<Category>\w+)\s+"
        r"€\s*"
        r"(?P<Amount>[-\d,]+)$"
    )
    match = pattern.match(line_text)
    if match:
        data = match.groupdict()
        try:
           parsed_date = datetime.strptime(data["Date"], "%d.%m.%y")
           data["Date"] = parsed_date.strftime("%d/%m/%Y")
        except ValueError:
           pass
        amount_str = data['Amount'].replace(',', '.')
        try:
            amount = float(amount_str)
        except ValueError:
            amount = None
        return [
            data['Date'],
            data['Counterparty'],
            data['Category'],
            amount
        ]
    else:
        return None

def to_xls(pdf_path, xls_output):
    parsed_rows = []
    headers = ["Date","Counterparty", "Category", "Amount"]
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            lines = page.extract_text_lines(strip=True, return_chars=False)
            if not lines or len(lines) <= 2:
              continue
            for i, line_obj in enumerate(lines[3:]):
              line_txt = line_obj["text"].strip()
              parsed_data = line_to_column(line_txt)
              if parsed_data:
                parsed_rows.append(parsed_data)
    if parsed_rows:
        df = pd.DataFrame(parsed_rows, columns=headers)
        df.to_excel(xls_output, index=False)
        print(f"✅ Excel file saved to {xls_output}")
    else:
        print(f"❌ No valid data found in PDF file {pdf_path}")

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", required=True, help="PDF Path")
  parser.add_argument("-o", "--output", required=False, help="Output Excel")
  args = parser.parse_args()
  if not (args.input):
    print(f"usage: youtoxls.exe --input <pdffile> --output <xlsfile> (optional)")
    sys.exit(1)
  input = args.input
  output = args.output
  if not args.output:
    output = f"you-export-{int(time.time() * 1000)}.xlsx"
  else:
    if not output.lower().endswith(".xlsx"):
      output = f"{output}.xlsx"
  to_xls(input, output)

if __name__ == "__main__":
  main()