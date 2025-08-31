Built with [`pdfplumber`](https://github.com/jsvine/pdfplumber) and `pandas`, this script is designed for statements that follow a standard table-like format, even when the PDF doesn't expose actual tables.

---

## 🔧 Features

- Extracts transaction data from PDF
- Parses dates, categories, and amounts cleanly
- Outputs to `.xlsx` with proper column formatting
- Supports command-line usage
- Auto-generates output filenames if not provided
- Optional support for custom headers

---

## 📦 Requirements

- Python 3.8+
- `pdfplumber`
- `pandas`
- `openpyxl` (for Excel writing)

You can install all dependencies with:

```bash
pip install -r requirements.txt
```
