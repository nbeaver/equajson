JSON=$(wildcard *.json)
TIMESTAMP=$(patsubst %.json, timestamps/%.timestamp,$(JSON))

all: timestamps $(TIMESTAMP)

timestamps:
	mkdir timestamps

timestamps/%.timestamp : %.json
	jsonlint $<
	../validate_equajson.py $< ../equajson-schema.json
	touch $@ # update the timestamp only if validation succeeds

clean:
	rm -f $(TIMESTAMP)
