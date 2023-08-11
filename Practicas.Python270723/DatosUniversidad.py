# coding=utf8
# https://www.educaweb.com/contenidos/educativos/selectividad/fechas-realizacion-examenes-selectividad/
# https://regex101.com/r/EfCvR7/1/codegen?language=python
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"<td>(.*)<\/td>|<strong>(.*)<\/strong>"

test_str = ("<table border=\"1\" class=\"tGrisos\" style=\"width:95%\">\n"
	" <tbody>\n"
	"  <tr>\n"
	"   <th colspan=\"1\" rowspan=\"1\"><br />\n"
	"   Comunidad autónoma<br />\n"
	"    </th>\n"
	"   <th><br />\n"
	"    Convocatoria ordinaria<br />\n"
	"    </th>\n"
	"   <th><br />\n"
	"   Convocatoria extraordinaria<br />\n"
	"    </th>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Andalucía</td>\n"
	"   <td style=\"text-align:center\"><strong>13, 14 y 15 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>11, 12 y 13 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Aragón</td>\n"
	"   <td style=\"text-align:center\"><strong>6, 7 y 8 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>4, 5 y 6 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Cantabria</td>\n"
	"   <td style=\"text-align:center\"><strong>5, 6 y 7 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>5, 6 y 7 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Castilla-La Mancha</td>\n"
	"   <td style=\"text-align:center\"><strong>12, 13 y 14 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>3, 4 y 5 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Castilla y León</td>\n"
	"   <td style=\"text-align:center\"><strong>7, 8 y 9 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>5, 6 y 7 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Catalunya</td>\n"
	"   <td style=\"text-align:center\"><strong>7, 8 y 9 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>5, 6 y 7 de septiembre</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Comunidad de Madrid</td>\n"
	"   <td style=\"text-align:center\"><strong>5, 6, 7 y 8 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>4, 5 y 6 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Comunidad Foral de Navarra</td>\n"
	"   <td style=\"text-align:center\"><strong>6, 7 y 8 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>28, 29 y 30 de junio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Comunitat Valenciana</td>\n"
	"   <td style=\"text-align:center\"><strong>6, 7 y 8 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>4, 5 y 6 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Euskadi</td>\n"
	"   <td style=\"text-align:center\"><strong>7, 8 y 9 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>5, 6 y 7 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Extremadura</td>\n"
	"   <td style=\"text-align:center\"><strong>6, 7 y 8 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>4, 5 y 6 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Galicia</td>\n"
	"   <td style=\"text-align:center\"><strong>6, 7 y 8 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>11, 12 y 13 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Illes Balears</td>\n"
	"   <td style=\"text-align:center\"><strong>6, 7 y 8 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>4, 5 y 6 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Islas Canarias</td>\n"
	"   <td style=\"text-align:center\"><strong>7, 8, 9 y 10 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>5, 6 y 7 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>La Rioja</td>\n"
	"   <td style=\"text-align:center\"><strong>5, 6 y 7 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>5, 6 y 7 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Principado de Asturias</td>\n"
	"   <td style=\"text-align:center\"><strong>6, 7 y 8 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>5, 6 y 7 de julio</strong></td>\n"
	"  </tr>\n"
	"  <tr>\n"
	"   <td>Región de Murcia</td>\n"
	"   <td style=\"text-align:center\"><strong>5, 6 y 7 de junio</strong></td>\n"
	"   <td style=\"text-align:center\"><strong>3, 4 y 5 de julio</strong></td>\n"
	"  </tr>\n"
	" </tbody>\n"
	"</table>")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    #print ("Match was found: {match}".format(match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        if match.group(groupNum) != None:
        	print ("Found at: {group}".format(group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
