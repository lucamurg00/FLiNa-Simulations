import numpy as np
import matplotlib.pyplot as plt
import pathlib
import re

path =pathlib.Path(__file__).parent.resolve()
path = str(path.as_posix())+"/"
# folder = np.array(["Thermal_Conductivity_FLiNa14_200p/","Thermal_Conductivity_FLiNa55/","Thermal_Conductivity_FNa_200p/","Thermal_Conductivity_FLi/"])
folder = np.array(["Thermal_Conductivity_FLiNa14_200p_234/","Thermal_Conductivity_FLiNa55_234/","Thermal_Conductivity_FNa_200p_234/","Thermal_Conductivity_FLi_200p_234/"])

# Extracting temperature values
def MPout(filename= "profile.mp"):
    """Extract values from Lammps profile.mp file
    """
    path =pathlib.Path(__file__).parent.resolve()
    path = str(path.as_posix())+"/"
    File = open(path+filename, "r")
    array = []
    inner_array = []

    i = 0
    for line in File:

        li =list(re.split(r'[\s,]+|\n', line))
        if li[0]=="":
            # print(li)
            # print(li[1:5])
            # exit()
            li =li[1:5]
            li = np.array([float(i) for i in li])
            inner_array.append(li)
        
        else:
            #inner_array = np.array([float(i) for i in inner_array])
            inner_array = np.array(inner_array)
            # print(inner_array)
            
            array.append(inner_array)
            inner_array = []

    array = array[4:]
    array = np.array(array) 


    return array

def therm_out(filename= "profile.mp"):
    """Extract values from Lammps profile.mp file
    """
    path =pathlib.Path(__file__).parent.resolve()
    path = str(path.as_posix())+"/"
    File = open(path+filename, "r")
    array = []

    i = 0
    for line in File:

        li =list(re.split(r'[\s,]+|\n', line))
        if line.startswith("Running average thermal conductivity:"):
            # print(li)
            # print(li[4])
            # exit()
            # li =li[5]
            # li = np.array([float(i) for i in li])
            array.append(float(li[4]))
        

    return array[0]

