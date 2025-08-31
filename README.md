Built with [`pdfplumber`](https://github.com/jsvine/pdfplumber) and `pandas`, this script is designed for Advanzia Bank/Carta YOU transaction statements to be converted in xls format for better data handling and processing.

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

Alternatively, you can download the latest standalone exe from the Releases page.
