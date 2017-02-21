from Datasource import Datasource
import numpy as np
import h5py

class HDF5(Datasource):
    pass
    @classmethod
    def load_tile(ds, query):
        path = query.OUTPUT.INFO.PATH.VALUE
        Z = query.index_xyz[-1]
        S,I,J = query.pixels_sij

        with h5py.File(path) as fd:
            volume = fd[fd.keys()[0]]
            return volume[Z, J[0]:J[1]:S, I[0]:I[1]:S]
