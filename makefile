.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: run
run:
	streamlit run object_detection.py