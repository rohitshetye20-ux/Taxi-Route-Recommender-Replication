"""
exporter.py

Report Exporter
Report Builder Framework v2.0
"""

from pathlib import Path


class ReportExporter:
    """
    Handles exporting the final report.
    """

    def __init__(self, document):

        self.document = document

    # ======================================================
    # DOCX EXPORT
    # ======================================================

    def save_docx(self, output_path):
        """
        Save the report as a DOCX file.
        """

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.document.save(output_path)

        print()

        print("=" * 60)
        print("REPORT EXPORTED SUCCESSFULLY")
        print("=" * 60)

        print(f"Location : {output_path}")

        print(f"Size     : {output_path.stat().st_size:,} bytes")

        return output_path

    # ======================================================
    # PDF PLACEHOLDER
    # ======================================================

    def save_pdf(self, output_path=None):
        """
        Placeholder for future PDF export support.
        """

        print()

        print("=" * 60)
        print("PDF EXPORT")
        print("=" * 60)

        print(
            "PDF export is not implemented in Report Builder v2.0."
        )

        print(
            "Generate the DOCX first and export it as a PDF "
            "using Microsoft Word."
        )

        return None