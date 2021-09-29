![example augmentation](https://github.com/estorrs/stainaug/blob/master/images/example.png)

A lightweight wrapper for image normalization implemented by [DIAGNijmegen](https://github.com/DIAGNijmegen/pathology-he-auto-augment), which used deconvolution based methods from [Faryna et al.](https://2021.midl.io/proceedings/faryna21.pdf) and [Tellez et al.](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/10581/2293048/HE-stain-augmentation-improves-generalization-of-convolutional-networks-for-histopathological/10.1117/12.2293048.full?SSO=1).

#### Installation

```bash
pip install stainaug
```

#### Basic Usage

```python
import PIL.Image as Image
import numpy as np

from stainaug.augment import Augmentor

# read in image
image_filepath = </path/to/image.jpeg>
img = np.asarray(Image.open(image_filepath))

# initialize augmentor
augmentor = Augmentor()

# transform image
augmented_img = augmentor.augment_HE(img)
```

#### Examples

For more examples see notebook [here](https://github.com/estorrs/stainaug/blob/master/examples/example.ipynb)

