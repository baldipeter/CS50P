import re
import formatting


def cal_qc_excel(c, q, dilq, writer, sheet, ti, row):
    """
    Writes the calibrators', the quality control samples' and the dilution quality control samples' results into an Excel sheet
    """
    # Declare variables
    column = 1
    row_names = ["ID of sample", "Nominal conc. [ng/mL]", "Measured conc. [ng/mL]", "Accuracy [%]",]

    # Name the RUN
    run_name = run_num(sheet)

    # Calibrators to to_excel object
    c[row_names].to_excel(
        excel_writer=writer,
        sheet_name="App V - In study validation",
        index=False,
        header=False,
        startrow=row,
        startcol=column,
    )

    workbook = writer.book
    worksheet = writer.sheets["App V - In study validation"]

    # The formatting module is used
    column_format = formatting.column_format(workbook, 10)
    cell_format = formatting.mark_format(workbook)
    title_format = formatting.column_format(workbook, 12)
    subtitle_format = formatting.subtitle_format(workbook)
    header_format = formatting.cal_header_format(workbook)
    string_format = formatting.string_format(workbook)

    # Set column format
    if row == 5:
        set_columns(worksheet, column_format)

    # Write header
    for col_num, value in enumerate(row_names):
        worksheet.write((row - 2), col_num + 1, value, header_format)

    # Mark if LLOQ (lower limit of quantitation) are out of acceptance range (<= 20%)
    mark_lloq(worksheet, row, column, cell_format)
    # Mark if samples are out of acceptance range (<= 15%)
    mark_rest(c, worksheet, row + 1, column, cell_format)

    # Merge and write title/sub-title
    title_print(worksheet, row - 5, column, "Accuracies of calibrators and QC samples",  title_format,)
    title_print(worksheet, row - 4, column, f"of {ti} - {run_name}", title_format,)
    title_print(worksheet, row - 1, column, "Calibrators", subtitle_format)

    # Set new row parameter for QCs
    row += len(c) + 1

    # QCs to to_excel object
    q[row_names].to_excel(
        excel_writer=writer,
        sheet_name="App V - In study validation",
        index=False,
        header=False,
        startrow=row,
        startcol=column,
    )

    # Mark if QC samples are out of acceptance range
    mark_rest(q, worksheet, row, column, cell_format)

    # Print title
    title_print(worksheet, row - 1, column, "Quality control samples", subtitle_format)

    row += len(q)

    # If there are dilQCs write them
    if dilq.empty != True:
        row += 1
        dilq[row_names].to_excel(
            excel_writer=writer,
            sheet_name="App V - In study validation",
            index=False,
            header=False,
            startrow=row,
            startcol=column,
        )

        # Mark if sample out of acceptance range
        mark_rest(dilq, worksheet, row, column, cell_format)

        title_print(worksheet, row - 1, column, "Dilution samples", subtitle_format)

    row += len(dilq) + 2

    # Print standard text below the table
    acceptance_parameters(worksheet, row, column, string_format)


def run_num(s):
    """
    Name the RUN based on the Raw Data Excel's sheet names
    """
    num = re.search(r"([0-9]{2}(?:[a-zA-Z]*)?)$", s)
    return f"RUN{num[1]}"


def set_columns(wsheet, colmn_format):
    """
    Column formatting
    """
    wsheet.set_column("B:E", 15.2, colmn_format,)
    wsheet.set_column("A:A", 1,)
    wsheet.set_column("F:F", 1,)


def mark_lloq(ws, rw, col, c_format):
    """
    Mark Lower Limit of Quantitation samples if out of range
    """
    col = col + 3
    ws.conditional_format(rw, col, rw, col,
        {"type": "cell", "criteria": ">=", "value": 20, "format": c_format},
    )
    ws.conditional_format(rw, col, rw, col,
        {"type": "cell", "criteria": "<=", "value": (-20), "format": c_format},
    )


def mark_rest(dframe, ws, rw, col, cell_form):
    """
    Mark the rest of the samples if out of range
    """
    col = col + 3
    ws.conditional_format(rw, col, rw + len(dframe), col,
        {"type": "cell", "criteria": ">=", "value": 15, "format": cell_form},
    )
    ws.conditional_format(rw, col, rw + len(dframe), col,
        {"type": "cell", "criteria": "<=", "value": (-15), "format": cell_form},
    )


def title_print(ws, ro, co, string, format):
    ws.merge_range(ro, co, ro, co + 3, string, format,)


def acceptance_parameters(works, r, c, s_form):
    """
    Print standard text below the table
    """
    works.write(r + 0, c, "Acceptance criteria:", s_form)
    works.write(r + 1, c, " Accuracy  ≤ ± 20% for C1, ≤ ± 15% for all other samples", s_form)
    works.write(r + 2, c, " Accuracy %:  (measured conc.- nominal conc.)/nominal conc. * 100",s_form,)
    works.write(r + 4, c, "Acceptance of the run:", s_form)
    works.write(r + 5, c, "Accuracy of at least 75% of calibrators and 67% of QC samples ", s_form,)
    works.write(r + 6, c, "(at least 50% at each conc. level) meet the acceptance criteria; r: ≥ 0.99", s_form,)
    works.write(r + 8, c, "To accept the results of the diluted samples at least 67% of the diluted high", s_form,)
    works.write(r + 9, c, "concentration QC samples should be within ±15% of their respective nominal value.", s_form,)
    works.write(r + 11, c, "Parameters of the calibration curve:", s_form)
    works.write(r + 12, c, "Equation (correlation):", s_form)
