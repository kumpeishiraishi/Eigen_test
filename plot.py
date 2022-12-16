import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 14

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'TeX Gyre Heros'

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.top'] = True
plt.rcParams['xtick.bottom'] = True
plt.rcParams['ytick.left'] = True
plt.rcParams['ytick.right'] = True

Nsamp = np.array([10, 100, 1000, 3000, 10000])
eigen = np.empty(Nsamp.size)
mkl = np.empty(Nsamp.size)

for i, x in enumerate(Nsamp):
    eigen[i] = np.genfromtxt('./{:d}/Eigen/result.dat'.format(x))
    mkl[i] = np.genfromtxt('./{:d}/MKL/result.dat'.format(x))

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(Nsamp, eigen, 'ko-', label='Eigen')
ax.plot(Nsamp, mkl, 'rv-', label='MKL')
ax.set_xscale('log')
ax.set_yscale('log')

ax.legend(frameon=False)

ax.set_xlabel('N')
ax.set_ylabel('Elapsed time (smaller is better)')

plt.tight_layout(pad=0.25)
ax.xaxis.set_label_coords(0.5, -0.05)
ax.yaxis.set_label_coords(-0.08, 0.5)

plt.tight_layout(pad=0.25)
plt.savefig('./test.png')
