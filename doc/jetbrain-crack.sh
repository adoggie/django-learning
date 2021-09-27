rm ~/.config/JetBrains/*/eval/*
rm ~/.java/.userPrefs/jetbrains/*/*/evlsprt*/prefs.xml
for file in ~/.config/JetBrains/*/options/other.xml; do
grep -v evlsprt $file > ${file}_new
mv ${file}_new $file
done
