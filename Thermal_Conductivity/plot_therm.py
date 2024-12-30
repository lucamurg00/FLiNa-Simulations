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


# Experimental Data based off of : THERMAL CONDUCTIVITY OF MOLTEN ALKALI HALIDES AND THEIR MIXTURES
def y(y0, b, T):
    return y0+b*T


def therm_exp_r0(temp):
    return y(-.99, 21.0e-4, temp)

def therm_exp_r2(temp):
    return y(-1.05, 20.3e-4, temp)

def therm_exp_r4(temp):
    return y(-1.05, 19.2e-4, temp)

def therm_exp_r6(temp):
    return y(-1.09, 18.7e-4, temp)

def therm_exp_r8(temp):
    return y(-.99, 17.2e-4, temp)

def therm_exp_r1(temp):
    return y(-.88, 16.0e-4, temp)

temp_r0 = np.linspace(1130,1240,100)
temp_r2 = np.linspace(1130,1260,100)
temp_r4 = np.linspace(1160,1265,100)
temp_r6 = np.linspace(1125,1250,100)
temp_r8 = np.linspace(1215,1305,100)
temp_r1 = np.linspace(1260,1350,100)
#-------------------------------------------------------
# Calculate the linear line using the equation
s1, b1 = np.polyfit(li[0], li[1], 1)
s2, b2 = np.polyfit(li[3], li[4], 1)
s3, b3 = np.polyfit(li[6][3:], li[7][3:], 1)
s4, b4 = np.polyfit(li[9], li[10], 1)
l1 = [s1 * xi + b1 for xi in li[0]]
l2 = [s2 * xi + b2 for xi in li[3]]
l3 = [s3 * xi + b3 for xi in li[6]]
l4 = [s4 * xi + b4 for xi in li[9]]


import matplotlib.colors as mcolors

# Define dodger blue and light blue
dodgerblue_dark = 'dodgerblue'
dodgerblue_light = 'yellowgreen'

color_dark = mcolors.to_rgba(dodgerblue_dark)
color_light = mcolors.to_rgba(dodgerblue_light)

num_variations = 6
colors_rgba = [tuple(np.linspace(color_dark[i], color_light[i], num_variations)) for i in range(4)]
d_blue = [mcolors.to_hex(color) for color in zip(*colors_rgba)]

# Define dodger blue and light blue
dodgerblue_dark = 'maroon'
dodgerblue_light = 'gold'

color_dark = mcolors.to_rgba(dodgerblue_dark)
color_light = mcolors.to_rgba(dodgerblue_light)

num_variations = 6
colors_rgba = [tuple(np.linspace(color_dark[i], color_light[i], num_variations)) for i in range(4)]
d_gold = [mcolors.to_hex(color) for color in zip(*colors_rgba)]


plt.clf()
colors = np.array(["gold","dodgerblue",'yellowgreen','maroon', 'red','blue','green','orange','black', 'purple'])
# plt.errorbar(li[9],li[10], li[11], linestyle='none',color=d_blue[3], marker="h", markeredgecolor = d_blue[3], markerfacecolor='none', elinewidth=1, capsize=5)
# plt.errorbar(li[0],li[1], li[2], linestyle='none',color= d_blue[2],  marker="^", markeredgecolor = d_blue[2], markerfacecolor='none', elinewidth=1, capsize=5)
# plt.errorbar(li[3],li[4], li[5], linestyle='none',color= d_blue[1],  marker="o", markeredgecolor = d_blue[1], markerfacecolor='none', elinewidth=1, capsize=5)
# plt.errorbar(li[6][3:],li[7][3:], li[8][3:], linestyle='none',color= d_blue[0],  marker="X", markeredgecolor = d_blue[0], markerfacecolor='none', elinewidth=1, capsize=5)

# plt.plot(temp_r0, therm_exp_r0(temp_r0),linestyle='-', color = d_gold[5])
# plt.plot(temp_r2, therm_exp_r2(temp_r2),linestyle=':', color = d_gold[4])
# plt.plot(temp_r4, therm_exp_r4(temp_r4),linestyle='--', color = d_gold[3])
# plt.plot(temp_r6, therm_exp_r6(temp_r6),linestyle='-.', color = d_gold[2])
# plt.plot(temp_r8, therm_exp_r8(temp_r8),linestyle='-', color = d_gold[1])
# plt.plot(temp_r1, therm_exp_r1(temp_r1),linestyle=':', color = d_gold[0])

