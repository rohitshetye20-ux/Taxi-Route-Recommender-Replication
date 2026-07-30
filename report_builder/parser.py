"""
parser.py

Markdown parser for the Final Report Builder.
"""

import re
from pathlib import Path

from report_builder.tables import TableRenderer
from report_builder.figures import FigureRenderer


class MarkdownParser:
    """
    Parses Markdown files into a Word document.
    """

    def __init__(self, document):

        self.document = document

        self.table_renderer = TableRenderer(document)

        self.figure_renderer = FigureRenderer(document)

    # ---------------------------------------------------------

    def parse_file(self, filepath):

        filepath = Path(filepath)

        print(f"Reading: {filepath.name}")

        with open(filepath, "r", encoding="utf-8") as f:

            text = f.read()

        self.parse_text(text)

    # ---------------------------------------------------------

    def parse_text(self, text):

        lines = text.splitlines()

        i = 0

        while i < len(lines):

            line = lines[i].rstrip()

            # -----------------------------
            # Skip blank lines
            # -----------------------------

            if not line:

                i += 1
                continue

            # -----------------------------
            # Markdown Table
            # -----------------------------

            if "|" in line:

                table_lines = []

                while i < len(lines):

                    current = lines[i].rstrip()

                    if "|" not in current:

                        break

                    table_lines.append(current)

                    i += 1

                if len(table_lines) >= 2:

                    self.table_renderer.render(table_lines)

                    continue

            # -----------------------------
            # Figure Placeholder
            # -----------------------------

            # Format 1:
            # [FIGURE: Repository Architecture]

            if line.startswith("[FIGURE:"):

                figure = (
                    line.replace("[FIGURE:", "")
                    .replace("]", "")
                    .strip()
                )

                self.figure_renderer.render(figure)

                i += 1

                continue

            # -----------------------------
            # Format 2:
            # *<<Insert Repository Architecture Diagram>>*
            # -----------------------------

            if "<<Insert" in line:

                figure = (
                    line.replace("*", "")
                    .replace("<<Insert", "")
                    .replace("Diagram>>", "")
                    .replace(">>", "")
                    .strip()
                )

                self.figure_renderer.render(figure)

                i += 1

                continue

            # -----------------------------

            self.parse_line(line)

            i += 1

    # ---------------------------------------------------------

    def parse_line(self, line):

        line = line.strip()

        # -----------------------------
        # Heading 1
        # -----------------------------

        if line.startswith("# "):

            self.document.add_heading(
                line[2:],
                level=1
            )

            return

        # -----------------------------

        if line.startswith("## "):

            self.document.add_heading(
                line[3:],
                level=2
            )

            return

        # -----------------------------

        if line.startswith("### "):

            self.document.add_heading(
                line[4:],
                level=3
            )

            return

        # -----------------------------
        # Bullet List
        # -----------------------------

        if line.startswith("- "):

            self.document.add_paragraph(
                line[2:],
                style="List Bullet"
            )

            return

        # -----------------------------
        # Numbered List
        # -----------------------------

        if re.match(r"^\d+\.", line):

            text = re.sub(
                r"^\d+\.\s*",
                "",
                line
            )

            self.document.add_paragraph(
                text,
                style="List Number"
            )

            return

        # -----------------------------
        # Horizontal Rule
        # -----------------------------

        if line.startswith("---"):

            self.document.add_paragraph(
                "────────────────────────────"
            )

            return

        # -----------------------------
        # Normal Paragraph
        # -----------------------------

        self.document.add_paragraph(line)