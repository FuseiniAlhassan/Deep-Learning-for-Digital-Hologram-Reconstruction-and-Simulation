# Path to my zip file
zip_file_path = r"C:\Users\HP\Desktop\archive.zip"

# Create temporary directory to extract files if needed
temp_dir = "temp_extracted_files"
os.makedirs(temp_dir, exist_ok=True)

X_train = np.zeros((1,64,64,1))
y_train = np.zeros((1,64,64,1))
i = 0

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(temp_dir)
    
X_train_path = os.path.join(temp_dir, "X_train_HOLO", "Labels", "")
y_train_path = os.path.join(temp_dir, "y_train_obj", "objects", "")

# Define the file lists before using them in the loop
X_train_list = os.listdir(X_train_path)
y_train_list = os.listdir(y_train_path)

for a, b in zip(X_train_list, y_train_list):
    if i % 100 == 0:
        print(i, end=" ")
    i += 1
    imx = load_img(path=X_train_path+a, color_mode='grayscale')
    imy = load_img(path=y_train_path+b, color_mode='grayscale')
    imx = np.asarray(imx).reshape(1,64,64,1)
    imy = np.asarray(imy).reshape(1,64,64,1)
    X_train = np.concatenate((X_train, imx), axis=0)
    y_train = np.concatenate((y_train, imy), axis=0)
    X_train = X_train[1:]#/255.
y_train = y_train[1:]#/255.