import subprocess
import os
from pdf2docx import Converter

def convert_pdf_to_docx(input_path: str, output_path: str) -> bool:
    """Converts a PDF file to a DOCX file using the pdf2docx library.
    Args:
        input_path: Full path to the input PDF file.
        output_path: Full path for the output DOCX file.
        
    Returns:
        True if conversion is successful, False otherwise.
    """
    try:
        cv = Converter(input_path)
        cv.convert(output_path)
        cv.close()
        return os.path.exists(output_path)
    
    except Exception as e:
        print(f"ERROR: PDF to DOCX conversion failed for {input_path}. Reason: {e}")
        return False
    
def convert_docx_to_pdf(input_path: str, output_dir: str) -> str | None:
    """
    Converts a DOCX file to a PDF file using the headless LibreOffice installation.
    
    Args:
        input_path: Full path to the input DOCX file.
        output_dir: Directory where the PDF will be saved.
    
    Returns:
        The full path to the output PDF file, or None if conversion fails.
    """
    try:
        command = [
            'libreoffice',
            '--headless',
            '--convert-to', 'pdf',
            '--outdir', output_dir,
            input_path
        ]

        subprocess.run(command, check=True, capture_output=True, text=True)

        base_name = os.path.basename(input_path)
        file_name_without_ext = os.path.splitext(base_name)[0]
        output_filename = f"{file_name_without_ext}.pdf"
        output_path = os.path.join(output_dir, output_filename)

        if os.path.exists(output_path):
            return output_path
        else:
            print(f"ERROR: DOCX to PDF conversion failed. Output file not found at {output_path}")
            return None
    except subprocess.CalledProcessError as e:
        print(f'ERROR: LibreOffice command failed. Stderr: {e.stderr}')
        return None
    except Exception as e:
        print(f'ERROR: DOCX to PDF conversion failed. Reason: {e}')
        return None
    