import os
import pandas as pd
from flask import Flask, send_file, render_template
from weasyprint import HTML

app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page with a download button
    return render_template('index.html')

@app.route('/generate_pdf', methods=['GET'])
def generate_pdf():
    # Example energy data (replace with actual data from Home Assistant)
    data = {
        "date": ["2024-12-01", "2024-12-02", "2024-12-03"],
        "consumption_kWh": [10.5, 12.3, 11.8],
        "cost_eur": [2.1, 2.5, 2.3]
    }
    df = pd.DataFrame(data)

    # Render the HTML template with data
    rendered_html = render_template('report_template.html', table=df.to_html(index=False))
    pdf = HTML(string=rendered_html).write_pdf()

    # Save the PDF to a file
    pdf_path = '/app/output/energy_report.pdf'
    with open(pdf_path, 'wb') as f:
        f.write(pdf)

    return send_file(pdf_path, as_attachment=True, download_name='energy_report.pdf')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
