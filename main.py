from pyresparser import ResumeParser
import warnings
warnings.filterwarnings('ignore')
data = ResumeParser('/home/shrey01/Resume_reader/ShreyCV-1.pdf.pdf').get_extracted_data()
print(data)