using PyPlot
using Distributions

function main()
    x = -10:0.01:10
    fig = figure(figsize=(10, 10))
    normal_pdf = pdf.(Normal(0, 1), x)
    plot(x, normal_pdf, label="gaussian distribution")
    
    for i in 1:11
        t_dist_pdf = pdf.(TDist(i), x)
        plot(x, t_dist_pdf, label="free degree of t distribution = " * string(i))
    end
    grid()
    legend(loc="best")
    display(fig)
    savefig("./stats_ml_mathmatical_py/fig/t-dist_jl.png")
    close(fig)
end


# main
main()
