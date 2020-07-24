import arcpy

arcpy.env.overwriteoutput=True

# File and layer names
inFeature1 = arcpy.GetParameterAsText(0)
inFeature2 = arcpy.GetParameterAsText(1)
inFeature3 = arcpy.GetParameterAsText(2)
inFeature4 = arcpy.GetParameterAsText(3)

# Add Attribute1 Field to the oldest Feature Class
arcpy.AddField_management(inFeature1, "Attribute1", "DOUBLE", "", "", "25", "", "NULLABLE", "REQUIRED", "")
cursor = arcpy.UpdateCursor(inFeature1)
for row in cursor:
    row.setValue("Attribute1", row.getValue(inFeature3))
    cursor.updateRow(row)

#Add Attribute Field2 to the newest feature class
arcpy.AddField_management(inFeature2, "Attribute2", "DOUBLE", "", "", "25", "", "NULLABLE", "REQUIRED", "")
cursor = arcpy.UpdateCursor(inFeature2)
for row in cursor:
    row.setValue("Attribute2", row.getValue(inFeature4))
    cursor.updateRow(row)

outFeatures = arcpy.GetParameterAsText(4)

arcpy.Identity_analysis(inFeature2, inFeature1, outFeatures)


arcpy.AddMessage("Script was run. To see result check Feature Class having Name of the Output Folder.")
