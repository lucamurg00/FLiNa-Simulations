import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange
import pathlib
from time import perf_counter
import re
import pyperclip as pc
import sys

# Box Length Calcualtion:
density = 3.1000838321211277 # grams/cm^3
# ratio =np.array([1,0,1]) # FNa 
ratio =np.array([1,1,0]) # FLi 

# Path:
filename = "FLi_1000_100_startpoint.lammps"
path =pathlib.Path(__file__).parent.resolve()
path = str(path.as_posix())+"/"

# Assumed Information:
# atom_1 = "F"
# atom_2 = "Li"
# atom_3 = "Na"
molar_mass =np.array([18.998, 6.9410, 22.990]) # must be in order which atoms appear above
avogadro = 6.023e23 # = 1 mole
x = 1

# Functions:
def Conout(filename= "CONTCAR", lbox =1):

    path =pathlib.Path(__file__).parent.resolve()
    path = str(path.as_posix())+"/"
    File = open(path+filename, "r")


    lattice_vector = []

    coords_complete = False
    direct_coords = []
    i = 0
    for line in File:
        if i == 2 or i == 3 or i == 4:
            li =list(re.split(r'[\s,]+|\n', line))            
            li =li[1:4]
            li = np.array([float(i) for i in li])
            lattice_vector.append(li)

        #-----------------------------------------
        li =list(re.split(r'[\s,]+|\n', line))
        if len(li) ==2 and li[0]=="" or line.startswith("Lattice velocities"):
            coords_complete = True
        if i >= 8 and coords_complete == False:
            li =li[1:4]
            li = np.array([float(i) for i in li])
            direct_coords.append(li)

        i += 1

    lattice_vector = np.array(lattice_vector) 
    direct_coords = np.array(direct_coords)

    return lattice_vector, direct_coords

def LampOut(atom_coords, x, y, z, Charges = False, System = 1):
    if System == 1: # Lammps
        atom_coords[:,0] *=x
        atom_coords[:,1] *=y
        atom_coords[:,2] *=z
        atom_num = len(atom_coords)

        # Items needed to create Lammps input file
        # Order of items in list
        order = np.arange(1,atom_num+1)
        order =order[:,np.newaxis]

        # Atom Ids
        a = ratio*atom_num/np.sum(ratio)
        atom_id = np.array([])
        for i in range(ratio.shape[0]):
            atom_id = np.append(atom_id, np.repeat(i+1,a[i]))
        #np.random.shuffle(atom_id)
        atom_id =atom_id[:,np.newaxis]
        atom_coords = np.round(atom_coords,3)

        if Charges:
            atom_coords =np.append(atom_id*0+1,atom_coords,axis =1)# Charges

        atom_coords =np.append(atom_id,atom_coords,axis =1)# Atom Id
        atom_coords =np.append(order,atom_coords,axis =1)# Order



        # Changing Coordinates to String
        str_coords = np.array2string(atom_coords)
        str_coords = str_coords.replace( "[", "")
        str_coords = str_coords.replace( "]", "")
        str_coords = str_coords.replace( ". ", "")
        str_coords = str_coords.replace( "    ", " ")
        str_coords = str_coords.replace( "   ", " ")
        str_coords = str_coords.replace( "  ", " ")
        str_coords = str_coords.replace( "\n    ", "\n")
        str_coords = str_coords.replace( "\n   ", "\n")
        str_coords = str_coords.replace( "\n  ", "\n")
        str_coords = str_coords.replace( "\n ", "\n")


        # Copying String to clipboard:    
        return str_coords

# Reading CONTCAR:
lat, atom_coords = Conout()


atom_number = atom_coords.shape[0]

#Calculation:
num_atoms = ratio*atom_number/np.sum(ratio)
print("Number of Each Atom:", num_atoms)
moles = num_atoms/avogadro
mass = moles*molar_mass
print("Individual Mass:",mass)
total_mass = np.sum(mass)
print("Total Mass:",total_mass)
volume_cm = total_mass/density
print("Volume in cm:",volume_cm)
volume_a = volume_cm*(1e8)**3
print("Volume in Angstrom:",volume_a)
box_length =(volume_a)**(1/3)
print("box_length in angstom:",box_length)

# Creating Lammps File:
x1 = box_length
y1 = box_length
z1 = box_length
Charges = False
System = 1 # Vasp == 0, Lammps == 1
coords = LampOut(atom_coords, x1, y1, z1, Charges = False, System = 1)
coords =coords[1:]

# Strings in File
name_str = "FLiNa to FNa ratio: " + str(x) + "\n\n"
atom_num_str = str(atom_number) + " atoms \n"
angle_str = "0  bonds\n0  angles0  dihedrals\n0  impropers\n\n"
atom_types_str = str(len(ratio)) + " atom type\n"
angle_types_str = "0  bond types\n0  angle types\n0  dihedral types\n0  improper types\n\n"
box_str = "0.0 " + str(x1) + " xlo xhi\n" + "0.0 " + str(y1) + " ylo yhi\n" + "0.0 " + str(z1) + " zlo zhi\n\n"
mass_str = "Masses\n\n" + "1 " + str(molar_mass[0]) + "\n" + "2 " + str(molar_mass[1]) + "\n" + "2 " + str(molar_mass[2]) + "\n\n"
atom_str = "Atoms\n\n"

np.set_printoptions(threshold=sys.maxsize) # Shows full array
np.set_printoptions(suppress=True) # Supresses Scientif notation
coords = LampOut(atom_coords, x1, y1, z1, Charges = False, System = 1)
coords =coords[1:]

text = name_str + atom_num_str + angle_str + atom_types_str + angle_types_str + box_str + mass_str + atom_str + coords
print(coords)


# File = open(path+"Ayo.txt", "w")
outFile = open(path + filename, "w")
outFile.writelines(text)
