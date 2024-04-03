from sage.structure.sage_object import SageObject
import numpy as np

class ComponentNumpy(SageObject):
    def __init__(self, ring, frame, nb_indices, start_index=0,
                 output_formatter=None):        
        self._ring = ring
        self._frame = frame
        self._nid = nb_indices
        self._dim = len(frame)
        self._sindex = start_index
        self._output_formatter = output_formatter
        self._comp = np.zeros([self._dim] * nb_indices)

    def _repr_(self):
        prefix, suffix = self._repr_symmetry()
        description = prefix
        description += str(self._nid)
        if self._nid == 1:
            description += "-index"
        else:
            description += "-indices"
        description += " components w.r.t. " + str(self._frame)
        description += suffix
        return description

    def _repr_symmetry(self):
        return "", ""

    def _new_instance(self):
        return ComponentNumpy(self._ring, self._frame, self._nid, self._sindex,
                          self._output_formatter)

    def copy(self):
        result = self._new_instance()
        for ind, val in self._comp.items():
            if isinstance(val, SageObject) and hasattr(val, 'copy'):
                result._comp[ind] = val.copy()
            else:
                result._comp[ind] = val
        return result

    def _del_zeros(self):
        zeros = []
        for ind, value in self._comp.items():
            if value == 0:
                zeros.append(ind)
        for ind in zeros:
            del self._comp[ind]

    def __getitem__(self, args):
        pass

    def __getlist__(self, ind_slice, no_format=True, format_type=None):
        pass

    def __mul__(self, other):
        return np.multiply(self, other)
    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test    
#test