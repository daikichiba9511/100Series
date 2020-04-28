using PyPlot
using Distributions

function main()
    x = 0:0.1:20
    fig = figure()
    for i in 1:11
        plot(x, pdf.(Chisq(i), x), label=string(i))
    end
    legend(loc="best")
    display(fig)
    savefig("./stats_ml_mathmatical_py/fig/fig1-3_jl.png")
    close(fig)
end

main()


