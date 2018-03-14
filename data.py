from enum import Enum


class InputData:
    BENIGN = 2
    MALIGNANT = 4

    def __init__(self):
        self.id = None  # type: int
        self.clump_thickness = None  # type: int
        self.uniformity_of_cell_size = None  # type: int
        self.uniformity_of_cell_shape = None  # type: int
        self.marginal_adhesion = None  # type: int
        self.single_epithelial_cell_size = None  # type: int
        self.bare_nuclei = None  # type: int
        self.bland_chromatin = None  # type: int
        self.normal_nucleoli = None  # type: int
        self.mitoses = None  # type: int
        self.type = None  # type: int

    def read(filename):
        arr = []  # type: list[InputData]

        with open(filename) as input:
            for line in input:
                values = line.split(',')
                if values[6] != '?':
                    data = InputData()
                    data.id = int(values[0])
                    data.clump_thickness = int(values[1])
                    data.uniformity_of_cell_size = int(values[2])
                    data.uniformity_of_cell_shape = int(values[3])
                    data.marginal_adhesion = int(values[4])
                    data.single_epithelial_cell_size = int(values[5])
                    data.bare_nuclei = int(values[6])
                    data.bland_chromatin = int(values[7])
                    data.normal_nucleoli = int(values[8])
                    data.mitoses = int(values[9])
                    data.type = int(values[10])
                    arr.append(data)
        return arr

    def get_value(self, type):
        if type == InputType.CLUMP_THICKNESS:
            return self.clump_thickness
        if type == InputType.UNIFORMITY_OF_CELL_SIZE:
            return self.uniformity_of_cell_size
        if type == InputType.UNIFORMITY_OF_CELL_SHAPE:
            return self.uniformity_of_cell_shape
        if type == InputType.MARGINAL_ADHESION:
            return self.marginal_adhesion
        if type == InputType.SINGLE_EPITHELIAL_CELL_SIZE:
            return self.single_epithelial_cell_size
        if type == InputType.BARE_NUCLEI:
            return self.bare_nuclei
        if type == InputType.BLAND_CHROMATIN:
            return self.bland_chromatin
        if type == InputType.NORMAL_NUCLEOLI:
            return self.normal_nucleoli
        if type == InputType.MITOSES:
            return self.mitoses
        return None


class InputType(Enum):
    CLUMP_THICKNESS = "clump_thickness"
    UNIFORMITY_OF_CELL_SIZE = "uniformity_of_cell_size"
    UNIFORMITY_OF_CELL_SHAPE = "uniformity_of_cell_shape"
    MARGINAL_ADHESION = "marginal_adhesion"
    SINGLE_EPITHELIAL_CELL_SIZE = "single_epithelial_cell_size"
    BARE_NUCLEI = "bare_nuclei"
    BLAND_CHROMATIN = "bland_chromatin"
    NORMAL_NUCLEOLI = "normal_nucleoli"
    MITOSES = "mitoses"
