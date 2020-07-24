import arcpy

# Calculates difference between the new and old Attributes
arcpy.env.overwriteoutput=True

inFeature = arcpy.GetParameterAsText(0)
arcpy.AddField_management(inFeature, "DIFFERENCE", "DOUBLE", "", "", "25", "", "NULLABLE", "REQUIRED", "")

cursor = arcpy.UpdateCursor(inFeature)
for row in cursor:
    # field3 will be equal to field2 minus field1
    row.setValue("DIFFERENCE", row.getValue("Attribute2")- row.getValue("Attribute1"))
    cursor.updateRow(row)

arcpy.AddMessage("Script was run. To see result check Feature Class having Name of the Output Folder.")
