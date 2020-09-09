__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/5/2020"

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import inch
from reportlab.graphics.charts.piecharts import Pie

#Data
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

report = SimpleDocTemplate("pdfReport.pdf")
styles = getSampleStyleSheet()
report_pie = Pie(width=3*inch, height=3*inch)

#Title
title = Paragraph("Inventory of Fruits", styles['h1'])

#Table
# table_style = [('GRID', StartCordinate_tuple, EndCordinate_tuple, Thickness, Color)]
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
table = Table(data=table_data, style=table_style, hAlign='LEFT')

#PieChart
report_pie.labels = []
report_pie.data = []
for key in sorted(fruit):
    report_pie.data.append(fruit[key])
    report_pie.labels.append(key)
report_chart = Drawing()
report_chart.add(report_pie)

#Final Build
report.build([title, table, report_chart])
print("report build successfull")