# # plt.legend(["LiF-NaF: 1-0","LiF-NaF: 4-1","LiF-NaF: 1-1","LiF-NaF: 0-1", "Exp: LiF-NaF: 1-0", "Exp: LiF-NaF: 4-1", "Exp: LiF-NaF: 3-2", "Exp: LiF-NaF: 2-3", "Exp: LiF-NaF: 1-4", "Exp: LiF-NaF: 0-1"],loc='upper left',fontsize='xx-small', frameon=True)
# plt.legend(["Exp: LiF-NaF: 1-0", "Exp: LiF-NaF: 4-1", "Exp: LiF-NaF: 3-2", "Exp: LiF-NaF: 2-3", "Exp: LiF-NaF: 1-4", "Exp: LiF-NaF: 0-1","LiF-NaF: 1-0","LiF-NaF: 4-1","LiF-NaF: 1-1","LiF-NaF: 0-1",],loc='upper left',fontsize='xx-small', frameon=True)



# plt.plot(li[9],l4,linestyle='-', color = d_blue[3])
# plt.plot(li[0],l1,linestyle=':', color = d_blue[2])
# plt.plot(li[3],l2,linestyle='--', color = d_blue[1])
# plt.plot(li[6][3:],l3[3:],linestyle='-.', color = d_blue[0])

# plt.xlabel("$T$ (K)")
# plt.ylim(.85, 1.75)
# plt.ylabel(r"$\lambda$ (Wm$^{-1}$K$^{-1}$)")
# # plt.ylim(.8, 1.8)
# # plt.xlim(950, 1550)
# plt.savefig(path + 'Thermal.pdf', format='pdf')
# plt.show()
# plt.clf()

fig, ax = plt.subplots(1, 1, figsize=(6, 6), sharex=True)

ax.errorbar(li[9], li[10], li[11], linestyle='none', color=d_blue[3], marker="h", markeredgecolor=d_blue[3], markerfacecolor='none', elinewidth=1, capsize=5)
ax.errorbar(li[0], li[1], li[2], linestyle='none', color=d_blue[2], marker="^", markeredgecolor=d_blue[2], markerfacecolor='none', elinewidth=1, capsize=5)
ax.errorbar(li[3], li[4], li[5], linestyle='none', color=d_blue[1], marker="o", markeredgecolor=d_blue[1], markerfacecolor='none', elinewidth=1, capsize=5)
ax.errorbar(li[6][3:], li[7][3:], li[8][3:], linestyle='none', color=d_blue[0], marker="X", markeredgecolor=d_blue[0], markerfacecolor='none', elinewidth=1, capsize=5)

ax.plot(temp_r0, therm_exp_r0(temp_r0), linestyle='-', color=d_gold[5])
ax.plot(temp_r2, therm_exp_r2(temp_r2), linestyle=':', color=d_gold[4])
ax.plot(temp_r4, therm_exp_r4(temp_r4), linestyle='--', color=d_gold[3])
ax.plot(temp_r6, therm_exp_r6(temp_r6), linestyle='-.', color=d_gold[2])
ax.plot(temp_r8, therm_exp_r8(temp_r8), linestyle='-', color=d_gold[1])
ax.plot(temp_r1, therm_exp_r1(temp_r1), linestyle=':', color=d_gold[0])

ax.legend(["Exp: LiF-NaF: 1-0", "Exp: LiF-NaF: 4-1", "Exp: LiF-NaF: 3-2", "Exp: LiF-NaF: 2-3", "Exp: LiF-NaF: 1-4", "Exp: LiF-NaF: 0-1", "LiF-NaF: 1-0", "LiF-NaF: 4-1", "LiF-NaF: 1-1", "LiF-NaF: 0-1"], loc='upper left', fontsize='xx-small', frameon=True)

ax.plot(li[9], l4, linestyle='-', color=d_blue[3])
ax.plot(li[0], l1, linestyle=':', color=d_blue[2])
ax.plot(li[3], l2, linestyle='--', color=d_blue[1])
ax.plot(li[6][3:], l3[3:], linestyle='-.', color=d_blue[0])

