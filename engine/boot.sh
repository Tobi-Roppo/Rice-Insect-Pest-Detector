kill -9 $(lsof -t -i:5000)
echo killed pre
python D:/Thesis/python-app-with-electron-gui/yolov5/detect.py &
cd ..
cd gui
npm start
kill -9 $(lsof -t -i:5000)
echo killed
