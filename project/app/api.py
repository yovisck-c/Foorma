from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
import uuid
from pathlib import Path
from .conversion_logic import convert_pdf_to_docx, convert_docx_to_pdf


#        |\___/|     /\___/\
#        )     (     )    ~(
#       =\     /=   =\~    /=
#         )===(       ) ~ (
#        /     \     /     \    
#        |     |     ) ~   (
#       /       \   /     ~ \
#       \       /   \~     ~/
#========\__ __/=====\__~__/==============================================
#           (( !Kitties! ))               Follow me on instagram!      
#===========))=========//=================================================
#          ((         ((                                        @piromali_
#           \)         \)


app = FastAPI(
    title="Document Converter API",
    description="API for high-quality document conversions (PDF <-> DOCX)."
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://host.docker.internal:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMP_DIR = "/tmp/converter"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

MAX_FILE_SIZE_BYTES = 50 * 1024 * 1024 

async def validate_file_size(file: UploadFile):
    """
    Checks if the uploaded file size exceeds the defined limit (MAX_FILE_SIZE_BYTES).
    Raises an HTTP 413 error if the file is too large.
    """
    await file.seek(0, 2) 
    file_size = await file.tell() 
    
    await file.seek(0) 

    if file_size > MAX_FILE_SIZE_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"File size limit exceeded. Max size is {MAX_FILE_SIZE_BYTES / (1024 * 1024):.0f} MB."
        )
    return file


def handle_upload(file: UploadFile, temp_dir: str, target_ext: str) -> tuple[str, str]:
    """Saves the uploaded file and returns the input path and expected output filename."""
    unique_id = str(uuid.uuid4())
    original_ext = file.filename.split('.')[-1]
    input_path = os.path.join(temp_dir, f"{unique_id}.{original_ext}")
    
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    base_name = Path(file.filename).stem
    output_filename = f"{base_name}_converted.{target_ext}"
    
    return input_path, output_filename


@app.get("/")
async def read_root():
    """A simple root endpoint to check if the API is running."""
    return {"message": "Converter API is running! Use /convert/{format}"}


@app.post("/convert/pdf-to-docx")
async def pdf_to_docx_endpoint(file: UploadFile = Depends(validate_file_size)):
    """
    Handles the PDF to DOCX conversion request.
    Uses Dependency Injection for file size validation.
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded.")

    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF file.")

    input_path, output_filename = handle_upload(file, TEMP_DIR, "docx")
    output_path = os.path.join(TEMP_DIR, output_filename)
    
    try:
        success = convert_pdf_to_docx(input_path, output_path)
        
        if success and os.path.exists(output_path):
            return FileResponse(
                path=output_path, 
                media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", 
                filename=output_filename
            )
        else:
            raise HTTPException(status_code=500, detail="Conversion failed. Output file not generated.")

    finally:
        if os.path.exists(input_path): os.remove(input_path)
        if os.path.exists(output_path): os.remove(output_path)


@app.post("/convert/docx-to-pdf")
async def docx_to_pdf_endpoint(file: UploadFile = Depends(validate_file_size)):
    """
    Handles the DOCX to PDF conversion request.
    Uses Dependency Injection for file size validation.
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded.")

    if not file.filename.lower().endswith(('.docx', '.doc')):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a DOCX or DOC file.")

    input_path, _ = handle_upload(file, TEMP_DIR, "pdf")
    output_path = None
    
    try:
        output_path = convert_docx_to_pdf(input_path, TEMP_DIR)
        
        if output_path and os.path.exists(output_path):
            return FileResponse(
                path=output_path, 
                media_type="application/pdf", 
                filename=os.path.basename(output_path)
            )
        else:
            raise HTTPException(status_code=500, detail="Conversion failed. Check API logs.")

    finally:
        if os.path.exists(input_path): os.remove(input_path)
        if output_path and os.path.exists(output_path): os.remove(output_path)