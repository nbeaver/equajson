JSON=$(wildcard *.json)
TIMESTAMP=$(patsubst %.json, timestamps/%.timestamp,$(JSON))

timestamps : $(TIMESTAMP)

timestamps/%.timestamp : %.json
	python ../validate_equajson.py $< ../schema.json
	python ../ad-hoc-scripts/extract_validate_latex.py $<
	touch $@ # update the timestamp only if validation succeeds

clean:
	rm -f $(TIMESTAMP)
