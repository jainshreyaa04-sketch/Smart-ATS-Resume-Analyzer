from fpdf import FPDF
import io

def create_pdf(resume_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Helvetica", size=12)

    safe_text = resume_text.encode("latin-1", "ignore").decode("latin-1")

    for line in safe_text.splitlines():
        if line.strip():
            pdf.cell(0, 8, text=line[:90], new_x="LMARGIN", new_y="NEXT")

    pdf_output = pdf.output()

    if isinstance(pdf_output, bytearray):
        pdf_output = bytes(pdf_output)
    elif isinstance(pdf_output, str):
        pdf_output = pdf_output.encode("latin-1")

    return io.BytesIO(pdf_output)