from numpy import loadtxt, size, absolute
from pylab import plot, show, clf, xlim, ylim, xlabel, ylabel

data = loadtxt("millikan.txt", float)

x = data [:,0]
y = data [:, 1]

n = size(x)
Ex = sum(x)/n
Ey = sum(y)/n
Exx = sum(x**2)/n
Exy = sum(x*y)/n

m = (Exy - Ex*Ey)/(Exx - Ex**2)
c = (Ey*Exx - Ex*Exy)/(Exx - Ex**2)
print(m)
print(c)

model = m*x + c


plot(x,y, "bo")
plot(x,model, "r-")
xlim(0.52e15, 1.21e15)
ylim(0.4, 3.2)
xlabel(r'$\nu$ (Hz)')
ylabel('voltage (V)')
show()

e = 1.602e-19
h = m*e
h_actual = 6.62607004e-34

perc_diff = 100 * absolute((h_actual - h)/h_actual)

print("The measure value of planck's constant is ", h, " kg m^2 /s")
print("The actual value is ", h_actual, " kg m^2 /s")
print("The percent difference is ", perc_diff)









