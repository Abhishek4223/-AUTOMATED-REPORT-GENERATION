import pandas as pd
from fpdf import FPDF


df = pd.read_csv("C:/Users/Santosh Chaudhary/Documents/data.csv")
print(df.head())
df.columns = df.columns.str.strip()  
print("Columns found:", df.columns.tolist())


avg_score = df["Score"].mean()

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(200, 10, "Student Score Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.ln(10)
        self.cell(0, 10, title, ln=True)

    def chapter_body(self, text):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, text)


pdf = PDF()
pdf.add_page()

pdf.chapter_title("Overall Performance")
pdf.chapter_body(f"Average Score: {avg_score:.2f}")

pdf.chapter_title("Individual Scores")
for index, row in df.iterrows():
    pdf.chapter_body(f"{row['Name']}: {row['Score']}")


pdf.output("score_report.pdf")
print(" Report generated: 'score_report.pdf'")
