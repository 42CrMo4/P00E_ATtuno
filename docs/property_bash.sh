DIR_PATH="."
FILE_PATTERN="project.properties"
for FILE in ${DIR_PATH}/${FILE_PATTERN}; do

	FILENAME=$(basename ${FILE})
	echo "Reading ${FILENAME}"

	OLD_IFS=$IFS; IFS=$'\n';
	while IFS="=" read -r PROP_KEY PROP_VALUE || [[ -n "$PROP_KEY" ]]; do

		echo "Prop Key:(${PROP_KEY}), (${PROP_VALUE})"
		echo "${PROP_KEY}, ${PROP_VALUE}" >> file.csv

	done < ${FILE}
	IFS=${OLD_IFS}

done
