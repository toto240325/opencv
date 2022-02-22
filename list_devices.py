import cv2
index = 0

arr = []
while True:
    print("testing index ",index)
    cap = cv2.VideoCapture(index)
    if not cap.read()[0]:
        break
    else:
        arr.append(index)
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        # Display the resulting frame
        cv2.imshow(f'frame {index}', frame)
        a = input("press a key")
    cap.release()
    index += 1
print(arr)
a = input("press a key")