li = []
def therm_plot(folder,ok = np.array([1,1,1,1,1,1])):
    sub_folder = (["1000K/","1100K/","1200K/","1300K/","1400K/","1500K/",])
    file1 = "profile.mp" 
    file2 = np.array(["therm_1000_job.out","therm_1100_job.out","therm_1200_job.out","therm_1300_job.out","therm_1400_job.out","therm_1500_job.out"])

    # Values of thermal conductivity as found from simulation:
    the = []
    st = []
    temp = []
    if ok[0] == 1:
        TC1000 = therm_out(folder+sub_folder[0]+file2[0])
        array0 = MPout(folder+sub_folder[0]+file1)
        tdiff0 =array0[:,10,3] - array0[:,0,3]
        u0 = TC1000 * np.mean(tdiff0[-50:])
        std0 = np.std(u0 /tdiff0[-50:], ddof = 1)
        the.append(TC1000)
        st.append(std0)
        temp.append(1000)

    if ok[1] == 1:
        TC1100 = therm_out(folder+sub_folder[1]+file2[1])
        array1 = MPout(folder+sub_folder[1]+file1)
        tdiff1 =array1[:,10,3] - array1[:,0,3]
        u1 = TC1100 * np.mean(tdiff1[-50:])
        std1 = np.std(u1 /tdiff1[-50:], ddof = 1)
        the.append(TC1100)
        st.append(std1)
        temp.append(1100)
        

    if ok[2] == 1:
        TC1200 = therm_out(folder+sub_folder[2]+file2[2])
        array2 = MPout(folder+sub_folder[2]+file1)
        tdiff2 =array2[:,10,3] - array2[:,0,3]
        u2 = TC1200 * np.mean(tdiff2[-50:])
        std2 = np.std(u2 /tdiff2[-50:], ddof = 1)
        the.append(TC1200)
        st.append(std2)
        temp.append(1200)

    if ok[3] == 1:
        TC1300 = therm_out(folder+sub_folder[3]+file2[3])
        array3 = MPout(folder+sub_folder[3]+file1)
        tdiff3 =array3[:,10,3] - array3[:,0,3]
        u3 = TC1300 * np.mean(tdiff3[-50:])
        std3 = np.std(u3 /tdiff3[-50:], ddof = 1)
        the.append(TC1300)
        st.append(std3)
        temp.append(1300)

    if ok[4] == 1:
        TC1400 = therm_out(folder+sub_folder[4]+file2[4])
        array4 = MPout(folder+sub_folder[4]+file1)
        tdiff4 =array4[:,10,3] - array4[:,0,3]
        u4 = TC1400 * np.mean(tdiff4[-50:])
        std4 = np.std(u4 /tdiff4[-50:], ddof = 1)
        the.append(TC1400)
        st.append(std4)
        temp.append(1400)

    if ok[5] == 1:
        TC1500 = therm_out(folder+sub_folder[5]+file2[5])
        array5 = MPout(folder+sub_folder[5]+file1)
        tdiff5 =array5[:,10,3] - array5[:,0,3]
        u5 = TC1500 * np.mean(tdiff5[-50:])
        std5 = np.std(u5 /tdiff5[-50:], ddof = 1)
        the.append(TC1500)
        st.append(std5)
        temp.append(1500)

    # print(st)
    # print(the)
    # exit()
    # array0 = MPout(folder+sub_folder[0]+file1)
    # array1 = MPout(folder+sub_folder[1]+file1)
    # array2 = MPout(folder+sub_folder[2]+file1)
    # array3 = MPout(folder+sub_folder[3]+file1)
    # array4 = MPout(folder+sub_folder[4]+file1)
    # array5 = MPout(folder+sub_folder[5]+file1)
    # print((150000- 100000)/1000)



    # tdiff0 =array0[:,10,3] - array0[:,0,3]
    # tdiff1 =array1[:,10,3] - array1[:,0,3]
    # tdiff2 =array2[:,10,3] - array2[:,0,3]
    # tdiff3 =array3[:,10,3] - array3[:,0,3]
    # tdiff4 =array4[:,10,3] - array4[:,0,3]
    # tdiff5 =array5[:,10,3] - array5[:,0,3]

    # u0 = TC1000 * np.mean(tdiff0[-50:])
    # u1 = TC1100 * np.mean(tdiff1[-50:])
    # u2 = TC1200 * np.mean(tdiff2[-50:])
    # u3 = TC1300 * np.mean(tdiff3[-50:])
    # u4 = TC1400 * np.mean(tdiff4[-50:])
    # u5 = TC1500 * np.mean(tdiff5[-50:])

    # std0 = np.std(u0 /tdiff0[-50:], ddof = 1)
    # std1 = np.std(u1 /tdiff1[-50:], ddof = 1)
    # std2 = np.std(u2 /tdiff2[-50:], ddof = 1)
    # std3 = np.std(u3 /tdiff3[-50:], ddof = 1)
    # std4 = np.std(u4 /tdiff4[-50:], ddof = 1)
    # std5 = np.std(u5 /tdiff5[-50:], ddof = 1)

    # print(std0)
    # print(std1)
    # print(std2)
    # print(std3)
    # print(std4)
    # print(std5)

    # print("\n")

    # Unit Transformation:
    Thermal_Cond = np.array(the)
    Thermal_Cond =Thermal_Cond[:,np.newaxis]
    STD = np.array(st)
    STD =STD[:,np.newaxis]


    def Transform(Thermal_Cond):
        kb = 8.617333262*10**-5 # Ev/(m*K)
        joules = 6.241509074461E+18 # eV
        second = 1e+12 # picseconds
        meter = 1e+10 # angstrom
        #Thermal_Cond =    # eV/(s*angstrom*K)
        Thermal_Cond = Thermal_Cond * meter  # eV/(fetmosecond*m*K)
        Thermal_Cond = Thermal_Cond * kb # correction
        Thermal_Cond = Thermal_Cond * second # eV/(s*m*K)
        Thermal_Cond = Thermal_Cond / joules # eV/(s*m*K)
        #print("FLiNa 4-1 Thermal Conductivity:",np.round(Thermal_Cond,6), "W/mK")
        return Thermal_Cond
    therm =np.ndarray.flatten(Transform(Thermal_Cond))
    std =np.ndarray.flatten(Transform(STD))
    temp = np.array(temp)



    # Experimental Data based off of : THERMAL CONDUCTIVITY OF MOLTEN ALKALI HALIDES AND THEIR MIXTURES
    #   LiF-NaF
    #   .8 -.2 <-- ratio



    def y(y0, b, T):
        return y0+b*T


    temp_exp =np.linspace(1130,1260,4)
    therm_exp = y(-1.05, 20.3e-4, temp_exp)
    std_exp = temp_exp*0 +.016
    # Plotting:
    path =pathlib.Path(__file__).parent.resolve()
    path = str(path.as_posix())+"/"
    li.append(temp)
    li.append(therm)
    li.append(std)




    plt.errorbar(temp,therm, std, linestyle='None', color='red', marker="o")
    # plt.errorbar(temp_exp,therm_exp,std_exp, linestyle='None', marker='^',color="green")
    # plt.xticks(x, time)
    plt.legend(["Simulation","Experimental"])
    plt.xlabel("Temperature (K)")
    plt.ylabel(r"Thermal Conductivity ($\frac{W}{mK}$)")
    plt.xlim(900, 1600)  # Sets the x-axis limits from 0 to 6
    plt.ylim(.6, 2.1) 
    # plt.savefig(folder + 'Thermal_Cond_FLiNa_4_1.png')
    # plt.savefig(folder + folder[:-1]+'.svg')
    plt.savefig(folder + folder[:-1]+'.pdf', format="pdf")
    # plt.show()
    plt.close()

therm_plot(folder[0], np.array([1,1,1,1,1,1]))
therm_plot(folder[1], np.array([1,1,1,1,1,1]))
therm_plot(folder[2], np.array([1,1,1,1,1,1]))
therm_plot(folder[3], np.array([0,0,1,1,1,1]))
# therm_plot(folder[3],np.array([1,1,1,1,1,1]))


