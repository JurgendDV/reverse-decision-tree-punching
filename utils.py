#22:37
def clean_data(data):
    data["Machine1"] = data["Machine1"].fillna("UNKNOWN")
    data.loc[data["Machine1"] == "G_STANS_VISION1", "Machine1"] = 0
    data.loc[data["Machine1"] == "G_STANS_VISION2", "Machine1"] = 1
    data.loc[data["Machine1"] == "G_STANS_MERCO", "Machine1"] = 2
    data.loc[data["Machine1"] == "G_STANS_SEMI", "Machine1"] = 3
    data.loc[data["Machine1"] == "G_STANSSTRAAT", "Machine1"] = 6
    data.loc[data["Machine1"] == "UNKNOWN", "Machine1"] = 7

    data.loc[data["Shape"] == "Snitjes/Glimlachjes", "Shape"] = 0
    data.loc[data["Shape"] == "Deksel diverse", "Shape"] = 1
    data.loc[data["Shape"] == "H-Vorm", "Shape"] = 2
    data.loc[data["Shape"] == "Banderole rechthoekige pot", "Shape"] = 3
    data.loc[data["Shape"] == "Rechthoekig gesneden", "Shape"] = 4
    data.loc[data["Shape"] == "Meerzijdig", "Shape"] = 5
    data.loc[data["Shape"] == "Unknown", "Shape"] = 6
    data.loc[data["Shape"] == "Deksel rond", "Shape"] = 7
    data.loc[data["Shape"] == "Veelhoek/Trapezium/...", "Shape"] = 8
    data.loc[data["Shape"] == "Vijfzijdig", "Shape"] = 9
    data.loc[data["Shape"] == "Diverse", "Shape"] = 10
    data.loc[data["Shape"] == "Banderole ovalen pot", "Shape"] = 11
    data.loc[data["Shape"] == "Driezijdig", "Shape"] = 12
    data.loc[data["Shape"] == "Vijfzijdig margarine", "Shape"] = 13
    data.loc[data["Shape"] == "Deksel ovaal", "Shape"] = 14
    data.loc[data["Shape"] == "Deksel rechthoekig", "Shape"] = 15
    data.loc[data["Shape"] == "Banderole diverse", "Shape"] = 16
    data.loc[data["Shape"] == "Banderole ronde pot", "Shape"] = 17

    data.loc[data["Bars"] == "moet met 2", "Bars"] = 0
    data.loc[data["Bars"] == "1 of 2", "Bars"] = 1    

    data["SelectedRule"] = data["SelectedRule"].fillna("999") 
    
    