# napari-noise2void

[![License BSD-3](https://img.shields.io/pypi/l/napari-noise2void.svg?color=green)](https://github.com/haesleinhuepf/napari-noise2void/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-noise2void.svg?color=green)](https://pypi.org/project/napari-noise2void)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-noise2void.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/napari-noise2void/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-noise2void/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/napari-noise2void/branch/main/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/napari-noise2void)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-noise2void)](https://napari-hub.org/plugins/napari-noise2void)

Image denoising using n2v as described in [Krull et al. 2019](https://arxiv.org/abs/1811.10980) and available as [python library n2v](https://github.com/juglab/n2v).
This napari plugins has been derived from example notebooks published [here](https://github.com/juglab/n2v/tree/master/examples) ([licensed BSD](licenses_thirdparty/license.txt)).

## Usage

* Load two example images, ideally acquired under the same conditions, for example [electron microscopy images provided by the n2v maintainers](https://download.fht.org/jug/n2v/SEM.zip).
* Start the plugin from the `Tools > Filtering / noise removal > Train noise2void denoiser` and enter the two images.

![img.png](https://github.com/haesleinhuepf/napari-noise2void/raw/main/docs/screenshot1.png)

* After clicking on `Run`, you can follow the progress in the terminal window in the background. This will take a while.

![img.png](https://github.com/haesleinhuepf/napari-noise2void/raw/main/docs/screenshot2.png)

* After the model has been trained, the result computed on the training image will be shown. 

![img.png](https://github.com/haesleinhuepf/napari-noise2void/raw/main/docs/screenshot3.png)

* You can reuse the model, e.g. by running the plugin `Tools > Filtering / noise removal > Apply noise2void denoiser` and entering its name in the text field.
* Consider increasing the number of tiles in case your images are large.

In this example, it was reused to also denoise the validation image.

![img.png](https://github.com/haesleinhuepf/napari-noise2void/raw/main/docs/screenshot4.png)

* Consider using [napari-curtain](https://www.napari-hub.org/plugins/napari-curtain) from the menu `Tools > Visualization > Curtain` to blend between the original image and the denoised image.

![img.png](https://github.com/haesleinhuepf/napari-noise2void/raw/main/docs/screenshot6.png)

The models are saved to the `models` folder in the directory where napari was started from. 
If you just started napari from the command line, this should be a subfolder of your home directory.

![img.png](https://github.com/haesleinhuepf/napari-noise2void/raw/main/docs/screenshot5.png)

Also consider training denoising models using the [example notebooks of n2v](https://github.com/juglab/n2v/tree/master/examples). 
By training models from multiple images using those notebooks, the resulting models should be more robust and reliable.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

## Installation

You can install `napari-noise2void` via [pip]:

    pip install napari-noise2void


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-noise2void" is free and open source software

## Support

If you encounter any problems, please create a thread on [image.sc] along with a detailed description and tag [@haesleinhuepf].

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/haesleinhuepf/napari-noise2void/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[image.sc]: https://image.sc
[@haesleinhuepf]: https://twitter.com/haesleinhuepf
