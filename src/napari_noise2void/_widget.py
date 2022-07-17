from napari_tools_menu import register_function
from napari_time_slicer import time_slicer

@register_function(menu="Filtering / noise removal > Train noise2void denoiser")
def train_noise2void(training_image: "napari.types.ImageData",
                     validation_image: "napari.types.ImageData",
                     number_training_epochs: int = 20,
                     train_batch_size: int = 4,
                     n2v_perc_pix=0.198,
                     model_filename: str = "my_model_n2v",
                     model_description: str = "none",
                     model_authors: str = "unknown"
                    ) -> "napari.types.ImageData":
    """

    Parameters
    ----------
    training_image
    validation_image
    model_filename

    Returns
    -------

    See Also
    --------
    ..[0] https://github.com/juglab/n2v/blob/master/examples/2D/denoising2D_SEM/01_training.ipynb
    ..[1] https://github.com/juglab/n2v/blob/master/examples/3D/01_training.ipynb
    """
    print(f"you have selected {training_image.shape}")
    from n2v.models import N2VConfig, N2V
    from n2v.internals.N2V_DataGenerator import N2V_DataGenerator
    import numpy as np


    datagen = N2V_DataGenerator()
    if len(training_image.shape) == 2:
        patch_shape = (64, 64)
        axes = 'YXC'
    elif len(training_image.shape) == 3:
        patch_shape = (32, 64, 64)
        axes = 'ZYXC'
    else:
        raise ValueError("Only 2D and 3D data supported.")

    data = np.asarray([training_image[..., np.newaxis]])
    data.shape
    print("data shope", data.shape)

    X = datagen.generate_patches(data, shape=patch_shape)
    X_val = datagen.generate_patches(np.asarray([validation_image[...,np.newaxis]]), shape=patch_shape)

    config = N2VConfig(X, unet_kern_size=3,
                       train_steps_per_epoch=int(X.shape[0] / 128),
                       train_epochs=number_training_epochs,
                       train_loss='mse',
                       batch_norm=True,
                       train_batch_size=train_batch_size,
                       n2v_perc_pix=n2v_perc_pix,
                       n2v_patch_shape=patch_shape,
                       n2v_manipulator='uniform_withCP',
                       n2v_neighborhood_radius=5)

    # the base directory in which our model will live
    basedir = 'models'
    # We are now creating our network model.
    model = N2V(config, model_filename, basedir=basedir)

    # We are ready to start training now.
    history = model.train(X, X_val)

    model.export_TF(name=model_filename,
                    description=model_description,
                    authors=model_authors.split(","),
                    test_img=X_val[0, ..., 0], axes=axes,
                    patch_shape=patch_shape)

    return apply_noise2void(training_image, model_filename=model_filename)

@register_function(menu="Filtering / noise removal > Apply noise2void denoiser")
@time_slicer
def apply_noise2void(image: "napari.types.ImageData",
                       model_filename: str = "my_model_n2v",
                       number_of_tiles: int = 4,
                      ) -> "napari.types.ImageData":
    """

    Parameters
    ----------
    image
    model_filename

    Returns
    -------

    See Also
    --------
    ..[0] https://github.com/juglab/n2v/blob/master/examples/3D/02_prediction.ipynb
    ..[1] https://github.com/juglab/n2v/blob/master/examples/2D/denoising2D_SEM/02_prediction.ipynb
    """
    if len(model_filename) == 0:
        raise Exception("No model chosen")

    from n2v.models import N2V
    import numpy as np

    basedir = 'models'
    model = N2V(config=None, name=model_filename, basedir=basedir)
    if len(image.shape) == 2:
        axes = "YXC"
        tiles = (number_of_tiles, number_of_tiles, 1)
    elif len(image.shape) == 3:
        axes = "ZYXC"
        tiles = (number_of_tiles, number_of_tiles, number_of_tiles, 1)
    else:
        raise ValueError("Only 2D and 3D data supported.")

    predicted_image = model.predict(image[..., np.newaxis], axes=axes, n_tiles=tiles)
    return predicted_image[..., 0]
