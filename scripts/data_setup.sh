SERVER_URL=https://demo.borealisdata.ca
PERSISTENT_ID=doi:10.80240/FK2/IFEI6R

FILE_NAME=data/raw/sub-nyuMouse11_sample-0006_TEM.png
FILE_ID=74037
curl -fL -o "$FILE_NAME" "$SERVER_URL/api/access/datafile/$FILE_ID"