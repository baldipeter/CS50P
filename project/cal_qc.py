import re
import formatting


def cal_qc_excel(cal, qc, dil_qc, writer, sheet, test_item, row, column_names):
    """
    Writes the calibrators', the quality control samples' and the dilution quality control samples' results into an Excel sheet
    """
    # Declare variables
    column = 1
    row_names = [column_names['id'][0], "Nominal conc. [ng/mL]", "Measured conc. [ng/mL]", "Accuracy [%]",]

    # Name the RUN
    run_name = run_num(sheet)

    # Calibrators to to_excel object
    cal[row_names].to_excel(
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
    mark_rest(cal, worksheet, row + 1, column, cell_format)

    # Merge and write title/sub-title
    title_print(worksheet, row - 5, column, "Accuracies of calibrators and QC samples",  title_format,)
    title_print(worksheet, row - 4, column, f"of {test_item} - {run_name}", title_format,)
    title_print(worksheet, row - 1, column, "Calibrators", subtitle_format)

    # Set new row parameter for QCs
    row += len(cal) + 1

    # QCs to to_excel object
    qc[row_names].to_excel(
        excel_writer=writer,
        sheet_name="App V - In study validation",
        index=False,
        header=False,
        startrow=row,
        startcol=column,
    )

    # Mark if QC samples are out of acceptance range
    mark_rest(qc, worksheet, row, column, cell_format)

    # Print title
    title_print(worksheet, row - 1, column, "Quality control samples", subtitle_format)

    row += len(qc)

    # If there are dilQCs write them
    if dil_qc.empty != True:
        row += 1
        dil_qc[row_names].to_excel(
            excel_writer=writer,
            sheet_name="App V - In study validation",
            index=False,
            header=False,
            startrow=row,
            startcol=column,
        )

        # Mark if sample out of acceptance range
        mark_rest(dil_qc, worksheet, row, column, cell_format)

        title_print(worksheet, row - 1, column, "Dilution samples", subtitle_format)

    row += len(dil_qc) + 2

    # Print standard text below the table
    acceptance_parameters(worksheet, row, column, string_format)


def run_num(s):
    """
    Name the RUN based on the Raw Data Excel's sheet names
    """
    num = re.search(r"([0-9]{2}(?:[a-zA-Z]*)?)$", s)
    return f"RUN{num[1]}"


def set_columns(worksheet, colmn_format):
    """
    Column formatting
    """
    worksheet.set_column("B:E", 15.2, colmn_format,)
    worksheet.set_column("A:A", 1,)
    worksheet.set_column("F:F", 1,)


def mark_lloq(worksheet, row, col, format):
    """
    Mark Lower Limit of Quantitation samples if out of range
    """
    col = col + 3
    worksheet.conditional_format(row, col, row, col,
        {"type": "cell", "criteria": ">=", "value": 20, "format": format},
    )
    worksheet.conditional_format(row, col, row, col,
        {"type": "cell", "criteria": "<=", "value": (-20), "format": format},
    )


def mark_rest(df, worksheet, row, col, format):
    """
    Mark the rest of the samples if out of range
    """
    col = col + 3
    worksheet.conditional_format(row, col, row + len(df), col,
        {"type": "cell", "criteria": ">=", "value": 15, "format": format},
    )
    worksheet.conditional_format(row, col, row + len(df), col,
        {"type": "cell", "criteria": "<=", "value": (-15), "format": format},
    )


def title_print(worksheet, row, col, string, format):
    worksheet.merge_range(row, col, row, col + 3, string, format,)


def acceptance_parameters(works, row, column, string_format):
    """
    Print standard text below the table
    """
    works.write(row + 0, column, "Acceptance criteria:", string_format)
    works.write(row + 1, column, " Accuracy  ≤ ± 20% for C1, ≤ ± 15% for all other samples", string_format)
    works.write(row + 2, column, " Accuracy %:  (measured conc.- nominal conc.)/nominal conc. * 100",string_format,)
    works.write(row + 4, column, "Acceptance of the run:", string_format)
    works.write(row + 5, column, "Accuracy of at least 75% of calibrators and 67% of QC samples ", string_format,)
    works.write(row + 6, column, "(at least 50% at each conc. level) meet the acceptance criteria; r: ≥ 0.99", string_format,)
    works.write(row + 8, column, "To accept the results of the diluted samples at least 67% of the diluted high", string_format,)
    works.write(row + 9, column, "concentration QC samples should be within ±15% of their respective nominal value.", string_format,)
    works.write(row + 11, column, "Parameters of the calibration curve:", string_format)
    works.write(row + 12, column, "Equation (correlation):", string_format)
