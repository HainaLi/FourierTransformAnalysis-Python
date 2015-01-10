
from scipy import *
from scipy import optimize
from wavefunction import *
from wavefunction.wavefunction1d import *

path_to_file = os.path.abspath('C:\Users\Haina\Desktop\chem 3821\csv files\HF (321).csv') #this sets the path to the file that you want to open
data = np.loadtxt(path_to_file,delimiter=",")

distancex = data[:,0]
energyy = data[:,1]

minvaluey = energyy[np.argmin(energyy)]
shiftx = distancex[np.argmin(energyy)]

for i in range(len(energyy)):
    energyy[i] = energyy[i] - minvaluey
    distancex[i] = distancex[i] - shiftx

def morse(r,re,alpha,De):
    return De*np.power((1-np.exp(-alpha*(r-re))),2)
    
guess = [.9,1,700]

optimizedresults, cov = scipy.optimize.curve_fit(morse,distancex,energyy,guess)

h = 6.626e-34
h_ = h/(2*pi)
e = 1.602e-19
cf = 1          # if cf = h_, use units where h_ = 1

mm = 1.58617e-27         # oscillator mass in kg
omega = 2 * pi  # oscillator frequency in GHz
x0 = 0          # shift in oscillator potiential minimum

D = optimizedresults[2]
b = optimizedresults[1]

args = {'D': D, 'b': b}
Na = 6.022e23

k = -h_ ** 2 * Na * 1.0e17/ (2 * mm)
#print "PREFACTOR" , k

x_min = -0.5 #in anstroms
x_max = 3
N = 750

def U_morse(x, args):
    """
    Morse oscillator potential
    """
    
    D = args['D']
    b = args['b']
    
    u = D * (1 - exp(-b*x)) ** 2

    return u
    
x = x = linspace(-.4, 2.1, N)

U = U_morse(x, args);

x_opt_min = optimize.fmin(U_morse, [0.0], (args,))



u = assemble_u_potential(N, U_morse, x, args)

K = assemble_K(N, k, x_min, x_max)

V = assemble_V(N, u, x_min, x_max)

H = K + V

evals, evecs = solve_eigenproblem(H)

fig, ax = subplots(figsize=(12,8))

ax.plot(x, U, 'k')
for n in range(25):
    Y = evals[n] + 100*evecs[n]

    mask = where(Y > U)    
    ax.plot(x[mask], evals[n] * ones(shape(x))[mask], 'k--')

    mask = where(Y > U-2.0)
    ax.plot(x[mask], Y[mask].real)
    
#ax.set_xlim(-1, 2)
#ax.set_ylim(0, 4)
ax.set_xlabel('Relative Distance (Angstroms)', fontsize=18)
ax.set_ylabel('Energy (KJ/mol)', fontsize=18);