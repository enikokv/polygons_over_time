import arcpy

arcpy.env.overwriteoutput=True

# UPDATE feature classes: Feature1 with Feature2 after Time Index has been added to each  feature class
inFeatures = arcpy.GetParameterAsText(0)
updateFeatures= arcpy.GetParameterAsText(1)

inFeatureTime_2= arcpy.GetParameterAsText(2)


arcpy.AddField_management(updateFeatures, "TIME", "DOUBLE", "", "", "25", "", "NULLABLE", "REQUIRED", "")
cursor = arcpy.UpdateCursor(updateFeatures)
for row in cursor:
    row.setValue("TIME", inFeatureTime_2)
    cursor.updateRow(row)

outFeatures = arcpy.GetParameterAsText(3)
arcpy.Update_analysis(inFeatures, updateFeatures, outFeatures, "BORDERS", 0.00)

arcpy.AddMessage("Script was run. To see result check Feature Class having Name of the Output Folder.")