ax.set_xlabel("$T$ (K)")
ax.set_ylim(.85, 1.75)
ax.set_xlim(975, 1525)
ax.set_ylabel(r"$\lambda$ (Wm$^{-1}$K$^{-1}$)")

plt.savefig(path + 'Thermal.pdf', format='pdf')
plt.show()
plt.clf()


#-------------------------------------------------------------------------

#-------------------------------------------------------------------------


li_1500 = [li[10][-1], li[1][-1], li[4][-1], li[7][-1]] 
li_1400 = [li[10][-2], li[1][-2], li[4][-2], li[7][-2]] 
li_1300 = [li[10][-3], li[1][-3], li[4][-3], li[7][-3]] 
li_ratio = [0, .2, .5, 1]

# li_1200 = [li[10][-4], li[1][-4], li[4][-4], li[7][-4]]
li_1200 = [li[10][-4], li[1][-4], li[4][-4]]
li_ratio_1200 = [0, .2, .5]

# li_1100 = [li[1][-5], li[4][-5], li[7][-5]]  
li_1100 = [li[1][-5], li[4][-5]]  
li_ratio_1100 = [.2, .5]

# li_1000 = [li[1][-6], li[4][-6], li[7][-6]]  
li_1000 = [li[1][-6], li[4][-6]]  
li_ratio_1000 = [.2, .5]

# exp_1150 = [therm_exp_r0(1150), therm_exp_r2(1150), therm_exp_r4(1150), therm_exp_r6(1150), therm_exp_r8(1150), therm_exp_r1(1150)]
# exp_ratio_1150 = [0, .2, .4, .6, .8, 1]

# exp_1200 = [therm_exp_r0(1200), therm_exp_r2(1200), therm_exp_r4(1200), therm_exp_r6(1200), therm_exp_r8(1200), therm_exp_r1(1200)]
# exp_ratio_1200 = [0, .2, .4, .6, .8, 1]

# exp_1250 = [therm_exp_r0(1250), therm_exp_r2(1250), therm_exp_r4(1250), therm_exp_r6(1250), therm_exp_r8(1250), therm_exp_r1(1250)]
# exp_ratio_1250 = [0, .2, .4, .6, .8, 1]

# exp_1300 = [therm_exp_r0(1300), therm_exp_r2(1300), therm_exp_r4(1300), therm_exp_r6(1300), therm_exp_r8(1300), therm_exp_r1(1300)]
# exp_ratio_1300 = [0, .2, .4, .6, .8, 1]

exp_1160 = [therm_exp_r0(1160), therm_exp_r2(1160), therm_exp_r4(1160), therm_exp_r6(1160),]
exp_ratio_1160 = [0, .2, .4, .6,]

exp_1215 = [therm_exp_r0(1215), therm_exp_r2(1215), therm_exp_r4(1215), therm_exp_r6(1215), therm_exp_r8(1215)]
exp_ratio_1215 = [0, .2, .4, .6, .8]

exp_1240 = [therm_exp_r0(1240), therm_exp_r2(1240), therm_exp_r4(1240), therm_exp_r6(1240), therm_exp_r8(1240),]
exp_ratio_1240 = [0, .2, .4, .6, .8,]

exp_1250 = [ therm_exp_r2(1250), therm_exp_r4(1250), therm_exp_r6(1250), therm_exp_r8(1250)]
exp_ratio_1250 = [.2, .4, .6, .8]

exp_1260 = [therm_exp_r2(1260), therm_exp_r4(1260), therm_exp_r6(1260), therm_exp_r8(1260), therm_exp_r1(1260)]
exp_ratio_1260 = [.2, .4, .6, .8, 1]

exp_1305 = [therm_exp_r8(1305), therm_exp_r1(1305)]
exp_ratio_1305 = [.8, 1]

colors = np.array([ 'gold', 'dodgerblue', 'yellowgreen', 'maroon', 'red', 'blue', 'green', 'orange', 'black', 'purple'])






