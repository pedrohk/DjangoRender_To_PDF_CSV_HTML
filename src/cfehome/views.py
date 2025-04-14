import locale

from . import renderers


def invoice_view(request):
    context = {
        "bill_to": "Pedro Kuhn",
        "invoice_number": "0354784FERS",
        "amount": 35_000,
        "date": "2025-04-14",
    }
    return renderers.render_to_pdf("pdfs/invoice.html", context)


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
    response = renderers.render_to_pdf("pdfs/invoice.html", context)
    if response.status_code == 404:
        raise HTTP404("Invoice not found")

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
    return response
