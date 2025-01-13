FROM python:3.13-slim

COPY convert_excel_to_markdown.py /convert_excel_to_markdown.py

RUN pip install pandas openpyxl

ENTRYPOINT ["python", "/convert_excel_to_markdown.py"]
