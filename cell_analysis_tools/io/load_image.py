import pathlib
from pathlib import Path
from typing import Union

import numpy as np
import tifffile

from .read_asc import read_asc


def load_image(path: Union[str, pathlib.PurePath]) -> np.ndarray:
    """
    Detects the extension and loads image into a numpy array 
    if it's a tif/tiff or an asc file.

    Parameters
    ----------
    path : pathlib path or str
        path to the image.

    Returns
    -------
    np.ndarray
        ndarray with the image data.

    """
    if not isinstance(path, pathlib.PurePath):
        path = Path(path)
    pass
    if path.suffix == ".asc":
        return read_asc(path)
    if path.suffix in [".tiff", ".tif"]:
        return tifffile.imread(path)
