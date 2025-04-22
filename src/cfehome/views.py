import csv
import locale
from django.template import loader

from django.http import *
from . import renderers

from django.shortcuts import render


def index(request):   
    return render(request, 'index.html')

def invoice_view_html(request):    
        context = {
            "bill_to": "Pedro Kuhn",
            "invoice_number": "0354784FERS",
            "amount": 35_000,
            "date": "2025-04-14",
        }       
        return render(request, 'renderer/invoice_html.html', context)

   

def invoice_view_csv(request):
    context = {
        "bill_to": "Pedro Kuhn",
        "invoice_number": "0354784FERS",
        "amount": 35_000,
        "date": "2025-04-14",
    }
   # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="myTemplate.csv"'},
    )

    writer = csv.writer(response)    
    writer.writerow(["bill_to" ';' "invoice_number" ';' "amount" ';' "date"])
    writer.writerow(['Pedro Kuhn' ';' "0354784FERS" ';' '35.000' ';' "2025-04-14"])

    return response



def invoice_view_pdf(request):
    context = {
        "bill_to": "Pedro Kuhn",
        "invoice_number": "0354784FERS",
        "amount": 35_000,
        "date": "2025-04-14",
    }
    return renderers.render_to_pdf("renderer/invoice_pdf.html", context)


def advanced_pdf_view(request):
    locale.setlocale(locale.LC_ALL, "")
    invoice_number = "0354784FERS"
    context = {
        "bill_to": "Pedro Kuhn",
        "invoice_number": f"{invoice_number}",
        "amount": locale.currency(35_000, grouping=True),
        "date": "2025-04-14",
        "pdf_title": f"Invoice #{invoice_number}",
    }
    response = renderers.render_to_pdf("renderer/invoice_pdf.html", context)
    if response.status_code == 404:
        raise Http404("Invoice not found")

    filename = f"Invoice_{invoice_number}.pdf"
    """
    Tell browser to view inline (default)
    """
    content = f"inline; filename={filename}"
    download = request.GET.get("download")
    if download:
        """
        Tells browser to initiate download
        """
        content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content
    return response
