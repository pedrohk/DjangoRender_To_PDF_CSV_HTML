# Render PDF, HTML and CSV Views in Django

A Django render exemple to generate a page in HTML, PDF or CSV

DjangoRender_To_PDF_CSV_HTML/
├── src/
│   ├── templates/
│   │ 		└──index.html
│   │ 		renderer/   
│   │   		├── invoice_html.html
│   │   		├── invoice_pdf.html
│   │   		└── myTemplate.csv
│   ├── views.py
│   ├── urls.py
│   ├── settings.py
│ 	├── renderers.py
│	├── asgi.py
│	├── wsgi.py
│   └── urls.py
├── manage.py
├── DjangoRender_To_PDF_CSV_HTML/


I used the reference code from: https://www.codingforentrepreneurs.com/blog/html-template-to-pdf-in-django
