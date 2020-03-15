"""
Adapted from code in numpy.ipynb

Prints out information about training and testing images for machine learning
on data from boston_housing.

By: Emma Schroer on 03-15-20

"""
from tensorflow.keras.datasets import boston_housing


def print_structures():
    print(
        'training images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n\n'.format(
                len(train_images),
                train_images.ndim,
                train_images.shape,
                train_images.dtype
        ),
        'testing images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {} \n'.format(
                len(test_labels),
                train_labels.ndim,
                test_labels.shape,
                test_labels.dtype
        )
    )


(train_images, train_labels), (test_images, test_labels) = boston_housing.load_data()
print_structures()
