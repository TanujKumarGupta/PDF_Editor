
import pypdf
from pypdf import PdfWriter,PdfReader
import os
''' MERGE PDF CODE
files=os.listdir("D:\\photopy")
final=PdfWriter()
for file in files:
    if file.endswith(".pdf"):
        final.append(file)

final.write("final.pdf")  # same as final.write("D:\\photopy\final.pdf") a swe have already opened the folder
final.close() '''

''' ENCRYPTED PDF
reader=PdfReader("merged.pdf")
writer=PdfWriter(clone_from=reader)

writer.encrypt(
    user_password="123456",
    algorithm="AES-256"
)
writer.write("merged_encrpyted.pdf")'''

''' DECRYPTION
reader=PdfReader("aadhaar.pdf")
if reader.is_encrypted:
    reader.decrypt("TANU2005")
writer=PdfWriter()
writer=PdfWriter(clone_from=reader)
writer.write("aadhaar_decrypted.pdf")
# with open("aadhaar.pdf","wb") as f:   this decryptes the original file
#     writer.write(f)
'''