print(li[-3:])
exit()
my_array = np.array(li)

print(my_array[-1])
exit()
delimiter = ','

# Save the array to the CSV file at the specified path
np.savetxt(path + 'my_array.csv', my_array, delimiter=delimiter)

import numpy as np
import matplotlib.pyplot as plt
import pathlib
import re

# Path and file:
path =pathlib.Path(__file__).parent.resolve()
path = str(path.as_posix())+"/"
name = "my_array.csv"
dat = np.genfromtxt( path + name, delimiter=',')

# Experimental Data based off of : THERMAL CONDUCTIVITY OF MOLTEN ALKALI HALIDES AND THEIR MIXTURES
def y(y0, b, T):
    return y0+b*T

#-------------------------------------------------------
#   LiF-NaF: .8 -.2 <-- ratio
temp_exp14 =np.linspace(1130,1260,4)
therm_exp14 = y(-1.05, 20.3e-4, temp_exp14)
std_exp14 = temp_exp14*0 +.016
#-------------------------------------------------------
#   LiF-NaF: .8 -.2 <-- ratio
temp_exp55 =np.linspace(1130,1260,4)
therm_exp55 = y(-1.07, 18.95e-4, temp_exp55)
std_exp55 = temp_exp55*0 +.011
#-------------------------------------------------------
#   LiF-NaF: .8 -.2 <-- ratio
temp_exp01 =np.linspace(1130,1260,4)
therm_exp01 = y(-0.89, 15.7e-4, temp_exp01)
std_exp01 = temp_exp01*0 +.01
#-------------------------------------------------------
# Calculate the linear line using the equation
s1, b1 = np.polyfit(dat[0], dat[1], 1)
s2, b2 = np.polyfit(dat[3], dat[4], 1)
s3, b3 = np.polyfit(dat[6], dat[7], 1)
l1 = [s1 * xi + b1 for xi in dat[0]]
l2 = [s2 * xi + b2 for xi in dat[3]]
l3 = [s3 * xi + b3 for xi in dat[6]]

slope_dft = np.array([s1,s2, s3])
points_dft = np.array([.2, .5, 1])
slope_exp = np.array([21.0,20.3, 19.2, 18.7, 17.2, 16.0])*1e-4
points_exp = np.array([0,.2, .4, .6, .8, 1]) 

# print(slope_exp)
# print(slope_dft)
# exit()
# plt.plot(points_exp,slope_exp)
# # plt.xlim(0, 1)  # Sets the x-axis limits from 0 to 6
# # # plt.ylim(.6, 2.1) 

# plt.plot(points_dft,slope_dft)
# plt.show()
# plt.xlim(0, 1)  # Sets the x-axis limits from 0 to 6
# plt.show()
# exit()
xx = np.array([1150,1300, 1450])
yy = np.array([1.233, 1.165, 1.089])
colors = ['C9','C2','C5'] #['#008B8B', '#9932CC', '#2F4F4F']#['#191970', '#4B0082', '#556B2F']#['#40E0D0', '#DA70D6', '#708090']
plt.errorbar(dat[0],dat[1], dat[2], linestyle='none',color=colors[0], marker="^", markeredgecolor = colors[0], markerfacecolor='none', elinewidth=1, capsize=5)
plt.errorbar(dat[3],dat[4], dat[5], linestyle='none',color=colors[1], marker="o", markeredgecolor = colors[1], markerfacecolor='none', elinewidth=1, capsize=5)
plt.errorbar(dat[6],dat[7], dat[8], linestyle='none',color=colors[2], marker="X", markeredgecolor = colors[2], markerfacecolor='none', elinewidth=1, capsize=5)
plt.plot(dat[0],l1,linestyle='-.', color = colors[0])
plt.plot(dat[3],l2,linestyle='--' , color = colors[1])
plt.plot(dat[6],l3,linestyle='-', color = colors[2])
plt.plot(xx,yy)
# plt.plot(1300,1.138, marker="^")
# plt.plot(1300,1.430, marker="^")
plt.set_cmap('cividis')
# plt.errorbar(temp_exp14,therm_exp14,std_exp14, linestyle='None', marker='^',color="green")
# plt.errorbar(temp_exp55,therm_exp55,std_exp55, linestyle='None', marker='^',color="orange")
# plt.errorbar(temp_exp01,therm_exp01,std_exp01, linestyle='None', marker='^',color="purple")
plt.legend(["LiF-NaF: 4-1","LiF-NaF: 1-1","LiF-NaF: 0-1"], frameon=True)
plt.xlabel("T (K)")
plt.ylabel(r"$\lambda$ ($W/mK$)")
# plt.savefig(path + 'Thermal_Cond_FLiNa_4_1.png')
# plt.savefig(path + 'Thermal_Cond_FLiNa_4_1.svg')
plt.savefig(path + 'Thermal_Cond_FLiNa_4_1.pdf', format='pdf')