# plt.plot(li_ratio, li_1500,linestyle='-',  color = d_blue[0], marker="X", markeredgecolor = d_blue[0], markerfacecolor='none')
# plt.plot(li_ratio, li_1400,linestyle='-',  color = d_blue[1], marker="^", markeredgecolor = d_blue[1], markerfacecolor='none')
# plt.plot(li_ratio, li_1300,linestyle='-', color = d_blue[2] , marker="o", markeredgecolor = d_blue[2], markerfacecolor='none')
# plt.plot(li_ratio_1200, li_1200,linestyle='-', color = d_blue[3] , marker="h", markeredgecolor = d_blue[3], markerfacecolor='none')
# plt.plot(li_ratio_1100, li_1100,linestyle='-', color = d_blue[4], marker="d", markeredgecolor = d_blue[4], markerfacecolor='none')
# plt.plot(li_ratio_1000, li_1000,linestyle='-', color = d_blue[5], marker="s", markeredgecolor = d_blue[5], markerfacecolor='none')


# plt.plot(exp_ratio_1305, exp_1305,linestyle='--', color = d_gold[0],marker="o", markeredgecolor = d_gold[0], markerfacecolor='none')
# plt.plot(exp_ratio_1260, exp_1260,linestyle='--', color = d_gold[1],marker="X", markeredgecolor = d_gold[0], markerfacecolor='none')
# plt.plot(exp_ratio_1215, exp_1215,linestyle='--', color = d_gold[2],marker="^", markeredgecolor = d_gold[0], markerfacecolor='none')
# plt.plot(exp_ratio_1160, exp_1160,linestyle='--', color = d_gold[3],marker="h", markeredgecolor = d_gold[0], markerfacecolor='none')




# plt.legend(["1500K", "1400K", "1300K", "1200K","1100K","1000", "Exp: 1305K", "Exp: 1260K", "Exp: 1215K", "Exp: 1160K"], frameon=True)
# plt.xlabel(r"Percent NaF in FLiNa")

# import matplotlib.ticker as mtick
# plt.gca().xaxis.set_major_formatter(mtick.PercentFormatter(1))

# plt.ylim(.85, 1.75)
# plt.ylabel(r"$\lambda$ (Wm$^{-1}$K$^{-1}$)")
# plt.savefig(path + 'Thermal_ratio.pdf', format='pdf')
# plt.show()

fig, ax = plt.subplots(1, 1, figsize=(6, 6), sharex=True)

ax.plot(li_ratio, li_1500, linestyle='-', color=d_blue[0], marker="X", markeredgecolor=d_blue[0], markerfacecolor='none')
ax.plot(li_ratio, li_1400, linestyle='-', color=d_blue[1], marker="^", markeredgecolor=d_blue[1], markerfacecolor='none')
ax.plot(li_ratio, li_1300, linestyle='-', color=d_blue[2], marker="o", markeredgecolor=d_blue[2], markerfacecolor='none')
ax.plot(li_ratio_1200, li_1200, linestyle='-', color=d_blue[3], marker="h", markeredgecolor=d_blue[3], markerfacecolor='none')
ax.plot(li_ratio_1100, li_1100, linestyle='-', color=d_blue[4], marker="d", markeredgecolor=d_blue[4], markerfacecolor='none')
ax.plot(li_ratio_1000, li_1000, linestyle='-', color=d_blue[5], marker="s", markeredgecolor=d_blue[5], markerfacecolor='none')

ax.plot(exp_ratio_1305, exp_1305, linestyle='--', color=d_gold[0], marker="o", markeredgecolor=d_gold[0], markerfacecolor='none')
ax.plot(exp_ratio_1260, exp_1260, linestyle='--', color=d_gold[1], marker="X", markeredgecolor=d_gold[0], markerfacecolor='none')
ax.plot(exp_ratio_1215, exp_1215, linestyle='--', color=d_gold[2], marker="^", markeredgecolor=d_gold[0], markerfacecolor='none')
ax.plot(exp_ratio_1160, exp_1160, linestyle='--', color=d_gold[3], marker="h", markeredgecolor=d_gold[0], markerfacecolor='none')

ax.legend(["1500K", "1400K", "1300K", "1200K", "1100K", "1000", "Exp: 1305K", "Exp: 1260K", "Exp: 1215K", "Exp: 1160K"], frameon=True)
ax.set_xlabel(r"Percent NaF in FLiNa")

import matplotlib.ticker as mtick
ax.xaxis.set_major_formatter(mtick.PercentFormatter(1))

ax.set_xlim(-.1, 1.1)
ax.set_ylim(.85, 1.75)
ax.set_ylabel(r"$\lambda$ (Wm$^{-1}$K$^{-1}$)")
plt.savefig(path + 'Thermal_ratio.pdf', format='pdf')
plt.show()
