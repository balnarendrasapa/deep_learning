.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: run
run:
	streamlit run streamlit_apps/object_detection_app.py