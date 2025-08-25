training = model.fit(X_train, y_train, batch_size=16, epochs=200)
#LOSS CURVE
fig = plt.figure(figsize=(8,8))
plt.plot(training.history['loss'][5:])
#plt.plot(training.history['val_loss'][5:])
plt.legend(['training loss','testing loss'])
plt.xlabel('number of Epochs')
plt.ylabel('Mean Squared error Loss')
plt.savefig('Loss_image')
plt.show()
#Final Output of CNN and after Local Threshold
