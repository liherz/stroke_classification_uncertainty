import numpy as np

# Generate synthetic input images which contain n_img successive images
def structure_data(X, Y, stroke, pat, path, img, n_img):
    X_new = np.zeros((0, X.shape[1], X.shape[2], n_img), dtype=np.float32)
    Y_new = []
    stroke_new = []
    pat_new = []
    path_new = []
    img_new = []
    
    # iterate over patients
    # get the images of the current patient and sort them
    for pid in np.unique(pat):
        idx = [ind for ind in range(len(pat)) if pat[ind] == pid]
        pat_images = img[idx]
        len_pat_images = len(pat_images)
        pat_images = np.unique(pat_images)
        pat_images = np.sort(pat_images)
        
        # find the index corresponding to the sorted images in the unique images!         
        cons_images = []
        idx = []
        for im in pat_images:
            for ind in range(len(img)):
                if im == img[ind] and im not in cons_images:
                    idx.append(ind)
                    # to ensure that the duplicated images are not contained within the idx, otherwise the same images would be repreated
                    cons_images.append(im)
                    
        # read in the data based on the sorted images
        X_tmp = np.zeros((len_pat_images-(n_img-1), X.shape[1], X.shape[2], n_img), dtype=np.float32)
        Y_tmp = np.zeros((len_pat_images-(n_img-1)), dtype=np.float32)
        stroke_tmp = np.zeros((len_pat_images-(n_img-1)), dtype=np.float32)
        pat_tmp = np.empty((len_pat_images-(n_img-1)), dtype=np.float32)
        path_tmp = np.empty((len_pat_images-(n_img-1)), dtype=np.object)
        img_tmp = np.empty((len_pat_images-(n_img-1)), dtype=np.object)
        j=0
        for i in range(len(pat_images)-(n_img-1)):
            for im in img:
                if im == pat_images[i]:
                    for k in range(n_img):
                        X_tmp[j,:,:,k] = X[idx[i+k],:,:,0]
                    Y_tmp[j] = Y[idx[i+int(n_img/2)]]
                    stroke_tmp[j] = stroke[idx[i+int(n_img/2)]]
                    pat_tmp[j] = pat[idx[i+int(n_img/2)]]
                    path_tmp[j] = path[idx[i+int(n_img/2)]]
                    img_tmp[j] = img[idx[i+int(n_img/2)]]
                    j += 1
        # Combine estimates of all patients
        # [:j]: to make sure that the img_tmp etc have the correct lenght
        X_new = np.concatenate((X_new, X_tmp[:j]), axis=0)
        Y_new = np.concatenate((Y_new, Y_tmp[:j]), axis=0)
        stroke_new = np.concatenate((stroke_new, stroke_tmp[:j]), axis=0)
        pat_new = np.concatenate((pat_new, pat_tmp[:j]), axis=0)
        path_new = np.concatenate((path_new, path_tmp[:j]), axis=0) # path to the image in the middle
        img_new = np.concatenate((img_new, img_tmp[:j]), axis=0)

    return(X_new, Y_new, stroke_new, pat_new, path_new, img_new)






