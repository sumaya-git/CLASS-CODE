from datetime import date 
from pathlib import Path

from flask import Flask, render_template 
from src import utils
 
 
app = Flask(__name__) 

FILE_PATH = str(Path(__file__).parent.parent / "invoice" / "invoice_template.xlsx")

 
@app.route('/') 

def home(): 
    #invoice_created_at = date.today().strftime('%d %b %Y') 
    return render_template(
        "invoice.html", 
        date=utils.extract_excel_file(FILE_PATH), 
        **utils.get_company_info(),
        **utils.get_user_info(),
        **utils.get.invoice_header_info(),
    )
    

 
 
if __name__ == "__main__": 
    app.run(debug=True) 

 