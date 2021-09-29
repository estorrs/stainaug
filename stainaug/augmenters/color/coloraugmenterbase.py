"""
This file contains base class for augmenting patches from whole slide images with color transformations.

Modified from https://github.com/DIAGNijmegen/pathology-he-auto-augment/he-randaugment/augmenters/color/coloraugmenterbase.py
"""

from stainaug.augmenters.augmenterbase import AugmenterBase

#----------------------------------------------------------------------------------------------------

class ColorAugmenterBase(AugmenterBase):
    """Base class for color patch augmentation."""

    def __init__(self, keyword):
        """
        Initialize the object.

        Args:
            keyword (str): Short name for the transformation.
        """

        # Initialize the base class.
        #
        super().__init__(keyword=keyword)
