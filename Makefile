.PHONY: build-android

build-android:
	buildozer -v android debug

run:
	clear
	python3 main.py
