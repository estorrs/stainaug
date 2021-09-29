import numpy as np

from stainaug.augmenters.color.hedcoloraugmenter import HedColorAugmenter


def get_he_augmentor(factor):
    return HedColorAugmenter(
        haematoxylin_sigma_range=(-factor, factor),
        haematoxylin_bias_range=(-factor, factor),
        eosin_sigma_range=(-factor, factor),
        eosin_bias_range=(-factor, factor),
        dab_sigma_range=(-factor, factor),
        dab_bias_range=(-factor, factor),
        cutoff_range=(0.15, 0.85)
    )


class Augmentor(object):
    def __init__(self, factor=.1):
        """
        Augmentor for H&E images.

        Parameters
        ----------
        factor: float
            - Controls aggressivness of the transformation. See
              https://github.com/DIAGNijmegen/pathology-he-auto-augment
              for more details.
        """
        self.he_augmentor = get_he_augmentor(factor)

    def augment_HE(self, img):
        """
        Augment H&E image.

        Parameters
        ----------
        img: np.ndarray
            - numpy array to be transformed. Array should be of shape
              (height, width, channels) where channels = 3.
        """
        # transform expects shape of (c, h, w)
        img = np.transpose(img, [2, 0, 1])

        self.he_augmentor.randomize()
        return np.transpose(self.he_augmentor.transform(img), [1, 2, 0])
