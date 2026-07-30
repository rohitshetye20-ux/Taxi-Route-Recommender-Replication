"""
styles.py

Defines document styles and page layout for the
Final Report Builder Framework v2.0.
"""

from docx.shared import Pt
from docx.shared import Inches

from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_LINE_SPACING


# ==========================================================
# FONT SETTINGS
# ==========================================================

BODY_FONT = "Times New Roman"

HEADING_FONT = "Times New Roman"

BODY_FONT_SIZE = 12

HEADING1_SIZE = 18

HEADING2_SIZE = 16

HEADING3_SIZE = 14

CAPTION_SIZE = 11


# ==========================================================
# APPLY STYLES
# ==========================================================

def apply_styles(document):
    """
    Configure all document styles.
    """

    styles = document.styles

    # ------------------------------------------------------
    # Normal
    # ------------------------------------------------------

    normal = styles["Normal"]

    normal.font.name = BODY_FONT

    normal.font.size = Pt(BODY_FONT_SIZE)

    normal.paragraph_format.line_spacing_rule = (
        WD_LINE_SPACING.ONE_POINT_FIVE
    )

    normal.paragraph_format.space_after = Pt(6)

    # ------------------------------------------------------
    # Heading 1
    # ------------------------------------------------------

    heading1 = styles["Heading 1"]

    heading1.font.name = HEADING_FONT

    heading1.font.size = Pt(HEADING1_SIZE)

    heading1.font.bold = True

    heading1.paragraph_format.space_before = Pt(18)

    heading1.paragraph_format.space_after = Pt(12)

    # ------------------------------------------------------
    # Heading 2
    # ------------------------------------------------------

    heading2 = styles["Heading 2"]

    heading2.font.name = HEADING_FONT

    heading2.font.size = Pt(HEADING2_SIZE)

    heading2.font.bold = True

    heading2.paragraph_format.space_before = Pt(14)

    heading2.paragraph_format.space_after = Pt(8)

    # ------------------------------------------------------
    # Heading 3
    # ------------------------------------------------------

    heading3 = styles["Heading 3"]

    heading3.font.name = HEADING_FONT

    heading3.font.size = Pt(HEADING3_SIZE)

    heading3.font.bold = True

    heading3.paragraph_format.space_before = Pt(12)

    heading3.paragraph_format.space_after = Pt(6)

    # ------------------------------------------------------
    # Caption Style
    # ------------------------------------------------------

    if "Caption" in styles:

        caption = styles["Caption"]

    else:

        caption = styles.add_style(
            "Caption",
            WD_STYLE_TYPE.PARAGRAPH
        )

    caption.font.name = BODY_FONT

    caption.font.size = Pt(CAPTION_SIZE)

    caption.font.italic = True

    caption.paragraph_format.space_before = Pt(4)

    caption.paragraph_format.space_after = Pt(10)

    # ------------------------------------------------------
    # Intense Quote
    # ------------------------------------------------------

    if "Intense Quote" in styles:

        quote = styles["Intense Quote"]

        quote.font.name = BODY_FONT

        quote.font.size = Pt(11)

    # ------------------------------------------------------
    # List Bullet
    # ------------------------------------------------------

    if "List Bullet" in styles:

        bullet = styles["List Bullet"]

        bullet.font.name = BODY_FONT

        bullet.font.size = Pt(BODY_FONT_SIZE)

    # ------------------------------------------------------
    # List Number
    # ------------------------------------------------------

    if "List Number" in styles:

        numbered = styles["List Number"]

        numbered.font.name = BODY_FONT

        numbered.font.size = Pt(BODY_FONT_SIZE)


# ==========================================================
# PAGE LAYOUT
# ==========================================================

def apply_page_layout(document):
    """
    Configure A4 page layout.
    """

    section = document.sections[0]

    section.page_width = Inches(8.27)

    section.page_height = Inches(11.69)

    section.top_margin = Inches(1)

    section.bottom_margin = Inches(1)

    section.left_margin = Inches(1)

    section.right_margin = Inches(1)

    section.gutter = 0

    section.start_type = WD_SECTION.NEW_PAGE

    