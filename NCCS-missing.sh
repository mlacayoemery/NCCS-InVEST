for i in *.tif ; do cp "$i" "pollinator_abundance_${i,,}" ; done
for i in pollinator_abundance*.tif ; do mv "$i" "${i/./ }" ; done
for i in pollinator_abundance*.tif ; do mv "$i" "${i/_glo_ensemble/}" ; done

missing=("andrena bicolor")
for i in "${missing[@]}"; do cp "pollinator_abundance_andrena barbilabris.tif"  "pollinator_abundance_$i.tif"; done

sudo apt-get install exiv2
for i in pollinator_abundance*.tif ; do exiv2 pr "$i" | awk -F: '/Image size/ {print $2}' ; done
