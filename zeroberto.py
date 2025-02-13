x = Min 
c = mDMval 

# Create a color map
cmap = plt.get_cmap('rainbow')

# Normalize the color values to the range of c with a logarithmic scale
norm = LogNorm(vmin=c.min(), vmax=c.max())

fig, ax = plt.subplots(figsize=(7,5), tight_layout=True)

for ci in c:
    y = betatot(Min, ci, omega012)
    ax.plot(x, y, color=cmap(norm(ci)))

# Create a scalar mappable object for the color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])  # Only needed for matplotlib < 3.1


# Add the color bar with a logarithmic scale
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label(r'$m_{\rm DM}$ [GeV]', fontsize=16)

ax.set_xlim(1e4,2e8)
ax.set_ylim(1e-13,1e-8)

ax.set_xscale("log") # ou poderia fazer logo ax.loglog
ax.set_yscale("log")

ax.tick_params(axis="x", labelsize=16) 
ax.tick_params(axis="y", labelsize=16) 

ax.set_ylabel(r"$\beta$", fontsize=16)
ax.set_xlabel(r"$M_{\rm in}$ [g]",fontsize=16)

ax.set_title(r'$\Omega_{\rm DM}h^2 = 0.12$', fontsize=16)
ax.legend(fontsize=14, fancybox=True, loc='lower left')#, title=r'$ 3\times 10^{11} \leq m_{\rm DM} \leq 10^{18}\,{\rm GeV}$', title_fontsize=14)
plt.savefig("fig.pdf")
plt.show()
