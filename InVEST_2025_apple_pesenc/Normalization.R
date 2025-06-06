### Normalization total species abundance guild_CH_presence_apple

library(raster)

# Verzeichnisse definieren
input_directory <- "O:/Data-Work/27_Natural_Resources-RE/271_KLIM_Work/CC_Impacts/NCCS/Data/M2b_Pollination/InVEST/Species_Input/valpar_bee_presence"   # Pfad anpassen
output_directory <- "O:/Data-Work/27_Natural_Resources-RE/271_KLIM_Work/CC_Impacts/NCCS/Data/M2b_Pollination/InVEST/Species_Input/valpar_bee_presence/Norm" # Pfad für normalisierte Raster
dir.create(output_directory, showWarnings = FALSE)  # Sicherstellen, dass das Output-Verzeichnis existiert

# Funktion zur Normalisierung eines Rasters
normalize_raster <- function(input_path, output_path) {
  raster <- raster(input_path)        # Raster einlesen
  normalized_raster <- raster / 347.49   # Normalisieren 
  
  # Normalisierten Raster speichern
  writeRaster(normalized_raster, datatype = "FLT4S", output_path, overwrite = TRUE)
}

# Alle Rasterdateien im Verzeichnis verarbeiten
files <- list.files(input_directory, pattern = "\\.tif$", full.names = TRUE)
for (file in files) {
  output_file <- file.path(output_directory, basename(file)) # Behalte den Dateinamen bei
  cat("Normalisiere:", file, "->", output_file, "\n")
  normalize_raster(file, output_file)
}




### Normalization 0-1

library(raster)

# Verzeichnisse definieren
input_directory <- "O:/Data-Work/27_Natural_Resources-RE/271_KLIM_Work/CC_Impacts/NCCS/Data/M2b_Pollination/InVEST/Species_Input/valpar_bee_presence"   # Pfad anpassen
output_directory <- "O:/Data-Work/27_Natural_Resources-RE/271_KLIM_Work/CC_Impacts/NCCS/Data/M2b_Pollination/InVEST/Species_Input/valpar_bee_presence/Norm" # Pfad für normalisierte Raster
dir.create(output_directory, showWarnings = FALSE)  # Sicherstellen, dass das Output-Verzeichnis existiert

# Funktion zur Normalisierung eines Rasters
normalize_raster <- function(input_path, output_path) {
  raster <- raster(input_path)        # Raster einlesen
  normalized_raster <- raster / 100   # Normalisieren (0–100 -> 0–1)
  
  # Normalisierten Raster speichern
  writeRaster(normalized_raster, output_path, overwrite = TRUE)
}

# Alle Rasterdateien im Verzeichnis verarbeiten
files <- list.files(input_directory, pattern = "\\.tif$", full.names = TRUE)
for (file in files) {
  output_file <- file.path(output_directory, basename(file)) # Behalte den Dateinamen bei
  cat("Normalisiere:", file, "->", output_file, "\n")
  normalize_raster(file, output_file)
}


