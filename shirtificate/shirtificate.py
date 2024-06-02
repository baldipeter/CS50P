from fpdf import FPDF, Align


class PDF(FPDF):
    def header(self):
        self.ln(20)
        self.set_font("helvetica", "B", 45)
        self.cell(0, 10, "CS50 Shirtificate", align="C")

    def picture(self, img):
        self.image(img, x=Align.C, y=70)

    def text(self, txt):
        self.ln(105)
        self.set_font("helvetica", "B", 30)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f"{txt} took CS50", align="C")


def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.picture("shirtificate.png")
    pdf.text(name)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
