def column_format(workbook, num):
    column_format = workbook.add_format(
        {
            "font_name": "Times New Roman",
            "font_size": num,
            "align": "center",
            "valign": "vcenter",
        }
    )
    return column_format


def cell_format(workbook):
    cell_format = workbook.add_format(
        {
            "font_name": "Times New Roman",
            "font_size": 10,
            "align": "center",
            "valign": "vcenter",
            "border": True,
        }
    )
    return cell_format


def title_format(workbook):
    title_format = workbook.add_format(
        {
            "font_name": "Times New Roman",
            "font_size": 10,
            "align": "center",
            "valign": "vcenter",
            "border": True,
            "bold": True,
        }
    )
    return title_format


def header_format(workbook):
    header_format = workbook.add_format(
        {
            "font_name": "Times New Roman",
            "font_size": 10,
            "align": "center",
            "valign": "vcenter",
            "border": True,
            "text_wrap": True,
            "rotation": 90,
        }
    )
    return header_format


def cal_header_format(workbook):
    header_format = workbook.add_format(
        {
            "font_name": "Times New Roman",
            "font_size": 10,
            "align": "center",
            "valign": "vcenter",
            "border": True,
            "text_wrap": True,
            "rotation": 0,
        }
    )
    return header_format


def warp_format(workbook):
    warp_format = workbook.add_format(
        {
            "font_name": "Times New Roman",
            "font_size": 10,
            "align": "center",
            "valign": "vcenter",
            "text_wrap": True,
        }
    )
    return warp_format


def mark_format(workbook):
    mark_format = workbook.add_format(
        {
            "font_name": "Times New Roman",
            "font_size": 10,
            "align": "center",
            "valign": "vcenter",
            "italic": True,
            "bold": True,
            "underline": True,
        }
    )
    return mark_format


def subtitle_format(workbook):
    subtitle_format = workbook.add_format(
        {
            "font_name": "Times New Roman",
            "font_size": 10,
            "align": "center",
            "valign": "vcenter",
            "bold": True,
            "top": True,
            "bottom": True,
        }
    )
    return subtitle_format


def string_format(workbook):
    string_format = workbook.add_format(
        {
            "font_name": "Times New Roman",
            "font_size": 10,
        }
    )
    return string_format
