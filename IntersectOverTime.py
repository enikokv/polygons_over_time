import arcpy

arcpy.env.overwriteoutput=True

inFeature1 = arcpy.GetParameterAsText(0)
inFeature2= arcpy.GetParameterAsText(1)
inFeatureTime_1= arcpy.GetParameterAsText(2)
inFeatureTime_2= arcpy.GetParameterAsText(3)

fields=arcpy.ListFields(inFeature1)
if "TIME" not in fields:
    arcpy.AddField_management(inFeature1, "TIME", "DOUBLE", "", "", "25", "", "NULLABLE", "REQUIRED", "")
    cursor = arcpy.UpdateCursor(inFeature1)
    for row in cursor:
        row.setValue("TIME", inFeatureTime_1)
        cursor.updateRow(row)

fields=arcpy.ListFields(inFeature2)
if "TIME" not in fields:
    arcpy.AddField_management(inFeature2, "TIME", "DOUBLE", "", "", "25", "", "NULLABLE", "REQUIRED", "")
    cursor = arcpy.UpdateCursor(inFeature2)
    for row in cursor:
        row.setValue("TIME", inFeatureTime_2)
        cursor.updateRow(row)

inFeatures=[inFeature1,inFeature2]
outFeatures = arcpy.GetParameterAsText(4)
arcpy.Intersect_analysis (inFeatures, outFeatures, "ALL")

arcpy.AddMessage("Script was run. To see result check Feature Class having Name of the Output Folder.")

### Intersect_analysis (in_features, out_feature_class, {join_attributes}, {cluster_tolerance}, {output_type})



