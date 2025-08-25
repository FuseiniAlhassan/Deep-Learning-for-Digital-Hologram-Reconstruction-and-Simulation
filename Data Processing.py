X_train_path = r"C:\Users\HP\Desktop\Reconstruction of Holograms\X_train_HOLO\Labels"
y_train_path = r"C:\Users\HP\Desktop\Reconstruction of Holograms\y_train_obj\objects"
X_train_list = os.listdir(path=X_train_path+'.')
y_train_list = os.listdir(path=y_train_path+'.')
X_train_list.sort()
y_train_list.sort()
print(X_train_list[1:10])
print(y_train_list[1:10])