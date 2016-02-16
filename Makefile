all:
	jsonlint equajson-schema.json
	jsonschema equajson-schema.json
